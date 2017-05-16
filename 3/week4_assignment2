# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import re
import urllib
from bs4 import *
namelist = []
url = raw_input('Enter - ')
a = re.findall('by_(.*).html',url)
b = str(a[0])
namelist.append(b)

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
i = 0
# Retrieve all of the anchor tags

while i<7:
    tags = soup('a')
    m = tags[17].get('href', None)
    m = str(m)
    
    name = re.findall('by_(.*).html',m)
    
    name1 = str(name[0])
    namelist.append(name1)
    url = m
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    i = i+1
print namelist
