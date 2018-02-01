# 用python中的一等函数实现基本的策略模式
# 参考书籍《流畅的Python》 [巴西］Luciano Ramalho  著 安道　吴珂  译



# 经典策略模式
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")

class LineItem(object):
    def __init__(self, product, quantity, price):
        self.product =product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price*self.quantity

class Order(object):
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,  "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


# 把Promotion定义为抽象基类(Abstract Base Class, ABC),这么做是为了使用@abstractmethod装饰器，从而明确表明所用的模式
class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """返回周口金额（正值）"""

class FidelityPromo(Promotion):
    """积分1000分或以上提供5%折扣"""

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

class LargeOrderPromo(Promotion):
    """不同商品达到10个或以上时提供7%折扣"""

    def discount(self, order):
        # if len(order.cart)>=10:
        #     return order.total()*0.07
        # return 0
        discount_items = {item.product for item in order.cart}
        if len(discount_items)>=10:
            return order.total()*0.07
        return 0
# 策略对象是享元，即可共享的对象，可以同时在多个上下文（这里是Order实例）中使用
# 共享是推荐做法，这样不必在每个新的上下文重使用相同策略时不断新键具体策略对象(直接promotion(),无需指定实例对象)，从而减少消耗
# 但是经典策略模式的一个缺点是运行时消耗大
# 《设计模式：可复用面向对象软件的基础》的作者建议再使用另一个模式， 但代码行数和维护成本会上升

# 测试
joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)

cart = [LineItem("banana", 4, 0.5),LineItem("apple", 10, 1.5),LineItem("watermellon", 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

banana_cart = [LineItem("banana", 30, 0.5), LineItem("apple", 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo()))
print(Order(ann, banana_cart, BulkItemPromo()))

long_cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_cart, LargeOrderPromo()))
print((Order(ann, long_cart, LargeOrderPromo())))

# 使用函数实现策略模式
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")

class LineItem(object):
    def __init__(self, product, quantity, price):
        self.product =product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price*self.quantity

class Order(object):
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,  "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())

def fidelity_promo(order):
    """积分1000分或以上提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0



def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

def large_order_promo(order):
    """不同商品达到10个或以上时提供7%折扣"""
    # if len(order.cart)>=10:
    #     return order.total()*0.07
    # return 0
    discount_items = {item.product for item in order.cart}
    if len(discount_items)>=10:
        return order.total()*0.07
    return 0
# 计算折扣只需调用self.promotion()函数
# 没有抽象类
# 各个策略都是函数

# 测试
joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)

cart = [LineItem("banana", 4, 0.5),LineItem("apple", 10, 1.5),LineItem("watermellon", 5, 5.0)]
print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))

banana_cart = [LineItem("banana", 30, 0.5), LineItem("apple", 10, 1.5)]
print(Order(joe, banana_cart, bulk_item_promo))
print(Order(ann, banana_cart, bulk_item_promo))

long_cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_cart, large_order_promo))
print((Order(ann, long_cart, large_order_promo)))

# 结论
# 在复杂情况下，需要具体策略维护内部状态时，可能需要把"策略"和"享元"模式结合起来。但是，具体策略一般没有内部状态，只是处理上下文中的数据。
# 此时一定要使用普通函数，而不是编写只有一个方法的类。
# 再去实现另一个类声明的单函数接口。
# 函数比用户定义的类的实例轻量，无需使用"享元"模式，因为各个策略函数在python编译模块时只会创建一次。
# 普通函数也是可共享对象，可以同时在多个上下文中使用





# 选择最佳策略-简单的方式
# 我们在函数策略模式基础上添加一个新的具体策略 找出折扣额度最大的策略
promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)
# 新添加一个函数实现其他函数策略
# 参数同样是Order的一个实例对象
# 使用生成器表达式把order传给promos列表中的各个函数，返回折扣额度最大的那个函数

# 优化返回最大折扣的功能 使函数列表通过python获取而不是手动添加

# 通过globals()可以找出模块中全部函数
# globals()返回一个字典，标识当前的全局符号表。这个符号表始终针对当前模块（对函数或方法来说，是指定义他们的模块，而不是调用他们的模块）
# globals()找到所有函数策略名,把以_promo结尾的函数全部找出
promos = [globals()[name] for name in globals() if name.endswith("_promo") and name != "best_promo"]


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)

# 另一种方法，监理一个单独的模块promotions，把除"best_promo"意外的策略函数放进去
# 在主程序导入promotions模块 以及导入提供高阶内省函数的inspect模块
import promotions
import inspect

promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]
# inspect.getmembers函数用于获取对象，这里是promotions模块
# 第二个参数inspect.isfunction是可选判断条件(布尔函数值)，用于获取模块中的函数

def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)


# 还有用装饰器实现的"策略"模式
# 上面的函数策略模式 定义的列表中有函数名称，函数best_promo也有函数名称，产生了重复的情况，会导致新增策略函数后忘记添加进列表而产生问题
# 所以通过添加装饰器的方法解决这个问题

promos = []


def promotion(func):
    promos.append(func)
    return func

@promotion
def fidelity_promo(order):
    """积分1000分或以上提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount

@promotion
def large_order_promo(order):
    """不同商品达到10个或以上时提供7%折扣"""
    discount_items = {item.product for item in order.cart}
    if len(discount_items)>=10:
        return order.total()*0.07
    return 0


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)

# 此方法的好处是可以方便管理各种策略





