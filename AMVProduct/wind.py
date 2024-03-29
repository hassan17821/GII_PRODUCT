import pdbufr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import Normalize, ListedColormap

def plot_upperLevelWind(outputPath ,df):
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]

    ## [@UPPER_LEVEL]
    minMaxVal = [10000 , 50000]
    pressure_brackets = [
        (10000, 25000),
        (25100, 35000),
        (35100, 50000)
    ]

    ## [@LOWER_LEVEL]
    # minMaxVal = [40000 , 95000]
    # pressure_brackets = [
    #     (40000, 59900),
    #     (60000, 79900),
    #     (80000, 95000)
    # ]

    filtered_df = df[
        (df['#1#latitude'] >= latBound[0])
        & (df['#1#latitude'] <= latBound[1])
        & (df['#1#longitude'] >= lngBound[0])
        & (df['#1#longitude'] <= lngBound[1])
        & (df['#1#pressure'] >= minMaxVal[0])
        & (df['#1#pressure'] <= minMaxVal[1])
    ].copy() 

    pressure_labels = ['red', 'green', 'blue']

    filtered_df['#1#pressureColor'] = np.select(
        [((filtered_df['#1#pressure'] >= low) & (filtered_df['#1#pressure'] <= high)) for low, high in pressure_brackets],
        pressure_labels, default='black'
    )

    # ======== WIND VECTOR CALCULATION IF NECESSARY ======== 
    # windu = -df['#1#windSpeed'] * np.sin(np.radians(df['#1#windDirection']))
    # windv = -df['#1#windSpeed'] * np.cos(np.radians(df['#1#windDirection']))

    # Create a cartopy map with PlateCarree projection
    # print(filtered_df['#1#windSpeed'])
    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())

    # ======== PRESSURE BAR COLORS ======== 
    # cmap = ListedColormap(pressure_labels)
    # norm = plt.Normalize(minMaxVal[0], minMaxVal[1])
    # sm = ScalarMappable(cmap=cmap, norm=norm)
    # sm.set_array([])
    # cbar = plt.colorbar(sm, ax=ax, label='Pressure')


    # Plot wind barbs with different colors based on pressure brackets
    # barbs = ax.barbs(filtered_df['#1#longitude'], filtered_df['#1#latitude'], filtered_df['#1#u'] ,filtered_df['#1#v'], color=filtered_df['#1#pressureColor'], pivot='middle', transform=ccrs.PlateCarree())
    barbs = ax.barbs(filtered_df['#1#longitude'],
                    filtered_df['#1#latitude'],
                    filtered_df['#1#u'],
                    filtered_df['#1#v'],
                    color=filtered_df['#1#pressureColor'],
                    transform=ccrs.PlateCarree(),
                    length=5,
                    linewidth=0.75)
    # ======== ADD COASTLINE AND OTHER FEATURES ======== 
    # ax.coastlines()
    # ax.add_feature(cfeature.BORDERS, linestyle=':')
    # ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
    # plt.show()
    fig.patch.set_alpha(0)
    fig.savefig(outputPath, transparent=True, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

def plot_lowerLevelWind(outputPath,df):
    latBound = [7.22, 37.454]
    lngBound = [43.753, 102.363]

    ## [@UPPER_LEVEL]
    # minMaxVal = [10000 , 50000]
    # pressure_brackets = [
    #     (10000, 25000),
    #     (25100, 35000),
    #     (35100, 50000)
    # ]

    ## [@LOWER_LEVEL]
    minMaxVal = [40000 , 95000]
    pressure_brackets = [
        (40000, 59900),
        (60000, 79900),
        (80000, 95000)
    ]

    filtered_df = df[
        (df['#1#latitude'] >= latBound[0])
        & (df['#1#latitude'] <= latBound[1])
        & (df['#1#longitude'] >= lngBound[0])
        & (df['#1#longitude'] <= lngBound[1])
        & (df['#1#pressure'] >= minMaxVal[0])
        & (df['#1#pressure'] <= minMaxVal[1])
    ].copy() 

    pressure_labels = ['red', 'green', 'blue']

    filtered_df['#1#pressureColor'] = np.select(
        [((filtered_df['#1#pressure'] >= low) & (filtered_df['#1#pressure'] <= high)) for low, high in pressure_brackets],
        pressure_labels, default='black'
    )

    # ======== WIND VECTOR CALCULATION IF NECESSARY ======== 
    # windu = -df['#1#windSpeed'] * np.sin(np.radians(df['#1#windDirection']))
    # windv = -df['#1#windSpeed'] * np.cos(np.radians(df['#1#windDirection']))

    # Create a cartopy map with PlateCarree projection
    # print(filtered_df['#1#windSpeed'])
    fig = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_extent([lngBound[0], lngBound[1], latBound[0], latBound[1]], crs=ccrs.PlateCarree())

    # ======== PRESSURE BAR COLORS ======== 
    # cmap = ListedColormap(pressure_labels)
    # norm = plt.Normalize(minMaxVal[0], minMaxVal[1])
    # sm = ScalarMappable(cmap=cmap, norm=norm)
    # sm.set_array([])
    # cbar = plt.colorbar(sm, ax=ax, label='Pressure')


    # Plot wind barbs with different colors based on pressure brackets
    # barbs = ax.barbs(filtered_df['#1#longitude'], filtered_df['#1#latitude'], filtered_df['#1#u'] ,filtered_df['#1#v'], color=filtered_df['#1#pressureColor'], pivot='middle', transform=ccrs.PlateCarree())
    barbs = ax.barbs(filtered_df['#1#longitude'],
                    filtered_df['#1#latitude'],
                    filtered_df['#1#u'],
                    filtered_df['#1#v'],
                    color=filtered_df['#1#pressureColor'],
                    transform=ccrs.PlateCarree(),
                    length=5,
                    linewidth=0.75)
    # ======== ADD COASTLINE AND OTHER FEATURES ======== 
    # ax.coastlines()
    # ax.add_feature(cfeature.BORDERS, linestyle=':')
    # ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='lightgray')
    # plt.show()
    fig.patch.set_alpha(0)
    fig.savefig(outputPath, transparent=True, format='webp', dpi=300, bbox_inches='tight', pad_inches=0)

export = plot_upperLevelWind, plot_lowerLevelWind