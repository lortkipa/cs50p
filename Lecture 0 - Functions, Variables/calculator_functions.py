def main():
    x = int(input('x: '))
    print(f'x squared is: {square(x)}')

def square(n):
    # return n ** 2
    # return n * n
    return pow(n, 2)

main()