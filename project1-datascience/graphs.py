# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Graphs for Hotdog Presentation
# By Andromeda Kepecs
# ATCS, F

# Read csv data
hotdog_eater_data = pd.read_csv('hotdogs.csv')

# Hotdogs per minute or rate of each eater 
def rate(df):
	# new column = number of hotdogs eaten divided by minutes
	rate = df['Rate (hot dogs / min)']

	# Populate bin list
	binlist = []
	width = 0.2 # Arbitrary number that can be set
	hist_max_x = math.ceil(rate.max())
	for i in range(0, int(hist_max_x/width)):
		binlist.append(i * width)

	# Plot
	plt.hist(rate, bins = binlist)
	plt.xlabel('Consumption Rate (hot dogs per min)')
	plt.show()



# Create graphs
rate(hotdog_eater_data)

