from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import requests
from io import StringIO, BytesIO
import json
import os
import datetime
import logging
from pathlib import Path


# ==============================
# 🔥 LOGGING SETUP (FIXED)
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


def data_extraction():

    print("🚀 Starting data extraction...")
    logging.info("[EXTRACTION] -> Starting data extraction process")

    SERVICE_ACCOUNT_FILE = "D:\\Data Analytics\\PROJECTS\\Food_Data_Analysis\\fetching-data-from-drive-bc2ee8f34bde.json"
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    STAGING_FOLDER_ID = '19kHynjk43QMv6MsGR4cs6Db9hAyHo5OO'
    TRACK_FILE = "processed_files.json"

    # ==============================
    # 🔗 CONNECT TO GOOGLE DRIVE
    # ==============================
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
        service = build('drive', 'v3', credentials=credentials)

        print("✅ Connected to Google Drive")
        logging.info("[EXTRACTION] Connected to Google Drive successfully")

    except Exception as e:
        print("❌ Failed to connect to Google Drive")
        logging.error(f"[EXTRACTION] Failed to connect: {str(e)}")
        return

    # ==============================
    # 📂 LOAD TRACKING FILE
    # ==============================
    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r") as f:
            existing_data = json.load(f)
        logging.info("[EXTRACTION] Tracking file loaded")
    else:
        existing_data = []
        logging.warning("[EXTRACTION] Tracking file not found, starting fresh")

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

    files = list_files(service, STAGING_FOLDER_ID)

    print(f"📂 Total files found: {len(files)}")
    logging.info(f"[EXTRACTION] Total files fetched: {len(files)}")

    file_dataframes = []

    # ==============================
    # 📥 FETCH FILES
    # ==============================
    for file in files:
        file_id = file['id']
        file_name = file['name']
        mime_type = file['mimeType']
        
        print(f"Processing: {file_name} | ID: {file_id}")
        logging.info(f"[EXTRACTION] Processing file: {file_name}")

        if file_id in processed_files:
            print(f"⏭️ Skipping already processed: {file_name}")
            logging.info(f"[EXTRACTION] Skipped already processed: {file_name}")
            continue

        if mime_type == 'application/vnd.google-apps.spreadsheet':
            download_url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv"

        elif mime_type in ['text/csv', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

        else:
            print(f"⚠️ Unsupported file: {file_name}")
            logging.warning(f"[EXTRACTION] Unsupported file skipped: {file_name}")
            continue

        try:
            response = requests.get(download_url)

            if response.status_code == 200:

                if mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                    df = pd.read_excel(BytesIO(response.content))
                else:
                    df = pd.read_csv(StringIO(response.content.decode('utf-8')))

                if not df.empty:
                    file_dataframes.append(df)

                    existing_data.append({
                        "file_id": file_id,
                        "file_name": file_name,
                        "processed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })

                    processed_files.add(file_id)

                    with open(TRACK_FILE, "w") as f:
                        json.dump(existing_data, f, indent=4)

                    print(f"✅ Processed: {file_name}")
                    logging.info(f"[EXTRACTION] Processed file: {file_name}")

                else:
                    print(f"⚠️ Empty file skipped: {file_name}")
                    logging.warning(f"[EXTRACTION] Empty file: {file_name}")

            else:
                print(f"❌ Download failed: {file_name}")
                logging.error(f"[EXTRACTION] Download failed: {file_name}")

        except Exception as e:
            print(f"❌ Error: {file_name}")
            logging.error(f"[EXTRACTION] Error processing {file_name}: {str(e)}")

    # ==============================
    # 🔗 COMBINE DATA
    # ==============================
    if not file_dataframes:
        print("⚠️ No new files processed")
        logging.warning("[EXTRACTION] No new files processed")
        return

    combined_df = pd.concat(file_dataframes, ignore_index=True)

    print("✅ Files combined")
    logging.info("[EXTRACTION] Files combined successfully")

    # ==============================
    # 💾 SAVE DATA
    # ==============================
    DATA_PATH = BASE_PATH / "Data"
    DATA_PATH.mkdir(exist_ok=True)

    file_path = DATA_PATH / "combined_data_raw.csv"
    combined_df.to_csv(file_path, index=False)

    print("Shape:", combined_df.shape)
    print(f"✅ Saved at: {file_path}")

    logging.info(f"[EXTRACTION] Final shape: {combined_df.shape}")
    logging.info(f"[EXTRACTION] Saved to: {file_path}")

    logging.shutdown()


if __name__ == "__main__":
    data_extraction()