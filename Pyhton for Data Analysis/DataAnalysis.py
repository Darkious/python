from time import time
time1 = time()
import pandas as pd;import numpy as np
from pandas import Series
from pandas import DataFrame
import pickle
with open('CET','rb') as f:
    CET=pickle.load(f)
time2 = time()
print(time2 - time1)
