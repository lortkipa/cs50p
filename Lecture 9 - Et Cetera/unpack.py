def f(*args, **kwargs):
    print(f'Positional: {args}')
    print(f'Named: {kwargs}')

f(100, 50, 25)
f(name='nika', last_name='lortki')