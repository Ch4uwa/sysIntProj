import requests
import spotipy

# required information


class MyRequests:
    APIkeys = {"siteIdAPIkey": "994bc5defb6e45d9a657f8125bfabf0f",
               "realTimeAPIkey": "0c84a833b5744b83ab387e0be62ebeb6", "weatherApiKey": "ba3f2e8a9bb3db4c249970a998e1c38b"}
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
        buses = slReq.json()["ResponseData"]["Buses"][0]
        atHome = {
            "lineNumber": buses["LineNumber"],
            "destination": buses["Destination"],
            "stopArea": buses["StopAreaName"],
            "displayTime": buses["DisplayTime"]}

        return atHome

    def __init__(self, town="Tullinge"):
        self.town = town

    def weatherAPI(self):
        # Show the temperature and if rain from Openweather
        countryID = "swe"
        units = "metric"
        weatherURL = ("http://api.openweathermap.org/data/2.5/weather?q=" +
                      self.town + "," + countryID + "&APPID=" + APIkeys["weatherApiKey"] + "&units=" + units)
        r = requests.get(weatherURL)
        weather = r.json()
        return weather

    # show local time and maybe choose others
    def worldclockapi(self):
        clockUrl = "http://worldclockapi.com/api/json/cet/now?callback=mycallback"
        r = requests.get(clockUrl)
        return r.json()


# clock = WorldTimeReq()
# print(clock.worldclockapi().get("currentDateTime"))
# print(clock.worldclockapi().get("dayOfTheWeek"))
# print(clock.worldclockapi().get("timeZoneName"))

# ---------------------------------
