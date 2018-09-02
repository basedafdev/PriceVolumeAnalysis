import kivy
import math
from browser import MainWindow
import webbrowser
import sys
from decimal import Decimal
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from kivy.uix.dropdown import DropDown
from directory import selectionSort
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Label, Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from kivy.uix.popup import Popup
from KivyCalendar import CalendarWidget, DatePicker
from directory import Directory

Config.set('graphics','width',800)
Config.set('graphics','height',800)

millnames = ['', ' Thousand', ' Million', ' Billion', ' Trillion']
def convert_string_to_date(date: str):


    date_list = date.split(".")

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
        self.date = 0
        self.directory = Directory()
        self.dog = self.directory.get_reversals_up(0)[0]
        print("Initialized")
        return "Sort by Price Deviation"
    def calculate(self, calculation):

        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
    def top_ten(self, id):

        b = int(id)*-1
        if  not hasattr(self, "dog"):
            self.dog = ["","","","","","","","","","","",""]
        return str(self.dog[b])

    def set_date(self, id):
        self.date = convert_string_to_date(id.text)

        self.dog = self.directory.get_reversals_up(self.date)[0]


    def pull_up_ticker(self, id):
        webbrowser.open('http://stockcharts.com/h-sc/ui?s=' + id.text,  new=2)
        pass
    def call_back(self,id):
        self.get_info(id)
    def sort_by_price_low_to_high(self):
        """ Sort the stocks by low to high Price Change
        """

        self.sort_by_price_high_to_low()
        self.dog = self.dog[::-1]

    def sort_by_price_high_to_low(self):
        """Sort the stocks by high to low Price Change
        """

        temp = self.directory.get_reversals_up(self.date)
        selectionSort(temp[1], temp[0],1)
        self.dog = temp[0]

    def sort_by_volume_low_to_high(self):
        """ Sort the stocks by low to high Volume deviation
        """

        self.sort_by_volume_high_to_low()
        self.dog = self.dog[::-1]

    def sort_by_volume_high_to_low(self):
        """ Sort the stocks by high to low Volume deviation
        """

        self.dog = self.directory.get_reversals_up(self.date)[0]
        for i in self.dog:
            print(i)
    def call_back2(self,id):
        webbrowser.open('http://stockcharts.com/h-sc/ui?s=' + id.stock_id)
    def get_info(self, id):
        """
        Gets the info Dialog for each Stock
        :param id:
        :return:
        """
        dialog = ""
        company = None

        for i in self.dog:
            if str(i).upper() == id.text.upper():
                company = i

        daybefore = None
        price_change = None
        volume_deviation = None
        price_change = None
        if company is not None:
            if self.date not in company.dates:
                daybefore = len(company.dates)-1
            else:
                daybefore = company.dates.index(self.date)-1
            price_change = company.get_change_in_price(company.dates[daybefore], company.dates[daybefore])
            historical_volume = company.getavg(company.dates[daybefore - 20], company.dates[daybefore - 1], "VOLUME")
            today_volume = company.volumes[daybefore]

            volume_deviation = today_volume/historical_volume
            dialog += "Company Name: " + str(company.company_name) + "\n" + "\n"
            dialog += "Market-Cap: " + str(millify(company.market_cap)) + "\n"
            dialog += "Sector: " + str(company.sector) + "\n"
            dialog += "Description: " + str(company.description) + '\n'
            dialog += "Price Change: " + str(round(price_change*100,2)) + "%" + "\n"
            dialog += "Volume Deviation: " + str(round(volume_deviation,2)) + "\n"

            new_label = Label(text=dialog)
            new_label.font_size = 15
            new_label.color = 1,1,1,1

            popup = Popup(title=id.text,
                          content=new_label,
                          size_hint=(None, None), size=(600, 400))
            popup.open()
        else:
            pass

    def full_list(self):

        layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(1,len(self.dog)+1):
            btn1 = Button(text=str(self.dog[-1*i]),size_hint_y=None, height=40)
            btn1.bind(on_press=self.call_back)

            layout.add_widget(btn1)

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        popup = Popup(title="Other Stocks", content=root,
                      size_hint=(None,None),
                      size= (600,800))
        popup.open()
class PriceVolumeAnalysisApp(App):

    def build(self):
        return CalcGridLayout()

def millify(n):
    n = float(n)
    millidx = max(0, min(len(millnames) - 1,
                            int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

    return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])
if __name__ == "__main__":
    calcApp = PriceVolumeAnalysisApp()
    calcApp.run()
