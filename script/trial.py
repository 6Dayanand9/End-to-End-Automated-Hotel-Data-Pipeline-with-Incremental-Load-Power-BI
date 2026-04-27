from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import requests
from io import StringIO, BytesIO
import json
import os
import datetime

def data_extraction():

    SERVICE_ACCOUNT_FILE = "D:\\Data Analytics\\PROJECTS\\Food_Data_Analysis\\fetching-data-from-drive-bc2ee8f34bde.json"

    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    STAGING_FOLDER_ID = '19kHynjk43QMv6MsGR4cs6Db9hAyHo5OO'

    TRACK_FILE = "processed_files.json"

    # ==============================
    # 🔗 CONNECT TO GOOGLE DRIVE
    # ==============================

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    service = build('drive', 'v3', credentials=credentials)

    # ==============================
    # 📂 LOAD TRACKING FILE
    # ==============================

    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r") as f:
            existing_data = json.load(f)
    else:
        existing_data = []

    # Create set for fast lookup
    processed_files = set(item["file_id"] for item in existing_data)

    # ==============================
    # 📂 LIST FILES
    # ==============================

    def list_files(service, folder_id):
        results = service.files().list(
            q=f"'{folder_id}' in parents",
            fields="files(id, name, mimeType)"
        ).execute()
        return results.get('files', [])

    # ==============================
    # 📥 FETCH FILES
    # ==============================

    files = list_files(service, STAGING_FOLDER_ID)

    file_dataframes = []

    for file in files:
        file_id = file['id']
        file_name = file['name']
        mime_type = file['mimeType']
        
        print(f"Processing: {file_name} | ID: {file_id}")

        # ⛔ Skip already processed files
        if file_id in processed_files:
            print(f"⏭️ Skipping already processed: {file_name}")
            continue

        # Determine download URL
        if mime_type == 'application/vnd.google-apps.spreadsheet':
            download_url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv"

        elif mime_type == 'text/csv':
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

        elif mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

        else:
            print(f"Skipping unsupported file: {file_name}")
            continue

        try:
            response = requests.get(download_url)

            if response.status_code == 200:
                # Read into DataFrame
                if mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                    df = pd.read_excel(BytesIO(response.content))
                else:
                    df = pd.read_csv(StringIO(response.content.decode('utf-8')))

                # ✅ Process only if not empty
                if not df.empty:
                    file_dataframes.append(df)

                    # ✅ Add metadata to tracking
                    existing_data.append({
                        "file_id": file_id,
                        "file_name": file_name,
                        "processed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })

                    # Update set
                    processed_files.add(file_id)

                    # Save JSON (pretty format)
                    with open(TRACK_FILE, "w") as f:
                        json.dump(existing_data, f, indent=4)

                    print(f"✅ Processed & tracked: {file_name}")
                else:
                    print(f"⚠️ Empty file skipped: {file_name}")

            else:
                print(f"❌ Download failed: {file_name}")

        except Exception as e:
            print(f"❌ Error processing {file_name}: {str(e)}")

    # ==============================
    # 🔗 COMBINE DATA
    # ==============================

    if file_dataframes:
        combined_df = pd.concat(file_dataframes, ignore_index=True)
        print("✅ All files combined successfully")
        
    else:
        print("⚠️ No new files processed")
    
    output_folder = "Data"
    os.makedirs(output_folder, exist_ok=True)

    # Option 1: overwrite every run (latest snapshot)
    file_path = os.path.join(output_folder, "combined_data_raw.csv")
    combined_df.to_csv(file_path, index=False)
    print(combined_df.shape)
    print(f"✅ Combined data saved to: {file_path}")

if __name__ == "__main__":
    data_extraction()

# ---------------------------------------------------------------------------

import mysql.connector
import pandas as pd
from pathlib import Path
import logging


# ==============================
# 🔥 LOGGING SETUP
# ==============================
BASE_PATH = Path(__file__).resolve().parent.parent
LOG_PATH = BASE_PATH / "logs"
LOG_PATH.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH / "pipeline.log"),
        logging.StreamHandler()
    ],
    force=True
)


def incremental_ingestion():

    logging.info("[LOADING] -> Starting data loading process")
    print("🚀 Starting data loading...")

    base_path = Path(__file__).resolve().parent.parent
    file_path = base_path / "Data" / "clean_data.csv"

    print("Reading from:", file_path)
    logging.info(f"[LOADING] Reading clean data from: {file_path}")

    # ==============================
    # 📥 READ DATA
    # ==============================
    try:
        df = pd.read_csv(file_path)
        logging.info(f"[LOADING] Data loaded successfully. Shape: {df.shape}")
    except Exception as e:
        print("❌ Failed to read clean data")
        logging.error(f"[LOADING] Error reading file: {str(e)}")
        return

    # ==============================
    # 🔗 MySQL Connection
    # ==============================
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="food_data_model"
        )
        cursor = conn.cursor()

        logging.info("[LOADING] Connected to MySQL successfully")

    except Exception as e:
        print("❌ Database connection failed")
        logging.error(f"[LOADING] DB connection error: {str(e)}")
        return

    # ==============================
    # 🧠 Create Insert Query
    # ==============================
    columns = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))

    query = f"INSERT INTO fact_orders ({columns}) VALUES ({placeholders})"
    logging.info("[LOADING] Insert query prepared")

    # ==============================
    # 🔄 Convert DataFrame → Tuples
    # ==============================
    data = [tuple(row) for row in df.to_numpy()]
    logging.info(f"[LOADING] Converted data to tuples. Total rows: {len(data)}")

    # ==============================
    # 🚀 Batch Insert
    # ==============================
    batch_size = 1000
    total_inserted = 0

    try:
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]
            cursor.executemany(query, batch)
            conn.commit()
            total_inserted += len(batch)

        print("✅ Data inserted successfully 🚀")
        logging.info(f"[LOADING] Data inserted successfully. Total rows: {total_inserted}")

    except Exception as e:
        print("❌ Error during insertion")
        logging.error(f"[LOADING] Insert error: {str(e)}")

    # ==============================
    # 🔚 Close Connection
    # ==============================
    cursor.close()
    conn.close()

    logging.info("[LOADING] MySQL connection closed")
    logging.shutdown()


if __name__ == "__main__":
    incremental_ingestion()