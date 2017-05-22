import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd

df = pd.read_csv('C:/Users/Morten/Documents/pipsvans/femfyrre/femfyrre_32.csv', header=None, skiprows=2, names=['time','A','B'])


noiseA = max(df.A[1:500])
noiseB = max(df.B[1:500])

plt.plot(df.time,df.B)

signalA = df.A[df.A > noiseA * 3]
signalB = df.B[df.B > noiseB * 4]
#signalAStartt = df.time[signalAstart[0,1]] 
signalAStart = signalA.index[0]
signalBStart = signalB.index[0]
signalATimeStart = df.time[signalAStart]
signalBTimeStart = df.time[signalBStart]
travelTime = signalATimeStart - signalBTimeStart

print(travelTime/1000*340)
#print(signalBTimeStart)
print(travelTime)
#print(signalA.index[0])
#print(signalATimeStart)


print(type(signalA))

plt.show()