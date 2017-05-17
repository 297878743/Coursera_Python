import urllib 
import json

#http://python-data.dr-chuck.net/comments_42.json
#http://python-data.dr-chuck.net/comments_371741.json 
url = raw_input('Enter location: ')
uh = urllib.urlopen(url)
data = uh.read()
info = json.loads(data)
sum1 = 0
for i in info['comments']:
    sum1 = sum1 + i['count']
print sum1