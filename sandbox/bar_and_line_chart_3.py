import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data
df_pilot_starlink = pd.read_csv('input_data/Starlink_Launch_Data.csv')
df_pilot_sightings = pd.read_csv('input_data/Pilot_sightings_per_Year.csv')

# Align Year columns if needed
df_combined = pd.merge(df_pilot_sightings, df_pilot_starlink, on='Year', how='outer')
print(df_combined.columns)

# Plot bar and line charts
fig, ax1 = plt.subplots(figsize=(10, 6))

sns.barplot(data=df_combined, x='Year', y='Pilot_Sightings_per_Year', ax=ax1, color='blue', zorder=2)
ax1.set_title('Pilot UFO Sightings & Starlink Satellites Launches per Year', fontdict={'fontsize': 18})
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('UFO Sightings', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
plt.xticks(rotation=90)

# Add secondary axis
ax2 = ax1.twinx()
ax2.plot(df_combined['Year'], df_combined['Satellites_Launched_per_Year'], color='red', marker='o', zorder=1)
ax2.set_ylabel('Satellites Launched', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Adjust layout
plt.tight_layout()
plt.show()
