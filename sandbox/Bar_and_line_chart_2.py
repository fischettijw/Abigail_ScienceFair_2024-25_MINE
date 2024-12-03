import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the data
df_pilot_starlink = pd.read_csv('input_data/Starlink_Launch_Data.csv')
df_pilot_sightings = pd.read_csv('input_data/Pilot_sightings_per_Year.csv')
print(df_pilot_starlink.columns)
print(df_pilot_sightings.columns)

# Plot a bar chart
fig, ax1 = plt.subplots(figsize=(10, 6))

sns.set_theme(style='darkgrid')
# sns.barplot(df_pilot_sightings, x='Year', y='Pilot_Sightings_per_Year', ax=ax1, color='blue')
sns.barplot(data=df_pilot_sightings, x='Year', y='Pilot_Sightings_per_Year', ax=ax1, color='skyblue', alpha=0.7)            

ax1.set_title('Pilot UFO Sightings & Starlink Satellites Launches per Year', fontdict={'fontsize': 18})
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
plt.tight_layout()
plt.show()
