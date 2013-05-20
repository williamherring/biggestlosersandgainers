import re
import requests


def Finds(pat, text):
    match = re.findall(pat, text)
    if match:
        print
        return match
    else:
        print 'No Ticker Symbol matches'

a = requests.get('http://finance.yahoo.com/losers?e=o')

pattern = r'"yfs_p20_(\w+)">'
txt = a.text

Finds(pattern, txt)