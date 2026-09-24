# ask user for input and convert it to int
# int(input("x: "))
x = float(input("x: "))
y = float(input("y: "))

# calculate x + y and round it
#res = round(x + y)
res = x / y #res = round(x / y, 2)
print(f"res: {res:.2f}") # print(f"result: {res:,}")