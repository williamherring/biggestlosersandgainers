import re
import requests


def prev_close(page):
	match = re.findall(r'Prev Close:</th><td class="yfnc_tabledata1">(\w+[\w.]\w+)</', page)
	if match:
		return match
	else:
		print "Not Found"


def open_price(page):
	match = re.findall(r'Open:</th><td class="yfnc_tabledata1">(\w+[\w.]\w+)</', page)
	if match:
		return match
	else:
		print "Not Found"


def beta_score(page):
	match = re.findall(r'Beta:</th><td class="yfnc_tabledata1">(\S\w+[\w.]\w+)</', page)
	if match:
		return match
	else:
		print "Not Found"


def days_range_lower(page):
	match = re.findall(r"Day's Range:</th><td class=\"yfnc_tabledata1\"><span><span id=\"yfs_g53_\S+(\w+[\w.]\w+)</", page)
	if match:
		return match
	else:
		print "Not Found"


def days_range_higher(page, ticker):
	ticker = ticker.lower
	a = 'Day\'s Range:</th><td class="yfnc_tabledata1"><span><span id="yfs_g53_%s">(\d[\d.]\d+' % ticker
	match = re.findall(a, page)
	if match:
		return match, ticker
	else:
		print "Not Found"

#  Returns HTML of ticker page
def ticker_page(ticker):
	url = 'http://finance.yahoo.com/q?s=' + ticker
	page = requests.get(url)
	return page.text


print days_range_higher(ticker_page('UNXL'))



