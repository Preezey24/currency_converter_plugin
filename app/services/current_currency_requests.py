import requests

def fetch_exchange_rates(base_currency, api_key):
    try:
        response = response = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_currency}&access_key={api_key}')
        response.raise_for_status()
        data = response.json()
        return data['rates']
    except requests.exceptions.RequestException as e:
        print(f'Error fetching exchange rates: {e}')