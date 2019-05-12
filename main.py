from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

import requestAPI


class MainWindow(Screen):
    sldestination = ObjectProperty(None)
    sltime = ObjectProperty(None)

    def on_enter(self, *args):
        sl = requestAPI.MyRequests()
        sldict = sl.slRealTime()
        self.sldestination.text = "Destination: " + sldict.get("destination")
        self.slLineNumber.text = "Bus: " + sldict.get("lineNumber")
        self.slStop.text = "From: " + sldict.get("stopArea")
        self.sltime.text = "Time to departure: " + sldict.get("displayTime")


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
