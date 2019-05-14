import requests

# required information


class MyRequests:
    # dict holding the api keys
    APIkeys = {"siteIdAPIkey": "",
               "realTimeAPIkey": "", "weatherApiKey": ""}

    def randNames(self):
        # fetching random names, limit=numbers of names
        data = requests.get('http://api.namnapi.se/v2/names.json?limit=1')
        d = data.json()
        return d


    def slRealTime(self):
        # Get the siteId of search word
        searchWord = "Gösta Frohms väg(Botkyrka)"
        slStationsOnly = "True"
        slMaxResults = "1"
        slUrl = ("https://api.sl.se/api2/typeahead.json?key=" +
                 self.APIkeys["siteIdAPIkey"] + "&searchstring=" + searchWord + "&stationsonly=" +
                 slStationsOnly + "&maxresults=" + slMaxResults)
        r = requests.get(slUrl)
        siteIdResp = r.json()["ResponseData"][0]["SiteId"]

        # get siteid from slSearchSiteID respons
        # set the timewindow to look within
        # Get departures of buses
        timeWindowMin = "60"
        realTimeURL = ("http://api.sl.se/api2/realtimedeparturesV4.json?key=" +
                       self.APIkeys["realTimeAPIkey"] + "&siteid=" + siteIdResp + "&timewindow=" + timeWindowMin)
        slReq = requests.get(realTimeURL)
        try:
            # if statement might not be needed
            if not slReq.json()["ResponseData"].get("Buses")[0]:
                return False
            else:
                buses = slReq.json()["ResponseData"].get("Buses")[0]
                atHome = {
                    "lineNumber": buses["LineNumber"],
                    "destination": buses["Destination"],
                    "stopArea": buses["StopAreaName"],
                    "displayTime": buses["DisplayTime"]}
                return atHome
        except:
            return False

    def weatherAPI(self):
        # Show the temperature and if rain from Openweather
        town = "Stockholm"
        countryID = "swe"
        units = "metric"
        weatherURL = ("http://api.openweathermap.org/data/2.5/weather?q=" +
                      town + "," + countryID + "&APPID=" + self.APIkeys["weatherApiKey"] + "&units=" + units)
        r = requests.get(weatherURL)
        weather = r.json()
        return weather

    def worldclockapi(self):
        # show local time and maybe choose others
        clockUrl = "http://worldclockapi.com/api/json/cet/now?callback=mycallback"
        r = requests.get(clockUrl)
        return r.json()

    def numbers(self):
        # get history from random year
        randNumURL = "http://numbersapi.com/random/year?json"
        r = requests.get(randNumURL)
        return r.json()

if __name__ == "__main__":
    MyRequests()
