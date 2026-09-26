def main():
    name = input("Wha'ts your name? ")
    print(hello(name))

def hello(name="[NO NAME]"):
    return f'hello, {name}!'

if __name__ == '__main__':
    main()