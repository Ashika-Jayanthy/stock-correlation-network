#Given n stocks, time period and a variable and distance measure, calculate the correlation network and plot the graph associated with it


import pandas as pd
import pandas_datareader as web
import datetime

class Stock_Correlations(object):

    def __init__(self, symb, time_start, time_end, variable, measure):

        self.symb = symb
        self.time_start = pd.to_datetime(time_start)
        self.time_end = pd.to_datetime(time_end)
        self.variable = str(variable)
        self.measure = str(measure)

    def get_data(self):
        #Get all data associated with input stocks
        data_arrays = {}
        for stock in self.symb:
            stock_data = web.DataReader(stock, "quandl", start,end)
            stock_data.index.name = 'Date'
            stock_data.reset_index(inplace=True)
            pd.to_datetime(stock_data['Date'])
            data_arrays[stock] = stock_data
            return

    def filter_data(self):
        #Filter data by time period and variable of interest


    def correlation_matrix(self):
        #Create correlation matrix for stocks

    def measure_distance(self):
        #Calculate pairwise distance between stocks

    def visualize_network(self):
        #Visualize the network of stocks
