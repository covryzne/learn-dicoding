import pandas as pd

from utils.transform import (
    clean_colors,
    clean_gender,
    clean_price,
    clean_rating,
    clean_size,
    transform_data,
)


def test_clean_price():
    assert clean_price("$100.00") == 1600000
    assert clean_price("$0.00") == 0
    assert clean_price("invalid") is None


def test_clean_rating():
    assert clean_rating("⭐ 4.5 / 5") == 4.5
    assert clean_rating("⭐ 3.0 / 5") == 3.0
    assert clean_rating("Invalid Rating") is None


def test_clean_colors():
    assert clean_colors("3 Colors") == 3
    assert clean_colors("invalid") is None


def test_clean_size():
    assert clean_size("Size: M") == "M"
    assert clean_size("Size: XL") == "XL"


def test_clean_gender():
    assert clean_gender("Gender: Male") == "Male"
    assert clean_gender("Gender: Female") == "Female"


def test_transform_data_full():
    raw_df = pd.DataFrame(
        [
            {
                "Title": "Cool Shirt",
                "Price": "$100.00",
                "Rating": "⭐ 4.5 / 5",
                "Colors": "3 Colors",
                "Size": "Size: M",
                "Gender": "Gender: Male",
                "Timestamp": "2025-09-01T00:00:00",
            }
        ]
    )
    clean_df = transform_data(raw_df)
    assert clean_df["Price"].iloc[0] == 1600000
    assert clean_df["Rating"].iloc[0] == 4.5
    assert clean_df["Colors"].iloc[0] == 3
    assert clean_df["Size"].iloc[0] == "M"
    assert clean_df["Gender"].iloc[0] == "Male"
