import pandas as pd


def clean_price(price_str):
    try:
        price_value = float(price_str.replace("$", "").replace(",", ""))
        return float(price_value * 16000)
    except:
        return None


def clean_rating(rating_str):
    try:
        rating_value = rating_str.split("⭐")[-1].split("/")[0].strip()
        return float(rating_value)
    except:
        return None


def clean_colors(colors_str):
    try:
        return int(colors_str.split()[0])
    except:
        return None


def clean_size(size_str):
    return size_str.replace("Size: ", "").strip()


def clean_gender(gender_str):
    return gender_str.replace("Gender: ", "").strip()


def transform_data(df):
    try:
        df = df.copy()

        # Bersihin dan ubah data
        df["Price"] = df["Price"].apply(clean_price)
        df["Rating"] = df["Rating"].apply(clean_rating)
        df["Colors"] = df["Colors"].apply(clean_colors)
        df["Size"] = df["Size"].apply(clean_size)
        df["Gender"] = df["Gender"].apply(clean_gender)

        # Drop null dan duplikat
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        # Pastikan tipe data
        df = df.astype(
            {
                "Title": str,
                "Price": float,
                "Rating": float,
                "Colors": int,
                "Size": str,
                "Gender": str,
                "Timestamp": str,
            }
        )

        return df

    except Exception as e:
        print(f"❌ Error during transformation: {e}")
        return pd.DataFrame()
