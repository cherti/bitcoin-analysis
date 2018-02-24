#!/usr/bin/env python3

"""
This Script reads the blockchain and parses all transactions into a structure
that contains only the information used in subsequent analysis runs to speed
those up.
"""

path_to_blockchain = 'bitcoin/blocks'
parsed_data_filename = 'bitcoin-transactions.txt'

import IPython
import sys, multiprocessing, time, json, bitcoin
from blockchain_parser.blockchain import Blockchain

# Instantiate the Blockchain by giving the path to the directory 
# containing the .blk files created by bitcoind
blockchain = Blockchain(path_to_blockchain)

truncation_counter = 0
arbitrary_error_counter = 0
txcounter = 0

def tx2dict(tx):
    txd = {}
    txd['hash'] = tx.hash
    txd['timestamp'] = block.header.timestamp.timestamp()  # because the timestamp is actually a datetime, therefore we call timestamp()
    txd['inputs'] = []
    txd['outputs'] = []
    for i in tx.inputs:
        txd['inputs'].append((str(i.transaction_hash), int(i.transaction_index)))

    for o in tx.outputs:
        txd['outputs'].append({'type':o.type, 'value':o.value, 'addresses':[a.address for a in o.addresses]})

    return txd

print(":: starting run")

t1 = time.time()

counter = 0

tx_datafile = open(parsed_data_filename, 'w')

for block in blockchain.get_unordered_blocks():
    counter += 1
    if counter%10000 == 0:
        print('current transactions:', txcounter)
    for tx in block.transactions:
        try:
            txd = tx2dict(tx)
            j = json.dumps(txd)
            print(j, file=tx_datafile)
            txcounter += 1
        except bitcoin.core.script.CScriptTruncatedPushDataError:
            truncation_counter += 1
        except:
            arbitrary_error_counter += 1




print()
print('Time used parsing:', t2-t1, 's')
print('truncation errors:', truncation_counter)
print('unclassified errors:', arbitrary_error_counter)

