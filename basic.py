class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
car1=Car('toyota',"red")
car2=Car('KIA','green')
print("Car 1 brand",car1.brand)
print("Car 1 color",car1.color)
print('Car 2 brand',car2.brand)
print('Car 2 color',car2.brand)
print(f"Car1- Brand {car1.brand} Color {car1.color}")
print(f"Car2- Brand {car2.brand} Color {car2.color}")
class Wallet:
    def __init__(self,balance):
        self.__balance=balance
    
    def deposit(self,amount):
            self.__validate(amount)
            self.__balance+=amount
    def withdraw(self,amount):
        self.__validate(amount)
        if amount> self.__balance:
            raise ValueError('Insufficien funds')
        else:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
    def __validate(self,amount):
        if amount < 0:
            raise ValueError('Amount must be positive')

        
acct_one = Wallet(0)
acct_one.deposit(3)
print(acct_one.get_balance()) # 3

acct_one.deposit(50)
print(acct_one.get_balance()) # 53
try:
    acct_one.deposit(-4)  # ValueError: Amount must be positive
except ValueError as e:
    print(e)
##acct_one.withdraw(-8) # ValueError: Amount must be positive
try:
    acct_one.withdraw(58) # ValueError: Insufficient funds
except ValueError as e:
    print(e)