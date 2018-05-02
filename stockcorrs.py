#Given n stocks, time period and a measure, calculate the correlation network and plot the graph associated with it


import pandas as pd
import pandas_datareader as web

class Stock_Correlations(object):

    def __init__(self, num_stocks, symb, tp, measure):
        self.num_stocks = num_stocks
        self.symb = symb
        self.tp = tp
        self.measure = measure

    def get_data(self):
        
