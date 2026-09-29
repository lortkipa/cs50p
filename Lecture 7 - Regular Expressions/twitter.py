import sys
import re

# https://twitter.com/lortkipa
# http://www.twitter.com/lortkipa

url = input('URL: ').strip()

# username = re.sub(r'^(https?://)?(www\.)?twitter\.com/', '', url)

if matches := re.search(r'^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)', url, re.IGNORECASE):
    print(f'username: {matches.group(1)}')
else:
    sys.exit('invalid url')