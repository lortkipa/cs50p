def main():
    n = get_num()
    meow(n)

def get_num():
    while True:
        n = int(input('n: '))

        if n > 0:
            return n

def meow(count):
    for _ in range(count):
        print('meow')

main()
