#!/usr/bin/env python3

"""
This script extracts addresses on the blockchain, deduplicates them and counts their occurrence
"""
path_to_alladdreses = 'bitcoin-addresses.txt'
path_to_uniqueaddreses = 'bc-countedaddresses.txt'

counted_addrs = {}

import time

t1 = time.time()

with open(path_to_alladdreses, 'r') as f:
	addrs = f.read().strip().split('\n')

print("total addresses found:", len(counted_addrs))

t2 = time.time()

for a in addrs:
	if a not in counted_addrs:
		counted_addrs[a] = 1
	else:
		counted_addrs[a] += 1

print("unique addresses found:", len(counted_addrs))

t3 = time.time()

with open(path_to_uniqueaddreses, 'w') as f:
	for a, n in counted_addrs.items():
		print(a, n, file=f)

t4 = time.time()


print()
print('Time used for reading in data:', t2-t1, 's')
print('Time used for counting:       ', t3-t2, 's')
print('Time used for writing results:', t4-t3, 's')

input()
