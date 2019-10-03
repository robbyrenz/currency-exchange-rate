import os
from flask import Flask, render_template, request

# grab the API key from the environment variable
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
