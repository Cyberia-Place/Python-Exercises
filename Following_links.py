import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduce URL: ')
position = int(input('Introduce position: '))
counter = int(input('Introduce repetitions: '))
lst = list()
name = None

while (counter > 0):
    counter -= 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    anchor_tags = soup('a')

    href_name = anchor_tags[position-1]
    name = href_name.contents[0]
    url = href_name.get('href')
print(name)
