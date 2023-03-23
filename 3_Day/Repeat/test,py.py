import matplotlib.pyplot as plt

data = [5, 0, 4, 4, 4, 0, 0, 4, 5, 3, 4, 4, 5, 2, 0, 1, 2, 3, 3, 5, 2, 2, 1, 2, 4]

# Create a histogram with 6 bins (one for each possible value from 0 to 5)
plt.hist(data, bins=6, edgecolor='black')

# Add axis labels and a title
plt.xlabel('Graduation Year')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Graduation Years')

# Show the plot
plt.show()
