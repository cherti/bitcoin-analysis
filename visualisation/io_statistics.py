#!/usr/bin/env python

from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
import gc

plt.switch_backend('agg')

io = []
il = []
ol = []
#with open('/datadump/datafiles/counted_in_out.txt', 'r') as f:
with open('counted_in_out.txt', 'r') as f:
	for line in f:
		i, o = line.strip().split()
		i, o = int(i), int(o)
		if i <=300 and o <=300:
			il.append(i)
			ol.append(o)

#points = np.loadtxt('/datadump/datafiles/counted_in_out.txt')

il = np.array(il)
ol = np.array(ol)

print('loading data done, plotting')

fig = plt.figure(figsize=(9,6))
#plt.title('input/output ratios')
#plt.xlim(0, 300)
#plt.ylim(0, 300)
plt.xlabel('Anzahl der Transaktions-Inputs')
plt.ylabel('Anzahl der Transaktions-Outputs')
#plt.hexbin(il, ol, xscale='log', yscale='log', bins='log')
plt.hexbin(il, ol, bins='log', gridsize=50) #, mincnt=1)
#plt.xlim(1000)
#plt.ylim(1000)
#plt.colorbar(ticks=["$10^"+str(i)+"$" for i in range(9)])
#plt.colorbar(ticks=["$$10^0$$", "$$10^1$$"])
cb = plt.colorbar(ticks=[i for i in range(9)])
#cb.ax.set_yticklabels(["a", "b", "c", "d", "e", "f", "g", "h"])
cb.ax.set_yticklabels(["$10^{}$".format(i) for i in range(9)])
cb.set_label("Anzahl der Transaktionen")
plt.savefig('hexbin1.png', dpi=1000) #, gc.collect())
