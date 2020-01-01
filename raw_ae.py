import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

df_vib_ae = pd.read_csv('C:\\Users\\tye02\\Desktop\\Serial com\\Startstop AE\\20170524_12\\20170524_12_00_00_vibration.csv')
sig_start = 2000
sig_end = 4000

# AnyEscalator sensor
vib_vertical_full_ae = df_vib_ae['GBVibVertical'] - np.average(df_vib_ae['GBVibVertical'])
vib_vertical_ae = df_vib_ae['GBVibVertical'].iloc[sig_start:sig_end] - np.average(df_vib_ae['GBVibVertical'].iloc[sig_start:sig_end])
vib_lateral_ae = df_vib_ae['GBVibLateral'].iloc[sig_start:sig_end] - np.average(df_vib_ae['GBVibLateral'].iloc[sig_start:sig_end])
vib_stepband_ae = df_vib_ae['GBVibForward'].iloc[sig_start:sig_end] - np.average(df_vib_ae['GBVibForward'].iloc[sig_start:sig_end])
t_ae = np.array(df_vib_ae['TimeStamp'].iloc[sig_start:sig_end])

avgvertical = np.average(df_vib_ae['GBVibVertical'])
print(avgvertical)