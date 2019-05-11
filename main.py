from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class MainWindow(TabbedPanel):
    pass


kv = Builder.load_file("style.kv")


class MyApp(App):
    def build(self):
        return MainWindow()


if __name__ == '__main__':
    MyApp().run()
