from utils.extract import extract_all
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgresql
from utils.transform import transform_data


def main():
    try:
        print("📥 Mulai proses ekstraksi data...")
        raw_df = extract_all()
        print(f"✅ Data mentah berhasil diambil: {len(raw_df)} baris")

        print("🧼 Mulai proses transformasi data...")
        clean_df = transform_data(raw_df)
        print(f"✅ Data bersih siap digunakan: {len(clean_df)} baris")

        print("💾 Simpan data ke CSV...")
        save_to_csv(clean_df)

        print("📤 Simpan data ke Google Sheets...")
        sheet_id = "1EQy7IRyEHTaQUzFfWNC5mIZtDpaoFJmBEQwuCz-GDS8"  # Ganti dengan ID Google Sheets lo
        creds_json = "google-sheets-api.json"
        save_to_google_sheets(clean_df, sheet_id, creds_json)

        print("🗄️ Simpan data ke PostgreSQL...")
        db_url = "postgresql://postgres:12345678@localhost:5432/etl_db"

        # Ganti sesuai koneksi lo
        save_to_postgresql(clean_df, db_url)

        print("🎉 ETL pipeline selesai dijalankan!")

    except Exception as e:
        print(f"❌ Error di main pipeline: {e}")


if __name__ == "__main__":
    main()
