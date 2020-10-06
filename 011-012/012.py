
#创建一个集合(无序、无重复项)
words_filter = set()
with open("filtered_words.txt", "r", encoding = "utf-8") as f:
    for x in f.readlines():
        #将需要屏蔽的词放入words_filter
        words_filter |= {x.strip("\n")}
while True:
    sentence = input("请输入需要检测的句子：")
    if sentence == "quit":
        break
    for x in words_filter:
        sentence = sentence.replace(x, "*"*len(x))
    print(sentence)
