import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from sqlalchemy import create_engine


def save_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"✅ Data disimpan ke {filename}")
    except Exception as e:
        print(f"❌ Error simpan ke CSV: {e}")


def save_to_google_sheets(df, sheet_id, creds_json):
    try:
        # Setup credentials
        scope = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(creds_json, scopes=scope)
        client = gspread.authorize(creds)

        # Buka spreadsheet dan sheet pertama
        sheet = client.open_by_key(sheet_id).sheet1

        # Clear isi lama dan update dengan data baru
        sheet.clear()
        sheet.update([df.columns.values.tolist()] + df.values.tolist())

        print("✅ Data berhasil disimpan ke Google Sheets")

    except Exception as e:
        print(f"❌ Error simpan ke Google Sheets: {e}")


def save_to_postgresql(df, db_url, table_name="products"):
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print("✅ Data disimpan ke PostgreSQL")
    except Exception as e:
        print(f"❌ Error simpan ke PostgreSQL: {e}")
