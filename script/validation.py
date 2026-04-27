import pandas as pd
from pathlib import Path

def get_cleaned_data_count():
    BASE_PATH = Path(__file__).resolve().parent.parent
    file_path = BASE_PATH / "data" / "clean_data.csv"

    if not file_path.exists():
        raise FileNotFoundError("❌ clean_data.csv not found. Please run cleaning first.")

    df = pd.read_csv(file_path)
    return df.shape[0]

