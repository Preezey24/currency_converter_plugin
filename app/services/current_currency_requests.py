import requests

def fetch_exchange_rates(base_currency, api_key):
    try:
        headers = {
        'apikey': f'{api_key}'
        }
        response = response = requests.get(f'https://api.apilayer.com/exchangerates_data/latest?base={base_currency}', headers=headers)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data['rates']
    except requests.exceptions.RequestException as e:
        print(f'Error fetching exchange rates: {e}')
