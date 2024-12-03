import matplotlib.pyplot as plt

# Data
Year = ['2010', '2011', '2012', '2013','2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']
Satellites = [0,0,0,0,0,0,0,0,2,120,833,989,1722,1984,1671]
Sightings = [1,1,1,2,1,1,0,0,0,0,1,4,7,65,103]

# Create figure and primary axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart on the left y-axis
ax1.bar(Year, Satellites, color='blue', label='Bar Data')
ax1.set_xlabel('Year')
ax1.set_ylabel('UFO Sightings per Year', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Secondary y-axis for the line chart on right
ax2 = ax1.twinx()
ax2.plot(Year, Satellites, color='orange', marker='o', label='Line Data')
ax2.set_ylabel('Starlink Satellites Launchedper Year', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Adding a title
plt.title('UFO Sightings & Starlink Satellites Launched per Year', fontdict={'fontsize': 18})
# plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()
