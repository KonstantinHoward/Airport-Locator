import os
import csv
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import sys
import random

client = requests.session()
# optionally generate fake user-agents for requests with ua.getRandom["useragent"]
# ua = UserAgent()

# url to access scrapeops proxy API
proxy = "https://proxy.scrapeops.io/v1/"
# add personal API key here
API_key = ""

# load main page containing links for each state
req = requests.get(url=proxy, params={
    "api_key" : API_key,
    "url" : "https://www.airnav.com/airports/us"})
if req.status_code != 200 :
    sys.exit("Fail on main page"+ str(req.status_code))

try:                                                                                  
    root_html = BeautifulSoup(req.content, "html.parser")
except bs4.FeatureNotFound as err:
    sys.exit("BS fail on main page"+ err)
    

# get links to state pages
state_links = []
for state in root_html.find_all("a", class_="wl") :
    state_links.append("https://www.airnav.com"+ state.get("href"))

print("Scraped " + str(len(state_links)) + " states")


suc = 0
fails = {}
# write to csv as you go
with open("locations.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["ID", "Coords"])

    for state_link in state_links :
        # load state page 
        req = client.get(proxy, params={"api_key":API_key,
                        "url": state_link})
        if req.status_code != 200 :
            sys.exit("Fail on state page"+ str(req.status_code) + state_link)
    
        try:                                                                                  
            state_html = BeautifulSoup(req.content, "html.parser")
        except bs4.FeatureNotFound as err:
            sys.exit("BS fail on state page"+ err + state_link)

        
        # get links to state's airport pages
        airports = state_html.find("center").find("table").find_all("a")
        print(state_link)

        # retrieve coords on each airport page and write to csv
        for airport in airports :
            # introduce random delay to be respectful
            time.sleep(random.randint(4,10))
            id = airport.text.strip()
            
            req = client.get(proxy, params={"api_key":API_key,
                        "url": "https://www.airnav.com/airport/"+id})
            # if request fails, save id and continue
            if req.status_code != 200 :
                print(id + " failed with " + str(req.status_code))
                fails[id] = req.status_code
                continue
            
            
            try:
                airport_html = BeautifulSoup(req.content, "html.parser")
            except bs4.FeatureNotFound as err:
                print(f'An error occurred while parsing the HTML: {err} for ' + id)
                fails[id] = -1
                continue

            # parse and clean text
            td_element = airport_html.find("body").select("table:nth-child(4)")[1].select("tr:nth-child(2)")[0]

            
            coords = [x for x in td_element.contents[1] if getattr(x, 'name', None) != 'br'][2].split(",")
            csv_writer.writerow([id, coords])
            csvfile.flush()
            suc += 1

print(f"Finished with {suc} successful requests and {len(fails)} failures.")
print(fails)