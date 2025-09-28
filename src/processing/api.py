import os
import requests
from typing import Any, Dict, Optional
from dotenv import load_dotenv
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

# Load .env file
load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "https://example.com/api/v1")
API_KEY = os.getenv("API_KEY")

HEADERS = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}

def _get(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Internal helper to perform GET requests with error handling."""
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    response = requests.get(url, headers=HEADERS, params=params, timeout=10)

    # Raise an error if request failed
    response.raise_for_status()
    return response.json()

def fetch_venues(limit: int = 100, offset: int = 0) -> list[Dict[str, Any]]:
    """Fetch venues from the API."""
    return _get(f"venues-for-event-bookings/records?limit={limit}&offset={offset}")

def fetch_cafes(limit: int = 100, offset: int = 0) -> list[Dict[str, Any]]:
    """Fetch cafes"""
    return _get(f"cafes-and-restaurants-with-seating-capacity/records?where=census_year%20%3E%3D%20'2023-01-01'%20AND%20census_year%20%3C%20'2024-01-01'&limit={limit}&offset={offset}")

def _get_chunk(endpoint, limit, offset):
    return _get(endpoint % (limit, offset))

def fetch_by_chunk(endpoint: str, out: str) -> list[Dict[str, Any]]:
    """Fetch data."""
    all_rows = [] # collect results in memory
    limit = 100
    offset = 0
    total_count = None
    
    while(total_count is None or offset < total_count):
        response = _get_chunk(endpoint, limit, offset)
        # API response
        results = response.get("results", [])
        total_count = response.get("total_count", len(results))

        if not results:
            break
        all_rows.extend(results)
        offset += 100

    df = pd.DataFrame(all_rows)
    df.to_csv(PROCESSED_DIR / f"{out}.csv", index=False)
    print(f"Saved {len(df)} venues to {PROCESSED_DIR/f'{out}.csv'}")
    
    
