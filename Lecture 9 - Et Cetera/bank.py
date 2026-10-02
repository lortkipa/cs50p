# balance = 0

# def main():
#     print('balance:', balance)
#     deposit(100)
#     withdraw(50)
#     print('balance:', balance)

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == '__main__':
#     main()

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

def main():
    acc = Account()
    print(f'balance: {acc.balance}')
    acc.deposit(100)
    acc.withdraw(50)
    print(f'balance: {acc.balance}')

if __name__ == '__main__':
    main()