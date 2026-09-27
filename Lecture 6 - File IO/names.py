with open('names.txt', 'a') as file:
    file.write(input("What's your name? ") + '\n')

with open('names.txt', 'r') as file:
    for line in sorted(file, reverse=True):
        print(f'hello, {line.rstrip()}!')
