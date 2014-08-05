from time import time
time1=time()
import pypyodbc
import pandas as pd;import numpy as np
import pickle
from pandas import DataFrame,Series
######################获取四六级成绩并将单项或总分为0的剔除掉##################
def get_data(DSN='MS201312',sheet='CET6_201312',index='*',drop=0):
    conn = pypyodbc.connect('DSN='+DSN)
    cur = conn.cursor()
    cur.execute("SELECT "+index+" FROM "+sheet)
    result = []
    for i in cur.fetchall():
        result.append(i)
    conn.close()
    result = DataFrame(result).drop(0,axis=1)
    result.columns = ['student_id','name','score','listening','reading','writing','academy']
    result = result.reindex(columns=['student_id','academy','name','score','listening','reading','writing'])
    if drop == 0:
        drop = result.isin([0])
        drop = drop.sum(axis=1)==0
        result = result[drop]
    elif drop == 1:
        drop = (result['score'].isin([0]) == False)
        result = result[drop]
    return result
######################获得每个学院的分类字典################################
def get_academy_data(data,academy):
    result={}
    for i in academy:
        result[i] = data[data['academy']==i]
    return result
CET_6 = get_data(drop=0)
CET_4 = get_data(sheet='CET4_201312',drop=0)
academy=np.union1d(CET_4['academy'].unique(),CET_6['academy'].unique())
CET_6_academy = get_academy_data(CET_6,academy)
CET_4_academy = get_academy_data(CET_6,academy)
######################每个院参加考试的人数##################################
def get_academy_sum(academy,sheet):
    result={}
    for i in academy:
        num=(sheet['academy']==i).sum()
        if num > 0:
            result[i] = num
##    result = DataFrame(result,columns=['academy','num'])
##    result = result.sort_index(by='num',ascending=False)
    result = Series(result,name='num')
    return result
###########################每个院总人数####################################
def get_academy_num(DSN='MS201312',academy=academy):
    result = []
    result_num={}
    conn = pypyodbc.connect('DSN='+DSN)
    cur = conn.cursor()
    cur.execute("SELECT xueyuan FROM csuxueshengxinxi")
    for i in cur.fetchall():
        result.append(i[0])
    result = Series(result)
    for i in academy:
        num = (result==i).sum()
        result_num[i] = num
    result = Series(result_num,name='num')
    return result
CET4_num = get_academy_sum(academy,CET_4)
CET6_num = get_academy_sum(academy,CET_6)
##CET_4 = CET_4.set_index('student_id')
##CET_6 = CET_6.set_index('student_id')
##a=CET_4
##b=CET_6
academy_sum = get_academy_num()
columns =['student_id','name','academy','score','listening','reading','writing','cet']
CET_4 = CET_4.reindex(columns=columns,fill_value=4)
CET_6 = CET_6.reindex(columns=columns,fill_value=6)
CET = pd.concat([CET_4,CET_6])
CET = CET.set_index(['cet','academy'])
with open('CET','wb') as f:
    pickle.dump(CET,f)
time2=time()
print(time2-time1)
