import xlwt
import re

book = xlwt.Workbook(encoding = "utf-8", style_compression=0)
sheet = book.add_sheet("student", cell_overwrite_ok = True)
with open("student.txt", "r", encoding = "utf-8") as f:
    text = f.read()
regex = re.compile(r'\"(\d+)\":\[\"(.*?)\",(\d+),(\d+),(\d+)\]')
info = regex.findall(text)
"""
print(info)
print(type(info))           #info类型为列表
print(type(info[0]))        #info[]类型为元组
"""
line = 0
#取出info列表中每组数据
for x in info:
    #取出x中的每个数据，并以i为列数(下标)，将数据依此写入sheet的单元格中
    for i in range(len(x)):
        sheet.write(line, i, x[i])
    line += 1
book.save("student.xls")
