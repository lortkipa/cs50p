def main():
    x = get_int('x: ')
    print(x)

def get_int(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            pass # print('please enter a valid number')

main()