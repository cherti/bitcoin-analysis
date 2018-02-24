#!/usr/bin/env python3

"""
This script counts the number of transactions that paid to wannacrypt
and how much they made with it
"""

parsed_data_filename = 'bitcoin-transactions.txt'
satoshi2btc = 0.00000001 #1 satoshi is one hundred millionth of a BTC

import time, json

wannacrypt = [
'13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94',
'12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw',
'115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn'
]

# parse and process tx
t1 = time.time()

allwctx = []
amount = 0
with open(parsed_data_filename, 'r') as f:
    for line in f:
        tx = json.loads(line)
        for o in tx['outputs']:
            for a in wannacrypt:
                if a in o.addresses:
                    allwctx.append(tx['hash'])
                    amount += o['value']


t2 = time.time()

print()
print('Transactions that paid to WannaCrypt found:', len(allwctx))
print('Amount paid to WannaCrypt:', amount*satoshi2btc)
print('Time used for parsing and processing data:   ', t2-t1, 's')

