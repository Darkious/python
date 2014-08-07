from pandas import Series, DataFrame
import pandas as pd
def get_name(txt_list):
    name_list =[]
    new_name_list =[]
    for i in txt_list:
        a = i.split(' ')
        if len(a)==3:
            if len(a[1]) ==8 and len(a[0]) ==10:
                    name_list.append(a[2])
    for i in name_list:
        if i[0]== '【':
            new_name_list.append(i[4:])
        else:
            new_name_list.append(i)
    return new_name_list
if __name__ == "__main__":
    file_dir = r'C:\Users\46474_000\Desktop\一帮逗比欢乐多.txt'
    f = open(file_dir,'r',encoding= 'utf-8').readlines()[8:]
    f = [i.strip() for i in f if i.strip() != '']
    f = f[6:]
    name_list = Series(get_name(f))
    a= name_list.value_counts()
    for i in a.index:
        print(i,a.ix[i])
