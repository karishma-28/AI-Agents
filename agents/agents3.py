import requests

def fetch_from_internet(query: str) -> dict:
    response = requests.get(f"https://api.duckduckgo.com/?q={query}&format=json")
    data = response.json()
    return {
        "query": query,
        "response": data.get("AbstractText", "No data found."),
        "source": data.get("AbstractURL", "Unknown")
    }
