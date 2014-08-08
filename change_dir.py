import os
import re
import time
def get_list(old_list,pattern):
    new_list = []
    for i in old_list:
        if pattern.search(i):
            new_list.append(i)
    return new_list
def get_new_list(old_list):
    new_list = []
    for i in old_list:
        element_time = os.stat(i).st_mtime
        difference = (time.time() - element_time)/86400
        if difference >=4 :
            new_list.append(i)
    return new_list
def change_dir_list(old_list):
    for i in old_list:
        if 'The.Last.Ship' in i:
            old_list.remove(i)
            os.rename(i,r'H:/电影/末日孤舰/'+i)
            print(i.ljust(35)+'移至H:/电影/末日孤舰')
        elif 'Tyrant' in i:
            old_list.remove(i)
            os.rename(i,r'H:/电影/Tyrant/'+i)
            print(i.ljust(35)+'移至H:/电影/Tyrant')
        elif '24.S09' in i:
            old_list.remove(i)
            os.rename(i,r'H:/电影/24h/'+i)
            print(i.ljust(35)+'移至H:/电影/24h')
        elif 'The.Flash' in i:
            old_list.remove(i)
            os.rename(i,r'H:/电影/The Flash/'+i)
            print(i.ljust(35)+'移至H:/电影/The Flash')
        else:
            os.rename(i,r'H:/电影/'+i)
            print(i.ljust(35)+'移至H:/电影')
    return old_list
def change_dir(list_dir):
    pattern = re.compile(r'.*\.(mkv|mp4|rmvb|ass|srt)$')
    os.chdir(list_dir)
    old_list = os.listdir()
    new_list = get_list(old_list,pattern)
    move_list = get_new_list(new_list)
    new_move_list = change_dir_list(move_list[:])
    return len(move_list)
if __name__ == "__main__":
    a = time.time()
    b = change_dir(r'H:\迅雷下载')
    dir_list = [i for i in os.listdir() if os.path.isdir(i)]
    for i in dir_list:
        c = change_dir('H://迅雷下载//'+i)
        b = b+c
    print('本次共移动%s部电影' %b)
    print(time.time()-a)
    input('按Enter键退出')
