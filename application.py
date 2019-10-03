import os
import requests
from flask import Flask, render_template, request

# grab the API key from the environment variable
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':  # user did not send anything
        return render_template("index.html")  # render the default homepage

    currency = request.form.get("currency")
    rate = get_rate(currency)
    return render_template("index.html", rate=rate, currency=currency)


def get_rate(currency):
    """
    gets the curent exchange rate of the given currency.
    :param currency: the currency to be checked against 1 EUR.
    :return: the rate of the currency relative to 1 EUR.
    """
    currency = currency.upper()
    r = requests.get(f"http://data.fixer.io/api/latest?access_key={API_KEY}&symbols={currency}")
    r = r.json()
    rate = r["rates"][currency]
    return rate


if __name__ == "__main__":
    app.run()
