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

# Hotdogs eaten frequency graph
def eaten(df):
	eaten = df['Number of Hot Dogs']

	# Populate bin list
	binlist = []
	width = 2
	hist_max_x = math.ceil(eaten.max())
	for i in range(0, int(hist_max_x/width)):
		binlist.append(i * width)

	# Plot
	plt.hist(eaten, bins = binlist)
	plt.xlabel('Number of hot dogs eaten')
	plt.show()

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

# Return a new column that only has the number of hot dogs eaten by F or M sexes
def eaten(df, sex):
	new = []
	hotdogs_eaten = df['Number of Hot Dogs']
	for i in range(len(hotdogs_eaten)):
		if df['Sex'][i] == sex:
			new.append(hotdogs_eaten[i])
	return new

# Create new list of rates, separated by sex
def rate_by_sex(df, sex):
	new = []
	rate = df['Rate (hot dogs / min)']
	for i in range(len(rate)):
		if df['Sex'][i] == sex:
			new.append(rate[i])
	return new

# Female rate hist plot
def rate_f(l):
	# Populate bin list
	binlist = []
	width = 0.15 # Arbitrary number that can be set
	hist_max_x = math.ceil(max(l))
	for i in range(0, int(hist_max_x/width)):
		binlist.append(i * width)

	# Plot
	plt.hist(l, bins = binlist)
	plt.xlabel('Consumption Rate of Female Competitors (hot dogs/min)')
	plt.show()

# Male rate hist plot
def rate_m(l):
	# Populate bin list
	binlist = []
	width = 0.2 # Arbitrary number that can be set
	hist_max_x = math.ceil(max(l))
	for i in range(0, int(hist_max_x/width)):
		binlist.append(i * width)

	# Plot
	plt.hist(l, bins = binlist)
	plt.xlabel('Consumption Rate of Male Competitors (hot dogs/min)')
	plt.show()


rate_f(rate_by_sex(hotdog_eater_data, 'F'))

rate_m(rate_by_sex(hotdog_eater_data, 'M')) 


# Num hot dogs eaten by competitors, separated by sex
eaten_by_women = eaten(hotdog_eater_data, 'F')
eaten_by_men = eaten(hotdog_eater_data, 'M')

max_f = max(eaten_by_women)
max_m = max(eaten_by_men)

print(max_f)
print(max_m)

# Create graphs
# eaten(hotdog_eater_data)
# rate(hotdog_eater_data)



