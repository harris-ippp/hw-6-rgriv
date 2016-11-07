import requests
from bs4 import BeautifulSoup
import json

base_url = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

with open("ELECTION_ID") as f:
    yeid = json.load(f)

for year, eid in yeid:
    resp = requests.get(url)
    file_name = year + ".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
