import kivy


import webbrowser
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.floatlayout import  FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from KivyCalendar import CalendarWidget, DatePicker
from directory import Directory

Config.set('graphics','width',800)
Config.set('graphics','height',800)


def convert_string_to_date(date: str):


    date_list = date.split(".")
    print(date_list)
    new_list = []
    new_list.append(date_list[2])
    if len(date_list[1]) == 1:
        new_list.append("0" + date_list[1])
    else:
        new_list.append(date_list[1])
    if len(date_list[0]) == 1:
        new_list.append("0" + date_list[0])
    else:
        new_list.append(date_list[0])

    new_date = int(str(new_list[0]+new_list[1]+new_list[2]))

    return new_date
class CalcGridLayout(GridLayout):

    def fake_init(self):
        self.directory = Directory()
        self.dog = self.directory.get_reversals_up(0)[0]
        print("Initialized")
        return "Sort by Price Deviation"
    def calculate(self, calculation):
        print("CLICKED")
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
    def top_ten(self, id):

        b = int(id)
        if  not hasattr(self, "dog"):
            self.dog = ["","","","","","","","","","","",""]
        return str(self.dog[b])

    def set_date(self, id):

        date = convert_string_to_date(id.text)
        print(date)
        self.dog = self.directory.get_reversals_up(date)[0]

    def pull_up_ticker(self, id):
        webbrowser.open("http://stockcharts.com/h-sc/ui?s="+id.text)

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

if __name__ == "__main__":
    calcApp = CalculatorApp()
    calcApp.run()