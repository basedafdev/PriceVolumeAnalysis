import datetime as dt
import pandas_datareader.data as web
import csv
def update_data(id: str, source='iex'):
    """
    Update the company_library with given Company:ID
    If source parameter is empty, source will default to iex
    """

    start = dt.datetime(dt.datetime.today().date().year,1,1)
    end = dt.datetime(dt.datetime.today().date().year,dt.datetime.today().date().month,dt.datetime.today().date().day-1)
    df = web.DataReader(id,source,start,end)
    temp = 'company_library/' + id + ".csv"
    df.to_csv(temp)

def generate_company_library():
    path = 'companylist.csv'
    companyids = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            companyids.append(line[0])
    companyids.pop(0)
    print(companyids)
    for id in companyids:

        try:
            update_data(id)
        except:
            pass


if __name__ == "__main__":
    """
    Testing the code
    """
    generate_company_library()