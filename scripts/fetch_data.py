from src.processing.api import fetch_venues, fetch_data
import pandas as pd
from pathlib import Path


DATA_DIR = Path("data/raw")

def main():
    # Use the public wrapper (not _get)
    venues = fetch_venues(limit=20)
    print(venues)
    # df_venues = pd.DataFrame(venues)
    # df_venues.to_csv(DATA_DIR / "venues.csv", index=False)

if __name__ == "__main__":
    main()
