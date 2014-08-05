import pandas as pd;import numpy as np
from pandas import Series,DataFrame
##df = pd.read_csv('ch06//csv_mindex.csv',index_col=['key1','key2'])
##result = pd.read_table('ch06//ex3.txt',sep='\s+')
##data = pd.read_csv('ch06//ex5.csv')
##chunker = pd.read_csv('ch06//ex6.csv',chunksize=1000)
##tot = Series([])
##for piece in chunker:
##    tot = tot.add(piece['key'].value_counts(),fill_value=0)
##tot = tot.order(ascending=False)
##dates = pd.date_range('1/1/2000',periods=7)
##ts = Series(np.arange(7),index=dates)
import csv
f = open('ch06//ex7.csv')
reader = csv.reader(f)
lines = list(reader)
header,values = lines[0],lines[1:]
data_dict = {h:v for h,v in zip(header,zip(*values))}
