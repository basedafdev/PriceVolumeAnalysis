import datetime as dt
import pandas_datareader.data as web
import csv

def update_data(id: str, source='robinhood'):
    """
    Update the company_library with given Company:ID
    If source parameter is empty, source will default to iex
    """

    start = dt.datetime(2017,3,2)
    end = dt.datetime(dt.datetime.today().date().year,dt.datetime.today().date().month,dt.datetime.today().date().day-1)
    df = web.DataReader(id,source,start,end)
    temp = 'company_library/' + id + ".csv"
    df.to_csv(temp)

def generate_company_list():
    """
    Return a list of all public companies
    :return a list
    """
    path = 'companylist.csv'
    companyids = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            companyids.append(line[0])
    companyids.pop(0)
    return companyids

def generate_company_library():
    """
    Takes all public companies and generates .csv file
    """

    companyids = generate_company_list()
    counter = 3300
    companyids = companyids[counter:]

    for id in companyids:
        print(counter,"generating", id + ".csv")
        try:
            update_data(id)
        except:
            pass
        counter += 1

if __name__ == "__main__":
    """
    Updates Company library
    """
    generate_company_library()

