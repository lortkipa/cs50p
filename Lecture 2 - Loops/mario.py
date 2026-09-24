def main():
    print_square(3, 4)

def print_column(height):
    print('#\n' * height, end='')

def print_row(width):
    print('?' * width)

# def print_square(width, height):
#     for i in range(height):
#         for j in range(width):
#             print('#', end='')
#         print()
def print_square(width, height):
    for i in range(height):
        print('#' * width)

main()