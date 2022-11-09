# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:37:29 2022
Edited on Thu Nov 3 15:01:00 2022

This script creates plots for case study 2 in:
    "TALKS: A systematic process for resolving model-data discrepancies"
    Maria Vilas et al. (2022)

@author: Felix Egger
"""

# Library import and constants
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# Flow unit
UNIT = 'ML d$^{-1}$'
# width of the bars in the bar plot
WIDTH = 0.35
# Step to set ticks on the x-axis on the figure
STEP = 7

# %% Adjust the figure
# Set font parameters for the plot
rc('text', usetex=False)
rc('font', **{'family': 'sans-serif', 'sans-serif': 'Arial'})
rc('font', size=20)
rc('xtick', labelsize=20)
rc('ytick', labelsize=20)
rc('lines', linewidth=2, mew=3)

COLORS = ('orange', 'darkblue', 'firebrick', 'lightcoral', 'darkblue',
          'cornflowerblue', 'mediumpurple', 'violet', 'darkgrey', 'dimgrey',
          'silver', 'slategrey', 'gainsboro', 'moccasin', 'blue', 'cornflowerblue', 'skyblue', 'lightgrey', 'whitesmoke', 'white')


# %% Load data for case study 2

# Load the data and convert to daily flow
data_cs2 = pd.read_csv('data_case_study_2.csv',
                       names=['observed', 'modeled'],
                       index_col=0,
                       skiprows=1)/365
# Get the observed and modeled data
flow_observed = data_cs2['observed']
flow_modeled = data_cs2['modeled']

# Generate the x-axis from the index of data_cs2
x = np.arange(len(data_cs2))
x_label = data_cs2.index


# %% Plot the differences Case study 2

fig, ax = plt.subplots(figsize=(14, 7), tight_layout=True)
# Create grey shading for the time discrepancies were found after the year 2000
ax.axvspan(29-WIDTH*1.5, 47, color=COLORS[8], alpha=0.4, lw=0)
ax.axhline(0, color='black', lw=0.8)
ax.bar(x, flow_modeled-flow_observed, WIDTH+0.4, color=COLORS[0],
       label='Observed-Modeled', edgecolor='black')
ax.set_xlabel('Year')
ax.set_ylabel(f'Modelled minus observed flow ({UNIT})')
ax.set_xticks(x[1::STEP], x_label[1::STEP])
fig.savefig('FIG2.png')

# %% Data analysis case study 2

# Get the data before discrepancies were found in 2000/2001
before = data_cs2[data_cs2.index < '2000/2001']
# Get the data after discrepancies were found in 2000/2001
after = data_cs2[data_cs2.index >= '2000/2001']

# Calculate and print the mean variation before  and after the 2000
print('Discrepancy before 2000: '
      f'{round((1-before.mean()[0]/before.mean()[1])*100,0)} %')
print('Discrepancy before 2000: '
      f'{round((1-after.mean()[0]/after.mean()[1])*100,0)} %')
