import os
import sys

import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.extract import extract_all


def test_extract_all_returns_dataframe():
    df = extract_all()
    assert isinstance(df, pd.DataFrame), "Output harus berupa DataFrame"


def test_extract_all_has_required_columns():
    df = extract_all()
    required_columns = [
        "Title",
        "Price",
        "Rating",
        "Colors",
        "Size",
        "Gender",
        "Timestamp",
    ]
    for col in required_columns:
        assert col in df.columns, f"Kolom '{col}' harus ada di hasil ekstraksi"


def test_extract_all_has_data():
    df = extract_all()
    assert len(df) > 0, "Data hasil ekstraksi tidak boleh kosong"


def test_extract_all_no_invalid_titles():
    df = extract_all()
    assert (
        not df["Title"].str.contains("Unknown Product").any()
    ), "Data tidak boleh mengandung 'Unknown Product'"


def test_extract_all_no_invalid_ratings():
    df = extract_all()
    assert (
        not df["Rating"].str.contains("Invalid Rating").any()
    ), "Data tidak boleh mengandung 'Invalid Rating'"
