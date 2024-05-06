from flask import Flask;
from flask.helpers import send_from_directory
from bs4 import BeautifulSoup;
from urllib.request import urlopen;
import pandas as pd;
import json
from flask_cors import CORS, cross_origin

# setting app flask backend
app = Flask(__name__, static_folder="visa_search/build")
CORS(app)

# route for companies list
@app.route("/companies_list",methods={"GET"})
@cross_origin()
def companies_list():
    # getting data from the UK website
    website = urlopen("https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers").read()
    soup = BeautifulSoup(website,"html.parser")
    csv_link = soup.find(id="documents").a["href"]

    # reading data
    data = pd.read_csv(csv_link)
    data_str = data.to_json(orient="index")
    data_json = json.loads(data_str)
    return data_json 

@app.route("/")
@cross_origin()
def serve():
    return send_from_directory(app.static_folder,"index.html")

if __name__ == "__main__":
    app.run(debug=True)