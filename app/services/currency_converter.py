from current_currency_requests import fetch_exchange_rates

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    exchange_rates = fetch_exchange_rates(from_currency)

    if not exchange_rates:
        print('Failed to fetch exchange rates. Conversion not possible.')
        return None

    rate = exchange_rates.get(to_currency)

    if not rate:
        print(f'Exchange rate for {to_currency} not found.')
        return None

    return amount * rate