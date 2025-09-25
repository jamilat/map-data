from src.processing.api import fetch_venues
import pandas as pd
from pathlib import Path


DATA_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
def venues():
    all_rows = [] # collect results in memory
    limit = 100
    offset = 0
    total_count = None
    
    while(total_count is None or offset < total_count):
        venues = fetch_venues(limit, offset)
        # API response
        results = venues.get("results", [])
        total_count = venues.get("total_count", len(results))

        if not results:
            break
        all_rows.extend(results)
        offset += 100

    df_venues = pd.DataFrame(all_rows)
    df_venues.to_csv(DATA_DIR / "venues.csv", index=False)
    print(f"Saved {len(df_venues)} venues to {DATA_DIR/'venues.csv'}")
    
    # For the JSON file:

    # Flatten lon/lat
    df_venues["lon"] = df_venues["geo_point_2d"].apply(lambda x: x["lon"])
    df_venues["lat"] = df_venues["geo_point_2d"].apply(lambda x: x["lat"])

    # Drop the nested dict columns if you don’t need them
    df_venues = df_venues.drop(columns=["geo_point_2d", "geo_shape"])

    # Save as JSON
    df_venues.to_json("data/processed/venues_with_flat_coords.json", orient="records", indent=2)
    print(f"Saved {len(df_venues)} venues to {PROCESSED_DIR/'venues_with_flat_coords.json'}")

def main():
    # Use the public wrapper (not _get)
    # venues()
    
    return

if __name__ == "__main__":
    main()
