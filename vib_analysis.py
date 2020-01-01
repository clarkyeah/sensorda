import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

# measured signal on the gearbox
df_vib = pd.read_csv('C:\\Users\\tye02\Desktop\\Serial com\\StartStop\\ReceivedTofile-COM3-2019_12_18_16-36-12_2.DAT',sep = '\:+|\,', header=None)
df_vib_ae = pd.read_csv('C:\\Users\\tye02\Desktop\\Serial com\\Startstop AE\\20170524_12\\20170524_12_00_00_vibration.csv')

# measured signal on the main bearing
# df_vib = pd.read_csv('C:\\Users\\tye02\\Desktop\\Serial com\\Main Bearing\\ReceivedTofile-COM3-2019_12_18_16-36-12.DAT',sep = '\:+|\,', header=None)
# df_vib_ae = pd.read_csv('C:\\Users\\tye02\\Desktop\\Serial com\\Main Bearing AE\\20170524_12_00_00_vibration.csv')

sig_start = 2000
sig_end = 4000

# AnyEscalator sensor
vib_vertical_full_ae = df_vib_ae['GBVibVertical']# - np.average(df_vib_ae['GBVibVertical'])
vib_vertical_ae = df_vib_ae['GBVibVertical'].iloc[sig_start:sig_end] - np.average(df_vib_ae['GBVibVertical'].iloc[sig_start:sig_end])
vib_lateral_ae = df_vib_ae['GBVibLateral'].iloc[sig_start:sig_end] - np.average(df_vib_ae['GBVibLateral'].iloc[sig_start:sig_end])
vib_stepband_ae = df_vib_ae['GBVibForward'].iloc[sig_start:sig_end] - np.average(df_vib_ae['GBVibForward'].iloc[sig_start:sig_end])
t_ae = np.array(df_vib_ae['TimeStamp'].iloc[sig_start:sig_end])

# SmartMesh sensor
sig_start = 2000
sig_end = 4000

vib_vertical_full = df_vib[1] - np.average(df_vib[1])
vib_vertical = df_vib[1].iloc[sig_start:sig_end] - np.average(df_vib[1].iloc[sig_start:sig_end])
vib_lateral = df_vib[2].iloc[sig_start:sig_end] - np.average(df_vib[2].iloc[sig_start:sig_end])
vib_stepband = df_vib[3].iloc[sig_start:sig_end] - np.average(df_vib[3].iloc[sig_start:sig_end])
t = np.array(df_vib[0].iloc[sig_start:sig_end])

fig  = plt.figure()
ax1 = fig.add_subplot(3,2,1)
plt.plot(vib_vertical_full)

ax2 = fig.add_subplot(3,2,2)
plt.plot(vib_vertical_full_ae)

ax3 = fig.add_subplot(3,2,3)
plt.plot(t, vib_stepband)

ax4 = fig.add_subplot(3,2,4)
plt.plot(t, vib_vertical_ae)

timelen = np.size(t)
timelen_ae = np.size(t_ae)

Mvib = np.fft.fft(vib_stepband)
Mvib = np.abs(Mvib)/timelen * 2
Fs = 1000 / (t[1] - t[0])
f = np.arange(0, timelen) * Fs / timelen

Mvib_ae = np.fft.fft(vib_stepband_ae)
Mvib_ae = np.abs(Mvib_ae)/timelen_ae * 2
Fs_ae = 200
f_ae = np.arange(0, timelen_ae) * Fs / timelen_ae

ax5 = fig.add_subplot(3,2,5)
plt.plot(f[0:int(timelen/2.0)], Mvib[0:int(timelen/2.0)])

ax6 = fig.add_subplot(3,2,6)
plt.plot(f_ae[0:int(timelen_ae/2.0)], Mvib_ae[0:int(timelen_ae/2.0)])
fig.show()



