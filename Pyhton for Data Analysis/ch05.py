from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import pandas.io.data as web
from numpy import nan as NA
##obj = Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
##sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
##obj3 = Series(sdata)
##states = ['California','Ohio','Oregon','Texas']
##obj4 = Series(sdata,index=states)
##obj4.name='population'
##obj4.index.name='state'
###obj.index=['Bob','Steve','Jeff','Ryan']
##
##data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
##         'year':[2000,2001,2002,2001,2002],
##         'pop':[1.5,1.7,3.6,2.4,2.9]}
##frame = DataFrame(data)
##frame2=DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three',
##                                                            'four','five'])
##val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
##frame2['debt']=val
##frame2['eastern'] = (frame2.state =='Ohio')
##pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,
##                                          2002:3.6}}
##frame3=DataFrame(pop)
##pdata = {'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}
###obj=Series(range(3),index=['a','b','c'])
##index = obj.index
##index = pd.Index(np.arange(3))
##obj2 = Series([1.5,-2.5,0],index=index)
##frame3.columns.name ='state'
##frame3.index.name ='year'
##obj2 = obj.reindex(['a','b','c','d','e'])
##obj3 = Series(['blue','purple','yellow'],index=[0,2,4])
######################################################################
##frame = DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],
##                  columns=['Ohio','Texas','California'])
##frame2 = frame.reindex(['a','b','c','d'])
##states = ['Texas','Utah','California']
##obj = Series(np.arange(4),index=['a','b','c','d'])
##new_obj = obj.drop('c')
##data = DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah',
##                                                     'New York'],columns=['one',
##                                                                         'two','three',
##                                                                         'four'])
##s1 = Series([7.3,-2.5,-3.4,1.5],index=['a','c','d','e'])
##s2 = Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
##df1 = DataFrame(np.arange(9).reshape((3,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado'])
##frame = DataFrame(np.arange(12).reshape((4,3)),columns=list('bde'),
##                index=['Utah','Ohio','Texas','Oregon'])
##df1 = DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
##df2 = DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
##arr = np.arange(12).reshape(3,4)
##frame = DataFrame(np.random.randn(4,3),columns=list('bde'),
##                  index=['Utah','Ohio','Texas','Oregon'])
##f = lambda x: x.max() - x.min()
##obj = Series(np.arange(4),index=['d','a','b','c'])
##frame = DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],
##                  columns=['d','a','b','c'])
##obj = Series([4,np.nan,7,np.nan,-3,2])
##frame = DataFrame({'b':[4,7,-3,2],'a':[0,1,0,-1]})
##obj = Series([7,-5,7,4,2,0,4])
##obj = Series(np.arange(5),index=['a','a','b','b','c'])
##df = DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
##df = DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-0.13]],index=['a','b','c','d'],columns=['one','two'])
##obj = Series(['a','b','c','d']*4)
############################################################################
##all_data = {}
##for tricker in ['AAPL','IBM','MSFT']:
##    all_data[tricker] = web.get_data_yahoo(tricker,'1/1/2000','1/1/2010')
####all_data['AAPL'] = web.get_data_yahoo('AAPL','1/1/2000','1/1/2010')
####all_data['IBM'] = web.get_data_yahoo('IBM','1/1/2000','1/1/2010')
####all_data['MSFT'] = web.get_data_yahoo('MSFT','1/1/2000','1/1/2010')
#####all_data['GOOG'] = web.get_data_yahoo('GOOG','1/1/2000','1/1/2010')
##price = DataFrame({tic:data['Adj Close'] for tic,data in all_data.items()})
##volume = DataFrame({tic:data['Volume'] for tic,data in all_data.items()})
##returns = price.pct_change()
############################################################################
obj = Series(['c','a','d','a','a','b','b','c','c'])
uniques = obj.unique()
mask = obj.isin(['b','c'])
data = DataFrame({'Qu1':[1,3,4,3,4],'Qu2':[2,3,1,2,3],'Qu3':[1,5,2,4,4]})
string_data = Series(['aardvark','artichoke',np.nan,'avocado'])
data = Series([1,NA,3.5,NA,7])
data = DataFrame([[1,6.5,3],[1,NA,NA],[NA,NA,NA],[NA,6.5,4]])
cleaned = data.dropna()
df = DataFrame(np.random.randn(7,3))
data = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])
frame=DataFrame(np.arange(12).reshape((4,3)),index=[['a','a','b','b'],[1,2,1,2]],
                  columns=[['Ohio','Ohio','Colorado'],['Green','Red','Green']])
frame = DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one',
                                                         'two','two','two',
                                                         'two'],
                     'd':[0,1,2,3,1,2,3]})
frame2 = frame.set_index(['c','d'])
ser = Series(np.arange(3.))
pdata = pd.Panel(dict((stk,web.get_data_yahoo(stk,'1/1/2009','6/1/2012'))
                      for stk in ['AAPL','MSFT','DELL']))
pdata = pdata.swapaxes('items','minor')
