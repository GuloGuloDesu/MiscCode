import pandas_datareader.data as web
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 1, 1)

#Google and Yahoo are dreprecated, use iex
facebook = web.DataReader('DUST', 'iex', start, end)

print(facebook.head())
