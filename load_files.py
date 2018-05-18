import datetime as dt
import pandas_datareader.data as web

def update_data(id: str, source='iex'):
<<<<<<< HEAD
=======
    """
    Update the company_library with given Company:ID
    If source parameter is empty, source will default to iex
    """

>>>>>>> e489e86a41382a0274fd8800f1790635eeeea7a5
    start = dt.datetime(dt.datetime.today().date().year,1,1)
    end = dt.datetime(dt.datetime.today().date().year,dt.datetime.today().date().month,dt.datetime.today().date().day-1)
    df = web.DataReader(id,source,start,end)
    temp = 'company_library/' + id + ".csv"
    df.to_csv(temp)
    print(df)

if __name__ == "__main__":
    """
    Testing the code
    """
    update_data("GOOG")
    update_data("TSLA")
<<<<<<< HEAD
    update_data("IBM")
=======
    update_data("GE")
>>>>>>> e489e86a41382a0274fd8800f1790635eeeea7a5
