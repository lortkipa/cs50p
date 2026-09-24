# ask user for their name
name = input("What's your name? ")

# remove whitespaces and capitalize user's name
name = name.strip().title()

# get user's first and last name
first, last = name.split()

# say hello to user
print("Hello, ", end="")
print(first)

print("Hello, ", first, sep="")

print(f"Hello, {first}")

# say hello "friend"
#print("Hello, \"friend\"")

"""
this is multi-line comments.
second line...
third line...
"""