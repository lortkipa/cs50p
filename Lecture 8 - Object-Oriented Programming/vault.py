class Vault:
    def __init__(self, gallions=0, sickles=0, knuts=0):
        self.gallions = gallions
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f'{self.gallions} gallions, {self.sickles} sickles, {self.knuts} knuts'

    def __add__(self, other):
        gallions = self.gallions + other.gallions
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(gallions, sickles, knuts)

potter = Vault(100, 50, 25)
print(f'Potter: {potter}')

weasly = Vault(25, 50, 100)
print(f'Weasly: {weasly}')

total = potter + weasly
print(f'Total: {total}')