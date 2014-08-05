import pandas as pd;import numpy as np
from pandas import DataFrame,Series
##df1 = DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
##df2 = DataFrame({'key':['a','b','d'],'data2':range(3)})
##df3 = DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})
##df4 = DataFrame({'rkey':['a','b','d'],'data2':range(3)})
##df1 = DataFrame({'key':['b','b','a','c','a','b'],'data1':range(6)})
##df2 = DataFrame({'key':['a','b','a','b','d'],'data2':range(5)})
##left = DataFrame({'key1':['foo','foo','bar'],
##                  'key2':['one','two','one'],
##                  'lval':[1,2,3]})
##right = DataFrame({'key1':['foo','foo','bar','bar'],
##                  'key2':['one','one','one','two'],
##                  'rval':[4,5,6,7]})
##left1 = DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})
##right1 = DataFrame({'group_val':[3.5,7]},index=['a','b'])
##lefth = DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],
##                   'key2':[2000,2001,2002,2001,2000],
##                   'data':np.arange(5)})
##righth = DataFrame(np.arange(12).reshape(6,2),index=[['Nevada','Nevada','Ohio','Ohio','Ohio',
##                                                      'Ohio'],[2001,2000,2000,2000,2001,2002]],
##                   columns=['event1','event2'])
arr = np.arange(12).reshape((3,4))
s1 = Series([0,1],index=['a','b'])
s2 = Series([2,3,4],index=['c','d','e'])
s3 = Series([5,6],index=['f','g'])
s4 = pd.concat([s1*5,s3],axis=0)
result = pd.concat([s1,s1,s3],keys=['one','two','three'])
