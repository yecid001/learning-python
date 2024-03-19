import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the Pima Indians Diabetes dataset
df = pd.read_csv('pima-indians-diabetes.csv')

# Calculate the histogram data using numpy.histogram()
hist_data, bins = np.histogram(df['Glucose'], bins=np.arange(0, 201, 25))

# Plot the histogram bars using matplotlib.pyplot.bar()
plt.bar(bins[:-1], hist_data, width=25, color='blue')

# Add a line that connects the data points using matplotlib.pyplot.plot()
plt.plot(bins[:-1], hist_data, linestyle='-', color='red')

# Set the title and labels
plt.title('Glucose Histogram')
plt.xlabel('Glucose Value')
plt.ylabel('Number of People')

# Set the x-axis limits
plt.xlim(0, 200)

# Set the number of minor ticks on the x-axis
plt.xticks(np.arange(0, 201, 25))

# Set the grid to be visible
plt.grid(True)

# Show the histogram
plt.show()