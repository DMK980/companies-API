from flask import Flask
import pandas as pd
import json

# setting app flask backend
app = Flask(__name__)

# route for companies list
@app.route("/",methods={"GET"})
def companies_list():
    data = pd.read_csv("2024-05-10_-_Worker_and_Temporary_Worker.csv")
    data_str = data.to_json(orient="index")
    data_json = json.loads(data_str)

    return data_json

if __name__ == "__main__":
    app.run(debug=True)