class Dog:
    special='this dog is a special '
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def wakup(self):
        
        if int(self.age)%2==0:
            return f"the {self.name} is wakeup"
        else:
            return f"the {self.name} is sleep"

    def __str__(self):
        return "hii im here"
    
    def areyuok(self):
        if len(self.name)%2==0:
            return f"the {self.name} is ok"
        


d1=Dog('lucy',3,'hasky')
d2=Dog('alex',2,'german')
print(d1.name)
print(d1.wakup())
print(d2.areyuok())

class BankAccount:
    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        # _balance یک قرارداد است که نشان می‌دهد این ویژگی نباید مستقیماً از بیرون دستکاری شود.
        # این یک "weakly private" attribute است.
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposit successful. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawal successful. New balance: {self._balance}")
            return amount
        elif amount > self._balance:
            print("Insufficient funds.")
            return 0
        else:
            print("Withdrawal amount must be positive.")
            return 0

    def get_balance(self):
        # این متد به عنوان یک رابط برای دسترسی به بالانس عمل می‌کند
        return self._balance

# ساخت شیء
account = BankAccount("Alice", 1000)

# استفاده از متدهای public
account.deposit(500)
account.withdraw(200)

# دسترسی به بالانس از طریق متد get_balance (بهترین روش)
print(f"Current balance for {account.owner_name}: {account.get_balance()}")

# تلاش برای دسترسی مستقیم به _balance (ممکن است، اما توصیه نمی‌شود)
# print(f"Direct access to balance: {account._balance}")
# account._balance = -5000 # این کار نباید انجام شود، زیرا از منطق کلاس خارج است
# print(f"Balance after direct manipulation: {account.get_balance()}")
