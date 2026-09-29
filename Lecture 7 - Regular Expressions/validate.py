import re

email = input("What's your email? ").strip()

# username, domein = email.split('@')

# if username and domein.endswith('.com'):
#     print('valid')
# else:
#     print('invalid')

# if re.search(r'^[a-zA-Z-0-9]+@\[a-zA-Z-0-9]+\.com$', email):
if re.search(r'^\w+@(\w+\.)?\w+\.(com|ge)$', email, re.IGNORECASE):
    print('valid')
else:
    print('invalid')