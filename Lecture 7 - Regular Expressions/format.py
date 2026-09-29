import re

name = input("What's your name? ").strip()


if matches := re.search(r'^(.+), *(.+)$', name):
    name = f'{matches.group(2)} {matches.group(1)}'
    # last, first = matches.groups()
    # name = f'{first} {last}'

print(f'hello, {name}')