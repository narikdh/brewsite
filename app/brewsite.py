from flask import Flask
from flask import render_template as rt
import requests, json, warnings
response = requests.get("https://api.openbrewerydb.org/v1/breweries")
data = json.loads(response.content)

beer_styles_response = requests.get(
    "https://api.catalog.beer/style",
    auth=("4cca85cc-5488-41a1-ba00-26aea923914d", ""),
    headers={"accept": "application/json"}
)
beer_styles = json.loads(beer_styles_response.content)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user = "Nick Cessac")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", content = data)

@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html", content = beer_styles["data"])

@app.route("/about")
def about():
    return rt("about.html", user = "Nick Cessac")

if __name__ == "__main__":
    app.run(debug=True)