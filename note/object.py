# =============================================================================
# CS61A 面向对象编程笔记
# =============================================================================

# =============================================================================
# 一, 类与实例
# =============================================================================

class Account:
    """
    Account 类 -- 银行账户的抽象模板.

    术语:
      class  -- 类, 定义一类对象的"蓝图"
      self   -- 指代当前实例本身, 必须作为方法的第一个参数
      method -- 定义在 class 里的 def, 操作实例的属性
    """

    bank_name = 'China Bank'  # 类属性: 所有实例共享

    def __init__(self, account_holder):
        """
        构造方法(前后各两个下划线).
        创建实例时自动调用: Account('orbro') -> __init__(新实例, 'orbro')
        """
        self.balance = 0           # 实例属性
        self.holder = account_holder

    def deposit(self, amount):
        """存款: balance += amount"""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """取款: 余额不足时拒绝"""
        if amount > self.balance:
            return 'Sorry, insufficient funds'
        self.balance = self.balance - amount
        return self.balance


# =============================================================================
# 二, 实例化的背后
# =============================================================================
# 执行 a = Account('orbro') 时:
#   1. Python 创建一个空实例(无任何属性)
#   2. 自动调用 Account.__init__(新实例, 'orbro')
#   3. __init__ 内部给 self 绑定属性(balance=0, holder='orbro')
#   4. 返回初始化完毕的实例, 绑定到变量 a

a = Account('orbro')
a.balance = 12          # 直接修改实例属性

b = Account('OrBrO')
b.balance = 200

# =============================================================================
# 三, 属性赋值与动态属性
# =============================================================================
# Python 允许给实例随时添加新属性(不需要预先声明)

a.backup = b            # 给 a 新增一个 backup 属性, 值为另一个 Account 实例
print(a.backup.balance) # -> 200

# =============================================================================
# 四, 别名(Aliasing)
# =============================================================================
# 多个变量绑定到同一个对象 -> 改一个, 另一个也跟着变

c = a                   # c 和 a 指向同一个 Account 实例
c.balance = 150
print(a.balance)        # -> 150(本质是同一块内存)

# =============================================================================
# 五, 属性查找顺序(点表达式求值规则)
# =============================================================================
# <expression>.<name> 的查找流程:
#   1. 先在实例属性里找 <name>
#   2. 找不到 -> 去该实例所属的类里找 <name>(类属性)

a.bank_name = 'America Bank'  # 在 a 上创建同名的实例属性("遮蔽"了类属性)

print(a.bank_name)  # -> 'America Bank'(实例属性优先)
print(b.bank_name)  # -> 'China Bank'(b 没有实例属性, 向上找到类属性)


# =============================================================================
# 六, 继承(Inheritance)
# =============================================================================
# 子类继承父类的所有属性和方法, 只需编写不同的部分.
# 语法: class <name>(<base class>)

class CheckingAccount(Account):
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        # Account.withdraw: 类名调用不自动绑self, 须手动传; 直接指定父类, 避免self.withdraw无限递归.
        # self.withdraw_fee: 类属性不在局部作用域, 必须通过self属性查找; 用self而非类名, 子类覆盖更灵活.
        return Account.withdraw(self, amount + self.withdraw_fee)


# =============================================================================
# 七, 类中名称查找规则
# =============================================================================
# 点表达式的查找顺序:
#   1. 如果实例中有该名称的属性 -> 返回属性值
#   2. 否则 -> 去父类中查找, 一直向上追溯

class SavingsAccount(Account):
    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


# =============================================================================
# 八, 多重继承(Multiple Inheritance)
# =============================================================================
# 一个子类可以有多个父类: class <name>(<base1>, <base2>)
# 属性查找按照 MRO(Method Resolution Order)从左到右, 找到即停.

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1       # 开户送 1 元


# =============================================================================
# 九, 组合(Composition)
# =============================================================================
# 一个对象把另一个对象作为属性, 叫做组合.
# 与继承的区别: 继承是"is-a", 组合是"has-a".

class Bank:

    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)       # 开户: 用 kind 类创建实例
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1
