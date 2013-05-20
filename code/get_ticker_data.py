import re
import requests
import datetime
# import new_data


def Finds(pat, text):
    match = re.findall(pat, text)
    if match:
        for m in match:
        	print m
        return match
    else:
        print 'No Ticker Symbol matches'

page = requests.get('http://finance.yahoo.com/losers?e=o')

pattern = r'"yfs_p20_(\w+)">'
txt = page.text

tickers = Finds(pattern, txt)

#date
now = datetime.datetime.now()
the_date = "%s/%s/%s" % (now.month, now.day, now.year)

#  Returns HTML of ticker page
def ticker_page(ticker):
	url = 'http://finance.yahoo.com/q?s=' + ticker
	page = requests.get(url)
	return page.text

