# api key - https://api.giphy.com/v1/stickers/search?api_key=F76P7UFFhVA322g5KsBWSqmrv2VhM43j&q=Happy&limit=25&offset=0&rating=g&lang=en

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    try:
        search = request.args.get("search")
        url = f"https://api.giphy.com/v1/stickers/search?api_key=F76P7UFFhVA322g5KsBWSqmrv2VhM43j&q={search}&limit=50&offset=0&rating=g&lang=en"
        url_data = requests.get(url)
        url_data = url_data.json()
        json_data = url_data["data"]
        return render_template("index.html", json_data=json_data)

    except:
        return render_template("error.html", search=search)

    return render_template("index.html")

app.run(debug=True)
