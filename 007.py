import os.path
import re

def count(dirPath):
    #用于存储数据
    blanklines, commentlines, codelines, totallines = 0, 0, 0, 0, 
    f_list = os.listdir(dirPath)
    for i in f_list:
        if os.path.splitext(i)[1] == ".py":
            #以UTF-8的编码形式打开后缀名为.py的文件
            with open(dirPath+"\\"+i, encoding = "UTF-8")as f:
                #打印文件名，用于调试
                #print(dirPath+"\\"+i)
                while True:
                    line = f.readline()
                    totallines += 1
                    #如果读取到文章末尾则结束循环，打开下一个文件
                    if line == "":
                        break
                    #line.strip()删除每行开始的空格，
                    elif line.strip().startswith("#"):
                        commentlines += 1
                    #如果strip()之后以 ''' or """ 开头，则说明多行注释开始
                    elif line.strip().startswith('"""') or line.strip().startswith("'''"):
                        #如果此行中''' or """ 只出现一次，则下面为多行注释内容
                        if line.count("'''") == 1 or line.count('"""') == 1:
                            commentlines += 1
                            while True:
                                line = f.readline()
                                totallines += 1
                                commentlines += 1
                                if ("'''" in line) or ('"""' in line):
                                    break
                                
                        else:
                            commentlines += 1
                            
                    elif line.strip():
                        codelines += 1
                    else:
                        blanklines += 1
        
    #打印出行数
    print('the nuber of totalines is : ' + str(totallines-1))
    print('the nuber of comments is : ' + str(commentlines))
    print('the nuber of codelines is : ' + str(codelines))
    print('the nuber of blanklines is : ' + str(blanklines))

count(r"E:\learn\proteus7.8")
                
                

