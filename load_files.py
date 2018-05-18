import datetime as dt
import pandas_datareader.data as web

def update_data(id: str, source='iex'):
    start = dt.datetime(dt.datetime.today().date().year,1,1)
    end = dt.datetime(dt.datetime.today().date().year,dt.datetime.today().date().month,dt.datetime.today().date().day-1)
    df = web.DataReader(id,source,start,end)
    temp = 'company_library/' + id + ".csv"
    df.to_csv(temp)
    print(df)
if __name__ == "__main__":
    update_data("GOOG")
    update_data("TSLA")
    update_data("IBM")