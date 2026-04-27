import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
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


def data_clean():

    logging.info("[CLEANING] -> Starting data cleaning process")
    print("🧹 Starting data cleaning...")

    base_path = Path(__file__).resolve().parent.parent
    file_path = base_path / "Data" / "combined_data_raw.csv"

    print("Reading from:", file_path)
    logging.info(f"[CLEANING] Reading raw data from: {file_path}")

    try:
        df = pd.read_csv(file_path)
        logging.info(f"[CLEANING] Raw data loaded successfully. Shape: {df.shape}")
    except Exception as e:
        print("❌ Failed to read raw data")
        logging.error(f"[CLEANING] Error reading file: {str(e)}")
        return

    # Drop columns
    df.drop(columns=['year','month'], inplace=True, errors='ignore')
    logging.info("[CLEANING] Dropped unnecessary columns")

    # Clean column names
    new_columns = []
    for col in df.columns:
        col = col.strip()
        col = col.lower()
        col = col.replace(' ', '_')
        new_columns.append(col)

    df.columns = new_columns
    logging.info("[CLEANING] Column names cleaned")

    # Rename columns
    df.rename(columns={
        'delivery_time_(in_mins)': 'delivery_time_in_mins',
        'discounts_offered_(%)': 'discounts_offered_pct',
        'average_rating.1': 'average_rating_1',
        'competitors_in_the_area_(count)': 'competitors_in_the_area_count'
    }, inplace=True)
    logging.info("[CLEANING] Columns renamed")

    # Remove duplicates
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    logging.info(f"[CLEANING] Duplicates removed: {before - after}")

    # Convert date
    df['order_delivered_date'] = pd.to_datetime(
        df['order_delivered_date'],
        format='mixed',
        errors='coerce'
    )
    logging.info("[CLEANING] Date column converted")

    # Convert time columns
    for col in ['time_of_order', 'time_of_delivery']:
        df[col] = pd.to_timedelta(df[col]).dt.round('1s')

    logging.info("[CLEANING] Time columns converted to timedelta")

    # Remove invalid rows
    before = df.shape[0]
    df = df[df['time_of_order'] <= df['time_of_delivery']]
    logging.info(f"[CLEANING] Invalid time rows removed: {before - df.shape[0]}")

    # Filter <= 2 hours
    before = df.shape[0]
    df = df[
        (df['time_of_delivery'] - df['time_of_order']) <= pd.Timedelta(hours=2)
    ]
    logging.info(f"[CLEANING] Rows filtered (>2hrs removed): {before - df.shape[0]}")

    # Convert back to HH:MM:SS
    for col in ['time_of_order', 'time_of_delivery']:
        df[col] = df[col].astype(str).str.split().str[-1]

    logging.info("[CLEANING] Time columns formatted for MySQL")

    # Create date_id
    df['date_id'] = df['order_delivered_date'].dt.strftime('%Y%m%d').astype(int)

    # Reorder columns
    cols = ['date_id'] + [col for col in df.columns if col != 'date_id']
    df = df[cols]

    # Drop original date
    df.drop(columns=['order_delivered_date'], inplace=True)

    print("Final Shape:", df.shape)
    logging.info(f"[CLEANING] Final cleaned data shape: {df.shape}")

    # ==============================
    # 💾 SAVE CLEAN DATA
    # ==============================
    CLEAN_PATH = BASE_PATH / "data"
    CLEAN_PATH.mkdir(parents=True, exist_ok=True)

    file_path = CLEAN_PATH / "clean_data.csv"

    df.to_csv(file_path, index=False)

    print(f"✅ Data saved successfully at: {file_path}")
    logging.info(f"[CLEANING] Clean data saved at: {file_path}")

    logging.shutdown()


if __name__ == "__main__":
    data_clean()