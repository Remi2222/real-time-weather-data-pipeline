import requests

def fetch_data(url):
    print("Fetching data from Weather API...")

    try:
        response = requests.get(url)
        response.raise_for_status()

        print("API Request Successful")
        return response.json()

    except requests.RequestException as e:
        print(f"Error fetching data from {url}")
        print(e)
        raise