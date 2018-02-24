#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

addrcnt = {}

with open('/datadump/datafiles/bc-countedaddresses.txt', 'r') as f:
	for line in f:
		addr, cnt = line.strip().split()
		cnt = int(cnt)
		if cnt not in addrcnt:
			addrcnt[cnt] = []

		addrcnt[cnt].append(addr)

print(len(addrcnt.keys()))

number = []
count  = []
histdata = {}

for cnt, addrs in addrcnt.items():
	number.append(len(addrs))
	count.append(cnt)
	histdata[cnt] = number

#plt.hist(histdata)
#plt.bar(count, number)

c, a = zip(*sorted(zip(count, number))) # unpack a list of pairs into two tuples

print('max amount of address-reuse:', max(a))
print('max different reuse-numbers:', max(c))

#fig = plt.figure(figsize=(9,6))
fig = plt.figure()
plt.title('address reusage')
plt.ylim(0, 2000)
plt.xlim(0, 3000)
plt.xlabel('number of usages')
plt.ylabel('number of addresses')
plt.plot(c, a)
plt.savefig('reusage.png')

print('plotting progress 1/3')

#fig = plt.figure(figsize=(9,6))
fig = plt.figure()
plt.title('address reusage')
plt.ylim(0, 8000)
plt.xlim(0, 5000)
plt.xlabel('number of usages')
plt.ylabel('number of addresses')
plt.plot(c, a)
plt.savefig('reusage-large.png')

print('plotting progress 2/3')

#fig = plt.figure(figsize=(9,6))
fig = plt.figure()
plt.title('address reusage')
plt.ylim(0, 2000)
plt.xlim(0, 3000)
plt.xlabel('number of addresses being used that often')
plt.ylabel('number of addresses')
plt.bar(c, a, width=100)
plt.savefig('aa-usage-barplot.png')
#plt.plot(count, number)
#plt.show()

print('plotting progress 3/3')

with open('address-reuse-stats', 'w') as f:
	reuse100 = 0
	for i in range(500):
		if i in addrcnt:
			reuse100 += len(addrcnt[i])

	print('addresses reused up to 100 times:     {}'.format(reuse100), file=f)

	reuse500 = 0
	for i in range(100, 500):
		if i in addrcnt:
			reuse500 += len(addrcnt[i])
	print('addresses reused 100 to 500 times:    {}'.format(reuse500), file=f)

	reuseinsane = 0
	for i in range(500, len(addrcnt)):
		if i in addrcnt:
			reuseinsane += len(addrcnt[i])

	print('addresses reused more than 500 times: {}'.format(reuseinsane), file=f)
