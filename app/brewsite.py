""" Project 1: Flask App
Release Date: October 8, 2026
Code Author: N. Cessac
Description: This application is designed to demonstrate the use of Git and Github to maintain version control on a site built in Python with Flask, templates, requests, json, apis, and testing, to build a brewery website.  It creates multple pages using templates to design the overall page, with content on each page to fill out each page.  
"""
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

@app.route("/") # routes the root site to home
@app.route("/home") 
def home(): # Renders the homepage, passing a default user to personalize the greeting
    return rt("home.html", user = "Nick Cessac")

@app.route("/breweries")
def breweries(): # Renders the breweries page using the brewey data fetched from the above API
    return rt("breweries.html", content = data)

@app.route("/beer_types")
def beer_types(): # Renders the beer_types page using the beer_styles data fetched from the api above.  Only passing the Data specific to the types of beer
    return rt("beer_types.html", content = beer_styles["data"])

@app.route("/about")
def about(): # renders the about us page
    return rt("about.html", user = "Nick Cessac")

# Only run when the file is executed direction, not when being imported as a module.  
if __name__ == "__main__": 
    app.run(debug=True)