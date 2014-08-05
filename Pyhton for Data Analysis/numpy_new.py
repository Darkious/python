import json
from time import time
from collections import defaultdict
from pandas import DataFrame,Series
from pylab import *
import pandas as pd;import numpy as np
time1=time()
path= r'C:\Users\46474_000\Desktop\usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
def get_counts2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts
def top_counts(count_dict,n=10):
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
counts = get_counts2(time_zones)
topcounts=top_counts(counts)
frame=DataFrame(records)
tz_counts=frame['tz'].value_counts()
clean_tz=frame['tz'].fillna('Missing')
clean_tz[clean_tz == '']='Unknown'
tz_counts =clean_tz.value_counts()
tz_counts[:10].plot(kind='barh',rot=0)
plt.show()
time2=time()
print(time2-time1)