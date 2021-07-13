import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

input = input('URL: ')
if len(input) > 1:
    xml = urllib.request.urlopen(input, context=ctx).read()
    tree = ET.fromstring(xml)
    lst = tree.findall('.//comment')
    number_sum = 0
    for comment in lst:
        number = int(comment.find('count').text)
        number_sum += number
    print(number_sum)
else:
    print('Try another URL')
