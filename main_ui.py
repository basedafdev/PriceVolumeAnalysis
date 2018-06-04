import sys
import csv
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from load_files import generate_company_list
from PyQt5.QtWidgets import QApplication,QWidget, QMainWindow,QMessageBox, QPushButton, QLineEdit, QLabel, QVBoxLayout, QListWidget, QStatusBar

from directory import Directory
from company import Company
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
        self.listWidget.itemClicked.connect(self.ticket_pull_up)

        # connect button to function on_click
        self.button.clicked.connect(self.addtolist)








    def top_five(self,item):
        pass


    def ticket_pull_up(self,item):
        """
        Pul ls up ticket of information when clicked
        """
        temp_company = Company(str(item.text()))
        end_date = 20180529
        year = self.directory.get_zone(temp_company,20170531,end_date) #1 year
        sixmonth = self.directory.get_zone(temp_company,20180102,end_date) #6 months
        threemonth = self.directory.get_zone(temp_company,20180301,end_date) #3 months
        onemonth = self.directory.get_zone(temp_company,20180501,end_date) # 1 month
        fiveday = self.directory.get_zone(temp_company,20180521,end_date) # 5 days
        #### GENERATES ONE YEAR ####
        ticket_window = new_window(self)
        ticket_window.year = QLabel(ticket_window)
        ticket_window.setWindowTitle(str(temp_company))
        ticket_window.year.setText("1-YEAR: " + " || ZONE: " + str(year[1]) + " ||  CHANGE IN PRICE: " + \
                                       str(round(year[3], 4)) + " || CHANGE IN VOLUME: " + str(
            round(year[4], 4)) + "  RANK: " + str(round(year[2],7)))
        ticket_window.year.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        ticket_window.year.setGeometry(10,0,500,30)

        #### GENERATES SIX MONTH ####
        ticket_window.sixmonth = QLabel(ticket_window)
        ticket_window.sixmonth.setText("6-MONTHS: " + " || ZONE: " +str(sixmonth[1]) + " ||  CHANGE IN PRICE: " +\
                                       str(round(sixmonth[3],4)) + " || CHANGE IN VOLUME: " + str(round(sixmonth[4],4)))
        ticket_window.sixmonth.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        ticket_window.sixmonth.setGeometry(10,20,400,30)

        #### GENERATES THREEMONTH MONTH ####
        ticket_window.threemonth = QLabel(ticket_window)
        ticket_window.threemonth.setText("3-MONTHS: " + " || ZONE: " + str(threemonth[1]) + " ||  CHANGE IN PRICE: " + \
                                       str(round(threemonth[3], 4)) + " || CHANGE IN VOLUME: " + str(
            round(threemonth[4], 4)))
        ticket_window.threemonth.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        ticket_window.threemonth.setGeometry(10, 40, 400,30)

        #### ONE MONTH ####
        ticket_window.onemonth = QLabel(ticket_window)
        ticket_window.onemonth.setText("1-MONTHS: " + " || ZONE: " + str(onemonth[1]) + " ||  CHANGE IN PRICE: " + \
                                         str(round(onemonth[3], 4)) + " || CHANGE IN VOLUME: " + str(
            round(onemonth[4], 4)))
        ticket_window.onemonth.setGeometry(10, 60, 400,30)
        ticket_window.onemonth.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        #### FIVE DAY ####
        ticket_window.fiveday = QLabel(ticket_window)
        ticket_window.onemonth.setText("5-DAY:    " + " || ZONE: " + str(fiveday[1]) + " ||  CHANGE IN PRICE: " + \
                                       str(round(fiveday[3], 4)) + " || CHANGE IN VOLUME: " + str(
            round(fiveday[4], 4)))
        ticket_window.fiveday.setGeometry(10, 80,400,30)
        ticket_window.fiveday.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        ticket_window.setGeometry(0,0,600,100)
        ticket_window.show()

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

class new_window(QMainWindow):
    def __init__(self, parent=None):
        super(new_window, self).__init__(parent)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(App.exec())
