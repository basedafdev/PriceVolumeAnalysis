import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
def update_data(id: str, source='iex'):
    style.use('ggplot')
    start = dt.datetime(dt.datetime.today().date().year,1,1)
    end = dt.datetime(dt.datetime.today().date().year,dt.datetime.today().date().month,dt.datetime.today().date().day-1)
    df = web.DataReader(id,source,start,end)
    df.to_csv('download.csv')
    print(df)