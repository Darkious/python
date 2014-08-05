from urllib import request
from urllib import error
import re
req = request.Request('http://csujwc.its.csu.edu.cn/XSXJ/Private/List_ZYBJ.aspx')
try: response = request.urlopen(req)
except error.URLError as e:
    if hasattr(e,'reason'):
        print(e.reason)
    elif hasattr(e,'code'):
        print(e.code,'code')

