from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<p>Hello, 362 World!</p>"

@app.route("/breweries")
def breweries():
    return "<p>Welcome to Breweries!</p>"

@app.route("/beer_types")
def bear_types():
    return "<p>Welcome to Beer types!</p>"

@app.route("/about")
def about():
    return "<p>Welcome to About Us!</p>"

if __name__ == "__main__":
    app.run(debug=True)