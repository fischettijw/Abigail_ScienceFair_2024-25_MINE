import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Bar Values': [10, 20, 15, 25],
    'Line Values': [100, 200, 150, 300]
})

# Create the plot
fig, ax1 = plt.subplots(figsize=(8, 6))

# Bar plot on the primary y-axis
sns.barplot(data=data, x='Category', y='Bar Values', ax=ax1, color='skyblue', alpha=0.7)
ax1.set_ylabel('Bar Values', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a secondary y-axis for the line plot
ax2 = ax1.twinx()
ax2.plot(data['Category'], data['Line Values'], color='red', marker='o', label='Line Values')
ax2.set_ylabel('Line Values', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add labels and title
ax1.set_title('Bar Chart with Line Chart Overlay')
ax1.set_xlabel('Category')

# Show the plot
plt.tight_layout()
plt.show()
