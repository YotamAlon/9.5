import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MainWindow(GridLayout):
    def __init__(self):
        super(MainWindow, self).__init__(self)


class Facebook2listApp(App):
    def build(self):
        return MainWindow()