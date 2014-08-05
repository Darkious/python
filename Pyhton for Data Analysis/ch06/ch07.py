##from lxml.html import parse
##from urllib.request import urlopen
##from pandas.io.parsers import TextParser
##response = urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options')
##parsed = parse(response)
##doc = parsed.getroot()
##links = doc.findall('.//a')
##lnk =links[28]
##urls = [lnk.get('href') for lnk in doc.findall('.//a')]
##tables = doc.findall('.//table')
##calls = tables[9]
##puts = tables[13]
##rows = calls.findall('.//tr')
##def _unpack(row,kind='td'):
##    elts =row.findall('.//%s' %kind)
##    return [val.text_content() for val in elts]
##def parse_options_data(table):
##    rows = table.findall('.//tr')
##    header = _unpack(rows[0],kind='th')
##    data = [_unpack(r) for r in rows[1:]]
##    return TextParser(data,names=header).get_chunk()
##call_data = parse_options_data(calls)
##put_data = parse_options_data(puts)
##import requests
##import json
##url = 'http://search.twitter.com/search.json?q=python%20pandas'
##resp = requests.get(url)
##data = json.loads(resp.text)
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
df1 = DataFrame(np.arange(6).reshape(3,2),index=['a','b','c'],columns=['one','two'])
df2 = DataFrame(5+np.arange(4).reshape(2,2),index=['a','c'],columns=['three','four'])
df1 = DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
df2 = DataFrame(np.random.randn(2,3),columns=['b','d','a'])
a = Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],index=['f','e','d','c','b','a'])
b = Series(np.arange(len(a)),dtype=np.float64,index=['f','e','d','c','b','a'])
b[-1] = np.nan
df1 = DataFrame({'a':[1,np.nan,5,np.nan],
                'b':[np.nan,2,np.nan,6],
                'c':range(2,18,4)})
df2 = DataFrame({'a':[5,4,np.nan,3,7],
                 'b':[np.nan,3,4,6,8]})
data =DataFrame(np.arange(6).reshape(2,3),index=pd.Index(['Ohio',
                                                          'Colorado'],
                                                         name='state'),
                columns=pd.Index(['one','two','three'],name='number'))
result = data.stack()
s1 = Series(np.arange(4),index=['a','b','c','d'])
s2 = Series([4,5,6],index=['c','d','e'])
data2 = pd.concat([s1,s2],keys=['one','two'])
df = DataFrame({'left':result,'right':result+5},columns=pd.Index(
    ['left','right'],name='side'))
ldata = pd.read_csv('macrodata.csv')
ldata = ldata[['year','realgdp','infl','unemp']]
a = ldata[['realgdp','infl','unemp']].stack()
b = ldata['year']
































