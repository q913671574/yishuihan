import urllib.request
import urllib
import re
from bs4 import BeautifulSoup

response =urllib.request.urlopen("https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%B7%AF%E9%A3%9E")
data = response.read().decode('utf-8')

"""
soup = BeautifulSoup(data)
content = soup.prettify()
"""

#创建find规则
regex = re.compile(r'thumbURL\"\:\"(.*?)\"')
#在data中寻找符合regex的对象，传给results(列表)
results = regex.findall(data)
"""
for i in range(4):
    print(results[i])
"""
#图片序号
picnum = 0
for x in results:
    if (".jpg" in x):
        #打开图片网址，读取数据保存在img中
        img = urllib.request.urlopen(x, timeout = 3).read()
        #打开(创建)一个以picnum.jpg为名字的文件;每打开一个文件picnum+1(避免覆盖)
        with open(str(picnum) + ".jpg" , "wb") as f:
            #将img数据写入f(picnum.jpg)中
            f.write(img)
            picnum += 1
            f.close
    else:
        print("No")
print("done")
    

