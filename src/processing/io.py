import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

def save_csv(df: pd.DataFrame, filename: str):
    path = DATA_DIR / "processed" / filename
    df.to_csv(path, index=False)

def load_csv(filename: str) -> pd.DataFrame:
    path = DATA_DIR / "processed" / filename
    return pd.read_csv(path)

def load_json(filename: str) -> pd.DataFrame:
    path = DATA_DIR / "processed" / filename
    return pd.read_json(path)

