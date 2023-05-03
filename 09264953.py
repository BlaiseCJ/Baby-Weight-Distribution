# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:02:55 2023

@author: Blaise Ezeokeke
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
"""
Importing modules and libraries:
    The csv module is to access its csv.reader() function
    Numpy is for data arrays
    Pyplot module of the Matplotlib library is for ploting the graph
"""

# Function to read the data3.csv file and returing the date as an array

def read_data_file(file_name):
    """
    Reading data from a CSV file and returning as a NumPy array.

    Args:
        file_name (str): Name of the CSV file.

    Returns:
        np.ndarray: Data array read from the CSV file.
    """
    data = []
    with open(file_name, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            data.append(float(row[0]))
    return np.array(data)


# Inputing the data3.csv file, using weights as variable

data_array = read_data_file('data3.csv')

# Printing the array
print(data_array)

# Calculating the average weight of babies 

average_weight = np.mean(data_array)

# Printing the average weight (W̃)
print(average_weight)



# Calculating X, the fraction of babies weighing between 0.85(W̃) and (W̃)
fraction = np.mean((data_array >= 0.85 * average_weight) & \
                   (data_array <= average_weight))

# Printing the value of X
print(fraction)


# Ploting the histogram
plt.hist(data_array, bins=10, edgecolor='black', alpha=0.9, label='Newborn Weights(Kg)')

# Adding vertical lines for average weight (W̃) and X coloring
plt.axvline(average_weight, color='black', linestyle='--', linewidth=1.5,\
            label=f'Average Weight (W̃) = {average_weight:.2f}')
plt.axvspan(0.85 * average_weight, average_weight, alpha=0.5, color='red',\
            label=f'X (0.85W̃ to W̃) = {fraction:.2f}')


# Setting labels, title and legend
plt.xlabel('Weight (Kg)')
plt.ylabel('Frequency (%)')
plt.title('Weights of Newborns in Europe')
plt.legend()

# Displaying the plot
plt.show()
