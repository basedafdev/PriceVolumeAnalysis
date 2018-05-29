import sys
import csv
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from load_files import generate_company_list
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox, QPushButton, QLineEdit, QLabel, QVBoxLayout, QListWidget, QStatusBar
from directory import Directory
class MainWindow(QMainWindow):
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
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
    def initUI(self):
        #Initialization of User interface

        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y, self.width, self.height)
        #create textbox
        self.initwatchlist()

        self.show()
    def quit(self):
        pass

    def initwatchlist(self):
        #Block for adding things into a watch list

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 25)
        self.textbox.resize(100, 20)

        self.lbl = QLabel(self)
        self.lbl.move(35, 0)
        self.lbl.setText("Watchlist")
        # create button
        self.button = QPushButton('Add', self)
        self.button.move(20, 50)

        self.box = QLabel(self)
        self.box.setGeometry(0,200,400,400)
        self.listWidget = QListWidget(self)

        self.listWidget.setGeometry(20,90,50,200)

        # connect button to function on_click
        self.button.clicked.connect(self.addtolist)
















    def addtolist(self):
        """
        THIS IS A EVENT FUNCTION FOR ADDING COMPANIES INTO A WATCHLIST

        """
        textboxValue = self.textbox.text()

        if textboxValue.upper() in self.directory.companystrings and textboxValue.upper() not in self.watchlist:
            self.watchlist.append(textboxValue.upper())
            self.listWidget.addItem(textboxValue.upper())
            self.statusBar.showMessage(textboxValue.upper()+ " has been added to your watchlist", 2000)

        elif textboxValue.upper() not in self.directory.companystrings:
            self.statusBar.showMessage("Invalid company id", 2000)
        elif textboxValue.upper() in self.watchlist:
            self.statusBar.showMessage(textboxValue.upper() + " is already in your watchlist", 2000 )

        self.textbox.setText("")



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())
