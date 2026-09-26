from random import choice
import random

coin = choice(['heads', 'tails'])
print('coin', coin, sep=': ')

randint = random.randint(1, 10)
print('random number between 1-10', randint, sep=': ')

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
print('shuffled cards', cards, sep=': ')