# Airport-Locator
Given a region described by three or more latitude, longitude coordinates and a list of FAA public airport identifiers, this tool determines whether the airports are within the region.
## Use
To use as a console app, run <code>python interface.py</code> at the command line and follow the instructions there. To use in another Python file, include <code>from locator import locator</code>. To create a <code>locator</code> object, call the constructor with an argument <code>coords : list[list[float]]</code> that defines the unordered coordinates of the geographic region in question. The <code>locator</code> object saves this region as a state, which can be updated with a call to <code>update_coords()</code>. Check which airports are located within the region with a call to <code>check_locations()</code>, passing a list of FAA airport identifiers as an argument. This function returns a corresponding list of boolean values. If a given identifiers is not valid, a message will indicate so and the value returned with be <code>False</code>.
### locator.py
Defines a locator class with functions for checking if an airport is in a given region. Uses <code>locations.csv</code> to lookup airport locations by FAA public airport ID.
### scraper.py
A webscraper built with BeautifulSoup that scraped over 4,000 webpages on AirNav.com to retrieve location data for each public airport in the United States with the resulting data written to locations.csv. Requires an API Key for ScrapeOps proxy service to run. The scaper ran for several hours (artificial delay) with only 8 failed requests and 4,719 successful.
### test.py
Unit testing of <code>locator.py</code> and its functions.
### interface.py
Provides a basic user interface at the command line for interacting with the <code>locator.py</code> class.
### locations.csv
Data describing the location of every public airport in the United States as latitude, longitude pairs. Only two columns: 'ID', 'Coords'. Keep in same directory as <code>locator.py</code>.
