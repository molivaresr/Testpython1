# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

req = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
soup = BeautifulSoup(req.text, "lxml")
soup.title
soup.title.name
soup.title.string
soup.h1
soup.h1.string
soup.h1.attrs

x = soup.h1['lang']
print(soup.title.string)
print(soup.h1.string)
print(soup.h1.attrs)
if soup.h1['lang'] == x: print("Idioma Inglés")
# for sub_heading in soup.find_all('h2'):
#     print(sub_heading.text)
print(soup.p.parent.name)
for parent in soup.p.parents:
    print(parent.name)

print(soup.p.a)
# print(soup.p.contents)
# # [<b>Python</b>, ' is a widely used ',.....the full list]
 
# print(soup.p.contents[10])
# # # <a href="/wiki/Readability" title="Readability">readability</a>
 
for child in soup.p.children:
    print(child.name)