#!/usr/bin/env python3

"""
This script counts the number of inputs and outputs of all transactions
on the Bitcoin blockchain
"""

data_file = 'bitcoin-transactions.txt'
chunk_size = 1000000

#import IPython
import sys, multiprocessing, time, json, os


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

    #IPython.embed()
    return txd

# load tx-jsons
t1 = time.time()

chunked_tx = []
txcounter = 0

print(":: reading in data")
with open(data_file, 'r') as f:
    current_chunk = []
    for line in f:
        txcounter += 1
        line = line.strip()
        if line == "": continue

        current_chunk.append(line)

        if txcounter % 1000000 == 0:
            print(":: reading data, currently at tx", txcounter)
            chunked_tx.append(current_chunk)
            current_chunk = []

cpus_in_use = min(len(chunked_tx), 50)
pool = multiprocessing.Pool(cpus_in_use)
print(":: aggregating data using {} cpus".format(cpus_in_use))

t2 = time.time()


print(":: counting inputs and outputs".format(cpus_in_use))

def count_in_out(txchunk):
    data = []
    for txline in txchunk:
        tx = json.loads(txline)
        number_in = len(tx['inputs'])
        number_out = len(tx['outputs'])
        data.append((number_in, number_out))

    return data


pool = multiprocessing.Pool(cpus_in_use)
pooledcounts = pool.map(count_in_out, chunked_tx)

with open('/datadump/bitcoin/counted_in_out.txt', 'w') as f:
    for l in pooledcounts:
        for number_in, number_out in l:
            print(number_in, number_out, file=f)

t3 = time.time()



print()
print('Time used for parsing and chunking data:  ', t2-t1, 's')
print('Time used for counting inputs and outputs:', t3-t2, 's')
