import streamlit as st
from pathlib import Path
from script.sql_queries import get_row_count
import time

# ==============================
# 📦 IMPORT PIPELINE MODULES
# ==============================
from script.Data_extraction import data_extraction
from script.clean import data_clean
from script.incremental_ingestion_mysql import incremental_ingestion

# ==============================
# 🔥 PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="ETL Pipeline Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Data Pipeline Dashboard")
st.write("Run your ETL pipeline step-by-step or all at once.")

# ==============================
# 🔘 STEP BUTTONS
# ==============================
col1, col2, col3 = st.columns(3)

# -------- EXTRACTION --------
with col1:
    if st.button("📥 Run Extraction"):
        status = st.empty()
        status.info("🟡 Extraction Running...")
        try:
            data_extraction()
            status.success("🟢 Extraction Completed")
        except Exception as e:
            status.error(f"🔴 Extraction Failed: {str(e)}")

# -------- CLEANING --------
with col2:
    if st.button("🧹 Run Cleaning"):
        status = st.empty()
        status.info("🟡 Cleaning Running...")
        try:
            data_clean()
            status.success("🟢 Cleaning Completed")
        except Exception as e:
            status.error(f"🔴 Cleaning Failed: {str(e)}")

# -------- LOADING + VALIDATION --------
with col3:
    if st.button("📤 Run Loading"):

        status = st.empty()
        validation_box = st.empty()

        try:
            # 🔹 BEFORE COUNT
            before_count = get_row_count()

            status.info("🟡 Loading Running...")
            incremental_ingestion()

            # 🔹 AFTER COUNT
            after_count = get_row_count()

            # 🔹 DIFFERENCE (ACTUAL INSERTED ROWS)
            inserted_rows = after_count - before_count

            status.success("🟢 Loading Completed")

            # 🔥 VALIDATION MESSAGE
            if inserted_rows == 0:
                validation_box.warning(f"""
📊 Data Validation

📌 Before Load: {before_count}  
📌 After Load: {after_count}  
📥 Rows Inserted: {inserted_rows}  

⚠️ No new data loaded (Duplicate data detected)
""")
            else:
                validation_box.success(f"""
📊 Data Validation

📌 Before Load: {before_count}  
📌 After Load: {after_count}  
📥 Rows Inserted: {inserted_rows}  

✅ New data successfully loaded
""")

        except Exception as e:
            status.error(f"🔴 Loading Failed: {str(e)}")

# ==============================
# 🚀 FULL PIPELINE WITH VALIDATION
# ==============================
st.markdown("---")

if st.button("🚀 Run Full Pipeline"):

    progress = st.progress(0)
    status = st.empty()
    validation_box = st.empty()

    try:
        # 🔹 BEFORE COUNT
        before_count = get_row_count()

        # Step 1 - Extraction
        status.info("🟡 Extraction Running...")
        data_extraction()
        progress.progress(33)

        # Step 2 - Cleaning
        status.info("🟡 Cleaning Running...")
        data_clean()
        progress.progress(66)

        # Step 3 - Loading
        status.info("🟡 Loading Running...")
        incremental_ingestion()
        progress.progress(100)

        # 🔹 AFTER COUNT
        after_count = get_row_count()

        # 🔹 DIFFERENCE
        inserted_rows = after_count - before_count

        status.success("🟢 Pipeline Completed")

        # 🔥 VALIDATION MESSAGE
        if inserted_rows == 0:
            validation_box.warning(f"""
📊 Data Validation

📌 Before Load: {before_count}  
📌 After Load: {after_count}  
📥 Rows Inserted: {inserted_rows}  

⚠️ No new data loaded (Duplicate data detected)
""")
        else:
            validation_box.success(f"""
📊 Data Validation

📌 Before Load: {before_count}  
📌 After Load: {after_count}  
📥 Rows Inserted: {inserted_rows}  

🎉 Pipeline Finished Successfully!
""")

    except Exception as e:
        status.error(f"🔴 Pipeline Failed: {str(e)}")

# ==============================
# 📄 LOG VIEWER
# ==============================
st.markdown("---")
st.subheader("📄 Pipeline Logs")

BASE_PATH = Path(__file__).resolve().parent
log_path = BASE_PATH / "logs" / "pipeline.log"

if log_path.exists():
    with open(log_path, "r", encoding="utf-8") as f:
        logs = f.read()

    st.text_area("Logs", logs, height=300)
else:
    st.warning("No logs found yet.")