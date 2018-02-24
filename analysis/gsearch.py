"""
This script checks the number of search results for the most frequently used
addresses on the blockchain.
Yes, this can likely be significantly improved by using a google API instead of scraping the search page.
"""

import requests
from bs4 import BeautifulSoup

def gsearchresults(searchterm):
	query = "https://www.google.com/search?q=" + searchterm

	r = requests.get(query)
	html_doc = r.text

	soup = BeautifulSoup(html_doc, 'html.parser')

	count = 0
	for s in soup.find_all("div", {'class':'s'}):
		# filter out blockchain.info as we find *all* addresses there
		# it's a bitcoin analysis frontend after all
		if 'blockchain.info' not in s.text:
			count += 1

	return count


addrcnt = {}

with open('bc-countedaddresses.txt', 'r') as f:
	for line in f:
		addr, cnt = line.strip().split()
		cnt = int(cnt)
		if cnt not in addrcnt:
			addrcnt[cnt] = []

		addrcnt[cnt].append(addr)

number = []
count  = []

for cnt, addrs in addrcnt.items():
	number.append(len(addrs))
	count.append(cnt)
	#histdata[cnt] = number

c, a = zip(*sorted(zip(count, number))) # unpack a list of pairs into two tuples

candidates = c[-10000:]

with open("manyaddresses2google", 'w') as f:
	for count in candidates:
		for cand in addrcnt[count]:
			print(cand)
			print(cand, file=f)

