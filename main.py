from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

from requestAPI import MyRequests
from gCal import gCalMain


class MainWindow(Screen):
    sltime = ObjectProperty(None)
    gCal = ObjectProperty(None)
    w_weather = ObjectProperty(None)
    clock = ObjectProperty(None)
    names = ObjectProperty(None)
    yearTrivia = ObjectProperty(None)

    def getClock(self):
        time = MyRequests().worldclockapi()
        t = time["currentDateTime"]
        _time = t.replace("T", " ")
        _time = _time.replace("+02:00", "")

        self.clock.text = time["dayOfTheWeek"] + " " + _time

    def getWeather(self):
        weathers = MyRequests().weatherAPI()
        if not weathers:
            self.w_weather.text = "Nothing to find"
        else:
            self.w_weather.text = ("Location: " + str(weathers["name"]) +
                                   "\nWeather: " + weathers["weather"][0].get("description") +
                                   "\nTemperature: " + str(weathers["main"].get("temp")) + "C" +
                                   "\nHumidity: " + str(weathers["main"].get("humidity")) + "%" +
                                   "\nMax: " + str(weathers["main"].get("temp_max")) + "C" +
                                   "\nMin: " + str(weathers["main"].get("temp_min")) + "C")

    def getSL(self):
        sl = MyRequests().slRealTime()
        if not sl:
            self.sltime.text = "Nothing to find"
        else:
            self.sltime.text = ("Bus: " + sl.get("lineNumber") +
                                "\nDeparts From: " + sl.get("stopArea") +
                                "\n" + sl.get("displayTime") +
                                "\nDestination: " + sl.get("destination"))

    def getCal(self):
        cal = gCalMain()
        if not cal:
            self.gCal.text = "Nothing to find"
        else:
            startTime = str(cal[0]["start"].get("dateTime"))
            endTime = str(cal[0]["end"].get("dateTime"))
            startTime = startTime.replace("T", " ")
            startTime = startTime.replace("Z", " +02:00")
            endTime = endTime.replace("T", " ")
            endTime = endTime.replace("Z", " +02:00")
            self.gCal.text = (startTime + "\n" +
                              str(cal[0].get("summary")) + " " +
                              str(cal[0].get("location")) + "\n" +
                              endTime)

    def getNames(self):
        n = MyRequests().randNames()
        self.names.text = n["names"][0].get(
            "gender") + " " + n["names"][0].get(
            "firstname") + " " + n["names"][0].get("surname")

    def randNumbs(self):
        r = MyRequests().numbers()
        self.yearTrivia.text = str(r["text"])

    def on_enter(self, *args):
        self.randNumbs()
        self.getNames()
        self.getWeather()
        self.getSL()
        self.getCal()
        self.getClock()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("style.kv")
sm = WindowManager()


screens = [MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)


class MyApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    MyApp().run()
