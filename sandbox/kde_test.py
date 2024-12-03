import seaborn as sns
import matplotlib.pyplot as plt

# Sample data: Heights of students
heights = [150, 155, 160, 162, 165, 167, 170, 172, 175, 178, 180, 182, 185, 190]

# Create the KDE plot
sns.kdeplot(heights, fill=True, gridsize = 800)

# Label the axes
plt.xlabel('Height (cm)')
plt.ylabel('Density')

# Show the plot
plt.show()
