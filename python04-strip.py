# 实现strip()功能
def my_strip(my_str):
    a = my_str.find(" ")
    while a == 0:
        my_str = my_str[a+1:]
        a = my_str.find(" ")
    b = my_str.rfind(" ")
    while (b == len(my_str) - 1) and b != -1:
        my_str = my_str[:b]
        b = my_str.rfind(" ")
    return my_str

print(my_strip("      hello  world      "))
