import requests
from flask import Flask, request

from services.currency_converter import convert_currency

app = Flask(__name__)

@app.route('/')
def convert():
    data = request.get_json()
    from_currency = data['from_currency']
    to_currency = data['to_currency']
    amount = data['amount']

    convert_currency(amount, from_currency, to_currency)
