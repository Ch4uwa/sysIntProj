import requests
import spotipy

# required information


class MyRequests:
    APIkeys = {"siteIdAPIkey": "994bc5defb6e45d9a657f8125bfabf0f",
               "realTimeAPIkey": "0c84a833b5744b83ab387e0be62ebeb6", "weatherApiKey": "ba3f2e8a9bb3db4c249970a998e1c38b"}

    def randNames(self):
        data = requests.get('http://api.namnapi.se/v2/names.json?limit=1')
        d = data.json()
        return d

# Show time of departure SL

    def slRealTime(self):
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
        timeWindowMin = "60"
        # set the args together
        realTimeURL = ("http://api.sl.se/api2/realtimedeparturesV4.json?key=" +
                       self.APIkeys["realTimeAPIkey"] + "&siteid=" + siteIdResp + "&timewindow=" + timeWindowMin)
        slReq = requests.get(realTimeURL)
        try:
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

    # show local time and maybe choose others
    def worldclockapi(self):
        clockUrl = "http://worldclockapi.com/api/json/cet/now?callback=mycallback"
        r = requests.get(clockUrl)
        return r.json()

    def numbers(self):
        randNumURL = "http://numbersapi.com/random/year?json"
        r = requests.get(randNumURL)
        return r.json()

if __name__ == "__main__":
    MyRequests()
