def main():
    name = input('name: ')
    hello(name)

def hello(name="\"No name\""):
    print(f'hello, {name}!')

main()