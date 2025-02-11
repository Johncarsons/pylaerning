from abc import ABC, abstractmethod
# encapsulation
# declaring valuables is called encapsulation
class Account:
    def __init__(self, account_id, holders_name, balance):
        self.account_ID = account_id
        self.holders_name = holders_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount #if balance
        print(f"Deposit of {amount} to {self.holders_name} is successful. New balance is {self.balance}")


    def withdraw(self, amount):
        print(f"Attemoting to withdraaw {amount} from account with  {self.balance} as balance.")
        if amount <= self.balance:
            self.balance -= amount #subtract from balance
            print(f"Withdrawal of {amount} successful. Account balance is now {self.balance}")
        else:
            print(f"Insufficient balance. Account balance is {self.balance} ")
    def get_balance(self):
        return self.balance

    def get_holders_name(self):
        return self.holders_name
    # Inheritance

class Customer(Account):
    def __init__(self, account_id, holders_name, balance, phone_number):
        super().__init__(account_id, holders_name, balance)
        self.phone_number = phone_number
# poolymorphisim
class Transaction:
    def __init__(self,amount):
        self.amount = amount
    def execute(self, account):
        pass
class DepositTransaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)
class WithdrawTransaction(Transaction):

    def execute(self, account):
        account.withdraw(self.amount)

# abstraction
class Paymentsystem(ABC):
    @abstractmethod
    def process_payment(self, ammount):
        pass
class MpesaPayment(Paymentsystem):
    def process_payment(self, ammount):
        print(f"Processing Mpesa payment of {ammount}")


# Example usage
mpesa = MpesaPayment
account1 =  Customer( account_id = "1324", holders_name = "Eric ", balance = 2000, phone_number = 711685266 )
deposit1 = DepositTransaction(0)
withdraw1 = WithdrawTransaction(2000)

deposit1.execute(account1)
withdraw1.execute(account1)
print(f"The balance of {account1.get_holders_name()} is {account1.get_balance()}")

account2 = Customer( 56789, "Kiama", 123456789, 722357224)
deposit2 = DepositTransaction(560)
withdraw2 = WithdrawTransaction(910000)
deposit2.execute(account2)
withdraw2.execute(account2)
print(f"The balance of {account2.get_holders_name()} is {account2.get_balance()}")