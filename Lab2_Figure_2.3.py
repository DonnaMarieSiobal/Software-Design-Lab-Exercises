class SavingsAccount(object):
    RATE = 0.02  # Single rate for all accounts
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string rep."""
        result = 'Name: ' + self.name + '\n'
        result += 'PIN: ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def deposit(self, amount):
        """Deposits the given amount and returns None."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """Withdraws the given amount.
        Returns None if successful, or an
        error message if unsuccessful."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

class Bank(object):
    def __init__(self):
        self.accounts = {}

    def __str__(self):
        return '\n'.join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        return name + "/" + pin

    def add(self, account):
        key = self.makeKey(account.getName(),
                           account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        total = 0.0

        for account in self.accounts.values():
                     total += account.computelnterest()

        return total

bank = Bank()
bank.add(SavingsAccount("Wilma", "1001", 4000.00))
bank.add(SavingsAccount("Fred", "1002", 1000.00))
print(bank, "\n")
account = bank.get("Wilma", "1000")
print(account, "\n")
account = bank.get("Wilma", "1001")
print (account, "\n")
account.deposit(25.00)
print(account, "\n")
print(bank)
