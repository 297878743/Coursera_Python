import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
url = address
uh = urllib.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('.//count')
sum = 0
for i in results:
    sum = sum + int(i.text)
print sum
