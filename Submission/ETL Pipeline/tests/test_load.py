from unittest.mock import MagicMock, patch

import pandas as pd

from utils.load import save_to_csv, save_to_google_sheets, save_to_postgresql


def test_save_to_csv(tmp_path):
    df = pd.DataFrame(
        [
            {
                "Title": "Test Product",
                "Price": 1600000,
                "Rating": 4.5,
                "Colors": 3,
                "Size": "M",
                "Gender": "Male",
                "Timestamp": "2025-09-01T00:00:00",
            }
        ]
    )
    file_path = tmp_path / "test_output.csv"
    save_to_csv(df, filename=str(file_path))
    assert file_path.exists()
    loaded_df = pd.read_csv(file_path)
    assert loaded_df.equals(df)


@patch("utils.load.gspread.authorize")
@patch("utils.load.Credentials.from_service_account_file")
def test_save_to_google_sheets(mock_creds, mock_auth):
    df = pd.DataFrame([{"Title": "Test", "Price": 1600000}])
    mock_client = MagicMock()
    mock_sheet = MagicMock()
    mock_client.open_by_key.return_value.sheet1 = mock_sheet
    mock_auth.return_value = mock_client

    save_to_google_sheets(df, "fake_sheet_id", "fake_creds.json")
    mock_sheet.clear.assert_called_once()
    mock_sheet.update.assert_called_once()


@patch("utils.load.create_engine")
def test_save_to_postgresql(mock_create_engine):
    df = pd.DataFrame([{"Title": "Test", "Price": 1600000}])

    # Mock engine dan koneksi
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    # Mock method to_sql di DataFrame
    with patch.object(pd.DataFrame, "to_sql") as mock_to_sql:
        save_to_postgresql(df, "postgresql://user:pass@localhost:5432/db")
        mock_to_sql.assert_called_once_with(
            "products", mock_engine, if_exists="replace", index=False
        )
