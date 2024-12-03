import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dummy data
years = range(2000, 2021)
df_pilot_sightings = pd.DataFrame({'Year': years, 'Pilot_Sightings_per_Year': range(100, 121)})
df_pilot_starlink = pd.DataFrame({'Year': years, 'Satellites_Launched_per_Year': range(50, 71)})
print(df_pilot_sightings)
print(df_pilot_starlink)

# Plot a bar chart
fig, ax1 = plt.subplots(figsize=(10, 6))

sns.set_theme(style='darkgrid')
sns.barplot(data=df_pilot_sightings, x='Year', y='Pilot_Sightings_per_Year', ax=ax1, color='blue')
ax1.set_title('Pilot UFO Sightings per Year', fontdict={'fontsize': 18})
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('UFO Sightings', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
plt.xticks(rotation=90)

# Create secondary axis
ax2 = ax1.twinx()
ax2.plot(df_pilot_starlink['Year'], df_pilot_starlink['Satellites_Launched_per_Year'], color='red', marker='o')
ax2.set_ylabel('Satellites Launched', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Show the plot
plt.show()  
