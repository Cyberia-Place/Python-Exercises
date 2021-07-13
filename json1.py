import json
import urllib.request, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduce URL: ')
archive = urllib.request.urlopen(url, context=ctx).read().decode()
json = json.loads(archive)

number_sum = 0
contador = 0
for item in json['comments']:
    number_sum += int(json['comments'][contador]['count'])
    contador += 1
print('Retrieving', url)
print('Retrieved', len(archive), 'characters')
print('Count:', len(json['comments']))
print('Sum:', number_sum)
