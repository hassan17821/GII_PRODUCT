# GII - K-Index
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Read BUFR data
productKey = 'kIndex'
# Filter data based on latitude and longitude range
filterd_df = df[
    (df['latitude'] >= 20)
     & (df['latitude'] <= 40)
     & (df['longitude'] >= 50)
     & (df['longitude'] <= 90)
     & (df[productKey] >= -30)
     & (df[productKey] <= 36)
]

print(filterd_df)
# Create the base map
fig = plt.figure(figsize=(16, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([50, 90, 20, 40])

# Add map features
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

# Plot the KIndex
sc = ax.scatter(filterd_df['longitude'], filterd_df['latitude'], c=filterd_df[productKey], cmap='RdBu', transform=ccrs.PlateCarree(), s=1)

# Add a colorbar
cbar = plt.colorbar(sc)
cbar.set_label('K-Index')

# Add a title
plt.title('K-Index Plot')

# Show the plot
plt.show()
