import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open('write.csv', 'a') as file:
    csv.DictWriter(file, fieldnames=['name', 'home']).writerow({'name': name, 'home': home})