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
    
If you want just want to see the stocks itself without the User Interface, run directory.py.
And for input just input the date in this format:
yearmonthday

example: 20180724 
this equates to 07/24/2018


Happy Investing!
