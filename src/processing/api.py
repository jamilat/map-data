import os
import requests
from typing import Any, Dict, Optional
from dotenv import load_dotenv

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

def fetch_data(param: int) -> list[Dict[str, Any]]:
    """Fetch data."""
    return _get(f"data/{param}")
