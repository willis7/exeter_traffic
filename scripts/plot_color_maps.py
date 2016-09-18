# This script creates the Coloured maps which simply compares total flow from all
# types of vehicles between roads. Different roads are distinguished by different colours.
import pandas as pd
import numpy as np
import seaborn as sns 
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


file_string = ['2014','_in2014','_out2014']
name_string_text = ['','inner','outer']

for i, name in enumerate(file_string):
    # import my normalised coordinate data
    road_coords = pd.read_csv("../data/road_coords_norm_vals%s.csv"%name, header = 0)

    mode = ["All"]
    colors = ['b','g','r','indianred','orange','purple','yellow','fuchsia']

    for i,m in enumerate(mode):
	
        fig = plt.figure(figsize=(8,8))

        map = Basemap(projection='merc', lat_0 = 57, lon_0 = -135,
                      resolution = 'h', area_thresh = 0.2,
                      llcrnrlon=-3.57, llcrnrlat=50.67,
                      urcrnrlon=-3.45, urcrnrlat=50.75)

        map.readshapefile('../data/roads', 'osm_roads')    

        map.drawcoastlines()
        map.drawcountries()
        map.fillcontinents(color = 'antiquewhite')
        map.drawmapboundary()

        for CP in road_coords["CP"].unique():

            lat = road_coords["Latitude"][road_coords["CP"] == CP].tolist()
            lon = road_coords["Longitude"][road_coords["CP"] == CP].tolist()
            x,y = map(lon, lat)

            markersize = road_coords[m+"%"][road_coords["CP"] == CP].tolist()[0]
	    
            colors = {'A379':'b','M5':'g','A377':'r',
                      'A376':'orange','A30':'purple','A3015':'yellow'}
	    
            markercolor = colors[road_coords["Road"][road_coords["CP"] == CP].tolist()[0]]

            map.plot(x, y, 'o', color = markercolor, markersize=markersize*200)

        plt.title('Relative AADF for %s%s'%(m,name_string_text[i]))    

        fig = plt.gcf()
        fig.savefig('../plots/maps/colorExeter_%s%s.png'%(m,name), dpi=150)