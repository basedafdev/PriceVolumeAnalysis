import sys
import csv
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from load_files import generate_company_list
from PyQt5.QtWidgets import QApplication, QSlider, QWidget, QMainWindow,QMessageBox, QPushButton, QLineEdit, QLabel, QVBoxLayout, QListWidget, QStatusBar

from directory import Directory
from company import Company
class Parameter_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.directory = Directory()
        self.title = "Price Volume Analysis"
        self.x = 100
        self.y = 100
        self.width = 900
        self.height = 500
        self.watchlist = []
        self.initUI()

    def initUI(self):
        #Initialization of User interface

        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y, self.width, self.height)
        self.price_percent_display = QLineEdit()
        self.max_price_display = QLineEdit()
        self.max_volume_display = QLineEdit()
        #Slider for max_price_change
        self.max_price_change = QSlider(Qt.Horizontal)
        self.max_price_change.setMaximum(100)
        self.max_price_change.setMinimum(0)
        self.max_price_change.setTickInterval(1)
        self.max_price_change.setValue(0)
        self.max_price_change.setTickPosition(QSlider.TicksBelow)
        self.max_price_change.valueChanged.connect(self.v_change1)
        #Slider for Max Price
        self.max_price = QSlider(Qt.Horizontal)
        self.max_price.setMaximum(2000)
        self.max_price.setMinimum(2)
        self.max_price.setTickInterval(1)
        self.max_price.setTickInterval(QSlider.TicksBelow)
        self.max_price.valueChanged.connect(self.v_change2)
        #Slider for the Max_Volume
        self.max_volume = QSlider(Qt.Horizontal)
        self.max_volume.setMaximum(1000000)
        self.max_volume.setMinimum(100)
        self.max_volume.setTickInterval(1)
        self.max_volume.setTickInterval(QSlider.TicksBelow)
        self.max_volume.valueChanged.connect(self.v_change3)
        #Slider for the Number of Trading days
        vbox = QVBoxLayout()
        vbox.addWidget(self.max_price_change)
        vbox.addWidget(self.price_percent_display)
        vbox.addWidget(self.max_price)
        vbox.addWidget(self.max_price_display)
        vbox.addWidget(self.max_volume)
        vbox.addWidget(self.max_volume_display)
        self.setLayout(vbox)
        self.show()

    def v_change1(self):
        my_value = str(self.max_price_change.value()) + "% Maximum Price Change"
        self.price_percent_display.setText(my_value)
        self.displaytop()
    def v_change2(self):
        my_value = "$" + str(self.max_price.value()) +" Maximum Price"
        self.max_price_display.setText(my_value)
        self.displaytop()
    def v_change3(self):
        my_value = str(self.max_volume.value()) + " Minimum Volume"
        self.max_volume_display.setText(my_value)
        self.displaytop()
    def displaytop(self):
        s = ""

        out = self.directory.get_reversals_up_ui(self.max_price_change.value()/100, self.max_price.value(), self.max_volume.value(),0)
        for i in range(len(out[0])):
            s += str(5 - i) + ") " + str(out[0][i]) + " " + str(out[1][i]) + '\n'
        print(s)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Parameter_Widget()
    sys.exit(App.exec())
