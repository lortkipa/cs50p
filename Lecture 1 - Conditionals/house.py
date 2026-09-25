name = input("What's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gyffindor")
# elif name == "Drako":
#     print("Slytherin")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gyffindor")
    case "Drako":
        print("Slytherin")
    case _:
        print("Who?")