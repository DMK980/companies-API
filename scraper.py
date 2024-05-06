from bs4 import BeautifulSoup;
from urllib.request import urlopen;
import pandas as pd;
import json

# getting data from the UK website

with urlopen("https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers") as response:
    website = response.read()

soup = BeautifulSoup(website,"html.parser")
csv_link = soup.find(id="documents").a["href"]

# reading data
data = pd.read_csv(csv_link)
data_str = data.to_json(orient="index")
data_json = json.loads(data_str)