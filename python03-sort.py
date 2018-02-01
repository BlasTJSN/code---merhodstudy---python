# 排序算法
# 1-桶排序
def sort1(lists):
    num_max = max(lists)
    battle = [0]*(num_max+1)
    for i in lists:
        battle[i] += 1
    sort_list = list()
    for num in range(len(battle)):
        if battle[num] != 0:
            for n in range(battle[num]):
                sort_list.append(num)
    return sort_list

print(sort1([5, 1, 7, 88, 3, 5, 2, 79, 77]))


# 2-冒泡排序
def sort2(lists):
    flag = 1
    for i in range(len(lists)-1, 0, -1):
        if flag: # 减少循环次数 确保排序完成就结束循环
            flag = 0
            for j in range(i):
                if lists[j] > lists[j+1]:
                    lists[j], lists[j+1] = lists[j+1], lists[j]
                    flag = 1
        else:
            break
    return lists

print(sort2([5, 1, 7, 88, 3, 5, 2, 79, 77]))


# 3-快速排序
def main_sort(lists, first, last):
    if first < last:
        target = move_sort(lists, first, last)
        main_sort(lists, first, target-1)
        main_sort(lists, target+1, last)


def move_sort(lists, front, back):
    key = lists[front]
    while front < back:
        while front < back and lists[back] >= key:
            back -= 1
        lists[front] = lists[back]
        while front < back and lists[front] <= key:
            front += 1
        lists[back] = lists[front]
    lists[front] = key
    return front
lists = [5, 1, 7, 88, 3, 5, 2, 79, 77]
main_sort(lists, 0, 8)
print(lists)

# 斐波那契数列
def fib(n):
    lists = [0, 1]
    for i in range(n):
        lists.append(lists[-1] + lists[-2])
    return lists

print(fib(10))
