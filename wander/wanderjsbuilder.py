import requests
from bs4 import BeautifulSoup
import re

url = "https://codeberg.org/susam/wander/issues/1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = []
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']

    if re.match(r'https?://.*/wander/?$', href):
        links.append(href)

unique_consoles = sorted(list(set(links)))

wander_js = "window.wander = {\n"
wander_js += "  consoles: [\n"
for console in unique_consoles:
    wander_js += f"    \"{console}\",\n"
wander_js = wander_js.rstrip(',\n') + "\n  ],\n"
wander_js += "  pages: [\n    // Add your recommended pages here\n  ]\n};\n"

with open('wander.js', 'w') as f:
    f.write(wander_js)

print(f"Generated wander.js with {len(unique_consoles)} consoles.")
