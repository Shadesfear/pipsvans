import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os


#liste over subdirs i pipsvans, men den returner også andre ting, så de skal sorteres fra
names = [x[1] for x in os.walk(os.getcwd())] # <-- This is not needed anymore! But im gonna keep it
#Only the subdirs we want
subdirs = [x[1] for x in os.walk(os.getcwd())][0][1:]

# laver et dictionary med keysets fra listen af strings 'subdirs'
df = dict.fromkeys(subdirs) 

#Reads all CSV files into the keyset.
for x in subdirs:
	df[x] = pd.read_csv(os.getcwd()+'/'+x+'/'+x+'_32.csv', header=None, skiprows=2, names=['time','A','B']) # mapper keyset til valueset


maxes = []
for x in subdirs:
	if df[x].empty:
		0
	else: 
		maxes.append(max(df[x].A[1:500]))

noise = float(max(np.asarray(maxes)))
		
signalA = df['tyve'].A[df['tyve'].A > noise*2]

for x in subdirs:
	j = df[x].A.values
	if j.dtype == object:
		pass#print('j.dtype')	
	print(j.dtype)


