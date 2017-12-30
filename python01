# Find查找指定字符串所有下标
# method-1
def my_find():
    str = input("请输入要查询的字符串：")
    kw = input("请输入想要查询的单词：")
    ti = -len(kw)
    while True:
        i = str.find(kw)
        if i != -1:
            ti = ti + i + len(kw)
            print(ti)
            str = str[i + len(kw)::]
        else:
            break
            
if __name__ == '__main__':
    my_find()
    
  
  
# menthod-2
def my_find():
    str = input("请输入要查询的字符串：")
    kw = input("请输入想要查询的单词：")
    ti = -len(kw)
    for a in range(str.count(kw)):
        i = str.find(kw)
        ti = ti + i + len(kw)
        print(ti)
        str = str[i + len(kw)::]

if __name__ == '__main__':
    my_find()



# method-3 生成器
def my_find(str, kw):
    ti = -len(kw)
    while str.find(kw) != -1:
        i = str.find(kw)
        ti = ti + i + len(kw)
        str = str[i + len(kw)::]
        yield ti



def main():
    str = input("请输入要查询的字符串：")
    kw = input("请输入想要查询的单词：")
    return my_find(str, kw)


if __name__ == '__main__':
    print(list(main()))
    # print(list(my_find("hellosadsahelloasdhhelloasd", "hello")))

# 使用列表推导式
def main():
    str = input("请输入要查询的字符串：")
    kw = input("请输入想要查询的单词：")
    # 使用列表推导式 对str循环切片与kw进行比较，相同则返回i(即下标)
    return [i for i in range(len(str)) if str[i:i+len(kw)] == kw]

if __name__ == '__main__':
    print(main())

 
