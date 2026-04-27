import logging
from pathlib import Path

# ==============================
# 🔥 LOGGING SETUP
# ==============================
BASE_PATH = Path(__file__).resolve().parent
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
# 📦 IMPORT PIPELINE MODULES
# ==============================
from script.Data_extraction import data_extraction
from script.clean import data_clean
from script.incremental_ingestion_mysql import incremental_ingestion


def run_pipeline():
    print("\n🚀 Starting Full Data Pipeline...\n")
    logging.info("[PIPELINE]  Pipeline started")

    # ==============================
    # 1️⃣ EXTRACTION
    # ==============================
    try:
        data_extraction()
        print("\n✅ Extraction Completed\n")
        logging.info("[PIPELINE] Extraction completed successfully")
    except Exception as e:
        print("❌ Extraction Failed")
        logging.error(f"[PIPELINE] Extraction failed: {str(e)}")
        return

    # ==============================
    # 2️⃣ CLEANING
    # ==============================
    try:
        data_clean()
        print("\n✅ Cleaning Completed\n")
        logging.info("[PIPELINE] Cleaning completed successfully")
    except Exception as e:
        print("❌ Cleaning Failed")
        logging.error(f"[PIPELINE] Cleaning failed: {str(e)}")
        return

    # ==============================
    # 3️⃣ LOADING
    # ==============================
    try:
        incremental_ingestion()
        print("\n✅ Loading Completed\n")
        logging.info("[PIPELINE] Loading completed successfully")
    except Exception as e:
        print("❌ Loading Failed")
        logging.error(f"[PIPELINE] Loading failed: {str(e)}")
        return

    print("🎉 Pipeline Finished Successfully!")
    logging.info("[PIPELINE]  Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()