
# 证明范围内哥德巴赫猜想
# method-1
def fun(n):
    list1 = [x for x in range(8, n+1, 2)]  # 把偶数放入列表
    list2 = list()
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list2.append(i) # 把质数放入列表
    for c in list1:
        is_Prime = True
        for a in list2:
            if is_Prime: # 如果为False 跳过本次循环 保证每个a只出现一次
                for b in list2:
                    if a + b == c:
                        print("%d+%d=%d" % (a, b, c))
                        is_Prime = False

fun(1000)

# method-2 -待完善
i = 6
while True:
    i += 2
    for a in range(2, i):
        is_True = True
        b = i - a # 保证a + b == i
        if i - a <= 1:
            is_True = False # 防止b == 1
        if is_True:
            for x in range(2, a):
                if a % x == 0:
                    is_True = False
            for y in range(2, b):
                if b % y == 0:
                    is_True = False
        if is_True: # 保证只出现质数的运算
            print("%d+%d=%d" % (a, b, i))
            break # 保证每次i只出现一次
