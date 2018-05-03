#Given n stocks, time period and a variable and distance measure, calculate the correlation network and plot the graph associated with it


import pandas as pd
import pandas_datareader as web
import datetime
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


class Stock_Correlations(object):

    def __init__(self, symb, time_start, time_end, variable, measure, threshold):

        self.symb = symb
        self.time_start = pd.to_datetime(time_start)
        self.time_end = pd.to_datetime(time_end)
        self.variable = str(variable)
        self.measure = str(measure)
        self.threshold = float(threshold)

    def get_data(self):
        #Get data associated with input stocks for variable in time period
        data_arrays = {}
        for stock in self.symb:
            stock_data = web.DataReader(stock, "iex", self.time_start,self.time_end)
            data_arrays[stock] = stock_data[self.variable]
        df = pd.DataFrame(data_arrays)
        return df

    def correlation_matrix(self,df):
        #Create correlation matrix for stocks

        cor = df.corr(method='spearman')
        return cor

    def create_graph(self, cor):
        #Create graph using correlation matrix

        stacks = cor.stack().reset_index()
        stacks.columns = ['s1','s2','corr']
        stacks = stacks.loc[(stacks['corr'] > self.threshold) & (stacks['s1'] != stacks['s2'])]
        g = nx.from_pandas_edgelist(stacks, 's1','s2')
        nx.draw(g, with_labels = True, node_color='blue', node_size=400, edge_color='black', linewidths=1, font_size=12)
        plt.show()
        return stacks

    def minimum_spanning_tree(self):
        #Create minimum spanning tree using graph
        return
#test

with open("stockslist.txt", 'r') as s:
    p = s.readlines()
arr = p[0].split('\r')


start = '2017-05-04'
end = '2017-06-04'
var = 'volume'
mes = 10
t=0.2
k = Stock_Correlations(arr,start,end,var,mes,t)
q = k.get_data()
m = k.correlation_matrix(q)
n = k.create_graph(m)
print n
