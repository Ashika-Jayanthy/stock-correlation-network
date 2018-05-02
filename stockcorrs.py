#Given n stocks, time period and a variable and distance measure, calculate the correlation network and plot the graph associated with it


import pandas as pd
import pandas_datareader as web
import datetime
import numpy as np

class Stock_Correlations(object):

    def __init__(self, symb, time_start, time_end, variable, measure):

        self.symb = symb
        self.time_start = pd.to_datetime(time_start)
        self.time_end = pd.to_datetime(time_end)
        self.variable = str(variable)
        self.measure = str(measure)

    def get_data(self):
        #Get data associated with input stocks for variable in time period
        data_arrays = {}
        for stock in self.symb:
            stock_data = web.DataReader(stock, "quandl", self.time_start,self.time_end)
            data_arrays[stock] = stock_data[self.variable]
        df = pd.DataFrame(data_arrays)
        return df

    def correlation_matrix(self):
        #Create correlation matrix for stocks
        return

    def measure_distance(self):
        #Calculate pairwise distance between stocks
        return

    def visualize_network(self):
        #Visualize the network of stocks
        return
#test
sym = ['LCNB', 'GEF']
start = '2017-05-04'
end = '2017-06-04'
var = 'Volume'
mes = 10

k = Stock_Correlations(sym,start,end,var,mes)
q = k.get_data()
print q
