# Airport-Locator
Check for airports in given locations
## locator.py
Defines a locator class with functions for checking if an airport is in a given region. Uses locations.csv to lookup airport locations by FAA public airport ID.
### Use

## scraper.py
A webscraper built with BeautifulSoup that scraped over 4,000 webpages on AirNav.com to retrieve location data for each public airport in the United States with the resulting data written to locations.csv. Requires an API Key for ScrapeOps proxy service to run. The scaper ran for several hours (artificial delay) with only 8 failed requests and 4,719 successful.
## test.py
Unit testing of the locator class and its functions.
## locations.csv
Data describing the location of every public airport in the United States as latitude, longitude pairs. Only two columns: 'ID', 'Coords'.
