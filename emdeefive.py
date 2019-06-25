import os
import hashlib
from bs4 import BeautifulSoup
import requests

print("----------------------------------")
print("EMDEEFIVE TOOL BY TIKVAH")
print("----------------------------------")
print("")
print("Please enter a URL, INCLUDING the HTTP://")
emdeeurl = input("--->")
b = requests.Session()
r = b.get(emdeeurl)
soupyboi = BeautifulSoup(r.content, "html.parser")
sup = soupyboi.find('h3')
m = hashlib.md5(sup.text.encode("UTF-8")).hexdigest()
print("Original: " + sup.text)
print("MD5 Hash is: " + m)
print("Sending POST Request")
data ={'hash': m}
p = b.post(emdeeurl, data = data)
suppy = BeautifulSoup(p.content, "html.parser")
flag = suppy.find('p')
print("Flag is: " + flag.text)