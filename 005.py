import collections
import os
from PIL import Image

with open("test.txt", "r") as f:
    str1 = f.read().split(" ")
    counter = collections.Counter(str1)
with open("result.txt", "w")as f:
    for key,value in counter.items():
        f.write(key +":"+str(value)+"\n")

    

x, y  = 4, 5
if x>y:
    small  =y
else:
    small = x

small = x if x<y else y


he = lambda x, y: x+y


def Size(dirPath, size_x, size_y):
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == ".jpg":
            print(dirPath+"\\"+i)
            img = Image.open(dirPath+"\\"+i)
            img.thumbnail((size_x, size_y))
            img.save(i)

Size(r"C:\Users\Administrator\Desktop\test", 1136, 640)
