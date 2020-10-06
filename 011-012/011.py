import codecs

#方法一：
def filtered_words():
    words = str(input("请输入需要检测的词语:"))
    with open("filtered_words.txt", "r", encoding="utf-8") as f:
        while True:
            temp = f.readline().strip()
            if words == temp:
                print("Freedom")
                break
            elif temp == "":
                print("Human Rights")
                break
            



if __name__ == "__main__":
    filtered_words()

#方法二：
"""
import codecs
def read_txt():
    l=[]
    with codecs.open('filtered_words.txt', encoding = "utf-8") as fp:
        for line in fp.readlines():
           l.append(line.strip())
    return l

def check(l):
    word=input('word:')
    for each_word in l:
        if word==each_word:
            print("Freedom")
            return None
    print ("Human rights")
    return None

def main():
    l=read_txt()
    check(l)
    print ()

if __name__=='__main__':
    main()


"""
