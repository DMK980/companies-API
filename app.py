from flask import Flask
import scraper

# setting app flask backend
app = Flask(__name__)

# route for companies list
@app.route("/",methods={"GET"})
def companies_list():
    return scraper.data_json["0"]

if __name__ == "__main__":
    app.run(debug=True)