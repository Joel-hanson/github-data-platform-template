import json
import os
import random
import time
from datetime import datetime

import requests


def scrape_data():
    """
    Main data scraping function - CUSTOMIZE THIS FOR YOUR DATA SOURCE

    Replace the example below with your actual data source.
    This template uses JSONPlaceholder as a demo API.
    """
    try:
        # REPLACE THIS URL with your data source
        url = "https://jsonplaceholder.typicode.com/posts"

        # Add proper headers for respectful scraping
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; DataBot/1.0; +https://github.com/your-username/your-repo)",
            "Accept": "application/json",
        }

        # Fetch data with retry logic
        response = fetch_with_retry(url, headers)
        raw_data = response.json()

        # Process and clean the data
        processed_data = process_data(raw_data)

        # Save to API endpoints
        save_api_data(processed_data)

        print(f"Successfully updated data: {len(processed_data)} items")
        return True

    except Exception as e:
        print(f"Error scraping data: {e}")
        return False


def fetch_with_retry(url, headers, max_retries=3):
    """Fetch data with exponential backoff retry logic"""
    for attempt in range(max_retries):
        try:
            # Add random delay to be respectful
            time.sleep(random.uniform(1, 3))

            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response

        except requests.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = (2**attempt) + random.uniform(0, 1)
                print(f"⚠️ Attempt {attempt + 1} failed, retrying in {wait_time:.1f}s")
                time.sleep(wait_time)
            else:
                raise e


def process_data(raw_data):
    """
    Process and clean raw data - CUSTOMIZE THIS FOR YOUR DATA

    Transform the raw data into your desired API format.
    """
    processed_items = []

    for item in raw_data[:10]:  # Limit to first 10 items for demo
        processed_item = {
            "id": item.get("id"),
            "title": item.get("title", "").title(),
            "body": item.get("body", "")[:100] + "...",  # Truncate for demo
            "user_id": item.get("userId"),
            "processed_at": datetime.now().isoformat(),
        }
        processed_items.append(processed_item)

    return processed_items


def save_api_data(data):
    """Save processed data to API endpoints"""

    # Ensure api directory exists
    os.makedirs("api", exist_ok=True)

    # Create API response structure
    api_response = {
        "last_updated": datetime.now().isoformat(),
        "total_items": len(data),
        "data": data,
        "meta": {"source": "GitHub Data Platform Template", "version": "1.0.0"},
    }

    # Save JSON endpoint
    with open("api/latest.json", "w") as f:
        json.dump(api_response, f, indent=2, ensure_ascii=False)

    # Save JSONP endpoint for cross-origin requests
    with open("api/latest.jsonp", "w") as f:
        jsonp_data = f"callback({json.dumps(api_response, ensure_ascii=False)});"
        f.write(jsonp_data)

    # Update historical data
    update_historical_data(data)


def update_historical_data(new_data):
    """Maintain historical data with rolling window"""
    try:
        with open("data/historical.json", "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    # Add new data with timestamp
    history.append(
        {
            "timestamp": datetime.now().isoformat(),
            "data_count": len(new_data),
            "sample": new_data[:3] if new_data else [],  # Store sample for history
        }
    )

    # Keep only last 30 entries (30 days if daily updates)
    history = history[-30:]

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)

    with open("data/historical.json", "w") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def validate_data(data):
    """Validate data quality before publishing"""
    if not data:
        raise ValueError("No data received")

    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    # Add your specific validation logic here
    for item in data:
        if not isinstance(item, dict):
            raise ValueError(f"Invalid item format: {item}")

    return True


if __name__ == "__main__":
    print("🚀 Starting data collection...")
    success = scrape_data()

    if success:
        print("Data collection completed successfully!")
        exit(0)
    else:
        print("Data collection failed!")
        exit(1)
