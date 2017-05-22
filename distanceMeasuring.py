import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os

#df = pd.read_csv('C:/Users/Morten/Documents/pipsvans/femfyrre/femfyrre_32.csv', header=None, skiprows=2, names=['time','A','B'])
names = [x[1] for x in os.walk('C:/Users/Morten/Documents/pipsvans')] #liste over subdirs i pipsvans, men den returner også andre ting, så de skal sorteres fra
subdirs = names[0][1:]
df = dict.fromkeys(subdirs) # laver et dictionary med keysets fra listen af strings 'subdirs'
for x in subdirs:
	df[x] = pd.read_csv('C:/Users/Morten/Documents/pipsvans/'+x+'/'+x+'_32.csv', header=None, skiprows=2, names=['time','A','B']) # mapper keyset til valueset

	#df = pd.read_csv('C:/Users/Morten/Documents/pipsvans/femfyrre/femfyrre_32.csv', header=None, skiprows=2, names=['time','A','B'])
	#df = pd.read_csv('C:/Users/Morten/Documents/pipsvans/femfyrre/femfyrre_32.csv', header=None, skiprows=2, names=['time','A','B'])


#noiseA = max(df.A[1:500]) 
#noiseB = max(df.B[1:500])

#plt.plot(df.time,df.B)

#signalA = df.A[df.A > noiseA * 3]
#signalB = df.B[df.B > noiseB * 4]
#signalAStartt = df.time[signalAstart[0,1]] 
#signalAStart = signalA.index[0]
#signalBStart = signalB.index[0]
#signalATimeStart = df.time[signalAStart]
#signalBTimeStart = df.time[signalBStart]
#travelTime = signalATimeStart - signalBTimeStart
#print(subdirs)
print(df['femfyrre'])

#print(travelTime/1000*340)
#print(signalBTimeStart)
#print(travelTime)
#print(signalA.index[0])
#print(signalATimeStart)


#print(os.walk('C:/Users/Morten/Documents/pipsvans'))
#print(type(signalA))


plt.show()