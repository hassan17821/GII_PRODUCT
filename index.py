# KO-INDEX
import pdbufr
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap, LinearSegmentedColormap

# Read BUFR data
# (Assuming 'df' is already defined)
productKey = 'parcelLiftedIndexTo500Hpa'
productLabel = 'kO Index'

# Set latitude and longitude bounds
latBound = [7.22, 37.454]
lngBound = [43.753, 102.363]
ranges = [-16 , -8 , -4 , 0 , 10 , 20]
minMaxVal = [-16 , 20]
# Filter data based on latitude and longitude range
filtered_df = df[
    (df['latitude'] >= latBound[0])
    & (df['latitude'] <= latBound[1])
    & (df['longitude'] >= lngBound[0])
    & (df['longitude'] <= lngBound[1])
    & (df[productKey] >= minMaxVal[0])
    & (df[productKey] <= minMaxVal[1])
]

# Create the base map
fig = plt.figure(figsize=(16, 16))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]- 3.4])

# Add map features
ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.OCEAN, facecolor='lightblue')

brown_cmap = LinearSegmentedColormap.from_list('brown', ['#D2B48C', '#8B4513'], N=20)
purple_cmap = LinearSegmentedColormap.from_list('blue', ['#A0A0E6', '#524788'], N=4)
yellow_cmap = LinearSegmentedColormap.from_list('green', ['#F0EB9F', '#A09D12'], N=4)
red_cmap = LinearSegmentedColormap.from_list('red', ['#6C0000', '#FC8282'], N=8)

# Combine the custom colormaps into one
combined_cmap = ListedColormap(np.concatenate([
    red_cmap(np.linspace(0, 1, 8)),
    yellow_cmap(np.linspace(0, 1, 4)),
    purple_cmap(np.linspace(0, 1, 4)),
    brown_cmap(np.linspace(0, 1, 20)),
]))

# Define color ranges and corresponding normalization values
norm = Normalize(vmin=minMaxVal[0], vmax=minMaxVal[1])

# Plot the KIndex with the combined custom colormap
sc = ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df[productKey],
                cmap=combined_cmap, transform=ccrs.PlateCarree(), s=1, norm=norm)

# Add a colorbar with fixed ticks and labels
cbar = plt.colorbar(sc, ticks=ranges, orientation='horizontal')
cbar.set_label(productLabel)

# Add a title
plt.title(productLabel + ' Plot')

plt.show()
