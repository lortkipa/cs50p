def main():
    num = int(input('num: '))
    print(f'{num} squared is {square(num)}')

def square(n):
    return n * n

if __name__ == "__main__":
    main()