import requests
from bs4 import BeautifulSoup
import json

url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"

resp = requests.get(url)
soup = BeautifulSoup(resp.content, "html.parser")
soup = soup.find('table', id = "search_results_table")

year_eid = []
for tr in soup.find_all("tr"):
    trid = tr.get("id")
    if trid is not None:
        trid = trid.replace("election-id-", "")
        year = tr.find("td", attrs = {'class' : "year first"}).text
        year_eid.append([year, trid])
f = open("ELECTION_ID","w")
json.dump(year_eid,f)
f.close()
