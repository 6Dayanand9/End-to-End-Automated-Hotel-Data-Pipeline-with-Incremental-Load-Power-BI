import mysql.connector
import pandas as pd
from pathlib import Path
import logging
import json
import os
import datetime


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


# ==============================
# 🔐 DATA SIGNATURE FUNCTION
# ==============================
def generate_data_signature(df):
    total_rows = len(df)

    first_row = tuple(df.iloc[0]) if total_rows > 0 else ()
    last_row = tuple(df.iloc[-1]) if total_rows > 0 else ()

    signature = str((total_rows, first_row, last_row))

    return signature


def incremental_ingestion():

    logging.info("[LOADING] Starting data loading process")
    print("🚀 Starting data loading...")

    file_path = BASE_PATH / "Data" / "clean_data.csv"
    TRACK_FILE = BASE_PATH / "loaded_files.json"

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
    # 🔐 GENERATE SIGNATURE
    # ==============================
    signature = generate_data_signature(df)

    # ==============================
    # 📂 LOAD TRACKING FILE
    # ==============================
    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r") as f:
            existing_data = json.load(f)
        logging.info("[LOADING] Tracking file loaded")
    else:
        existing_data = []
        logging.warning("[LOADING] No tracking file found, starting fresh")

    processed_signatures = set(item["signature"] for item in existing_data)

    # ==============================
    # ⛔ CHECK DUPLICATE DATA
    # ==============================
    if signature in processed_signatures:
        print("⏭️ Same data already loaded. Skipping...")
        logging.info("[LOADING] Duplicate data detected, skipping")
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
    # 🚀 INSERT DATA
    # ==============================
    columns = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))
    query = f"INSERT INTO fact_orders ({columns}) VALUES ({placeholders})"

    try:
        cursor.executemany(query, [tuple(row) for row in df.to_numpy()])
        conn.commit()

        print("✅ Data inserted successfully 🚀")
        logging.info("[LOADING] Data inserted successfully")

        # ==============================
        # ✅ UPDATE TRACKING
        # ==============================
        existing_data.append({
            "file_name": file_path.name,
            "signature": signature,
            "loaded_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        with open(TRACK_FILE, "w") as f:
            json.dump(existing_data, f, indent=4)

        logging.info("[LOADING] Tracking file updated")

    except Exception as e:
        print("❌ Error during insertion")
        logging.error(f"[LOADING] Insert error: {str(e)}")

    cursor.close()
    conn.close()

    logging.info("[LOADING] MySQL connection closed")
    logging.shutdown()


if __name__ == "__main__":
    incremental_ingestion()