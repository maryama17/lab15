"""
Lab15_mhasan6_1.py
Author: Maryama Hasan
Purpose: Read unemployment data from a CSV file and plot the rate over time using Matplotlib. 
Date: 2025-08-06
"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open('OHRU.csv', 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        print(f"Row {i}: {row}")
        if i == 1:  
            break


dates = []
rates = []

with open('OHRU.csv', 'r') as file:
    next(file) 
    for line in file:
        date_str, rate_str = line.strip().split(',')
        date = datetime.strptime(date_str, '%Y-%m-%d') 
        rate = float(rate_str)
        dates.append(date)
        rates.append(rate)


plt.figure(figsize=(10, 5))
plt.plot(dates, rates, color='blue', linewidth=2)
plt.title('US Unemployment Rate (1976 - Present)')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()
