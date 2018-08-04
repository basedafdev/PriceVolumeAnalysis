# Price-Volume Equity Scanner
**Equity analysis tool that forecasts price reversals**
Thomas Liu

Breakdown:

1.  company_library
    * directory of all the top companies and its historical data. In .csv format
2.  icon_library
    * directory of the icons for main_ui.py
3. company.py
    * CLASS: Represents a company. Has attributes like historical dates, volumes, and prices.
4. directory.py
    * CLASS: Represents a directory of companies. Has attributes;
5. load_files.py
    * METHODS: Updates, generates, and populates the company_library
6. main_ui.py
    * User interface
    ****
    
Make sure python 3.6 or greater is installed.


Depedencies that need to be installed:

    pip install pandas
    pip install pandas_datareader
    pip install Kivy
    pip install KivyCalender
    pip install Kivy-Garden
    
Steps To Running the Application:

1) Run load_files.py     (this will update all the .csv files in the company_library)


2) Run directory.py or main_ui.py


If you want just want to see the stocks itself without the User Interface, run directory.py.
To do Date input just input the date in this format:

   yearmonthday

   example: 20180724 
   this equates to 07/24/2018


If you want to skip all of this work, just shoot me an email with your email address and I'll try send over a top 100
list of stocks everyday




If you have any issues, concerns, or bugs shoot me a message at toms.liu@mail.utoronto.ca


Happy Investing!
