class bankaccount:
    bank_name = "ABC Bank"
    @classmethod
    def changeBank(cls):
        cls.bank_name="supreme bank"
    @staticmethod
    def calculate_intrest(principle,rate,time):
        i=principle*rate*time/100
        print("interst :",i)
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance
    def display(self):
        print("Account details")
        print("account numbers:",self.account_number)
        print("account holder :",self.account_holder)
        print("bank name",self.bank_name)

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Balance after deposit: {self.__balance}" )
        else:
            print("Deposit amount must be positive")
    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.__balance}")
        else:
            print("Insufficient balance")
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,balance):
        if balance >= 0:
         self.__balance = balance
        else:
          print("Invalid balance")


if __name__ == "__main__":
    print(bankaccount.bank_name)
    b1 = bankaccount('123456', 'John Doe', 1000)
    b2= bankaccount('789012', 'Jane Smith', 2000)
    print(b1.balance)
    b1.balance=900000
    print(b1.balance)
