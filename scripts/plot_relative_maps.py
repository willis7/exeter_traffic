## Script to make annotated maps of Exeter
## This should be run from exeter_traffic/scripts/
## make_relative_csv.py should be run before this to create the values to be plotted.

import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.basemap import Basemap

# Could also exchange the year to make all these plots for each year

# If you don't want to run all the years (will take a while) then alter this
# list
# years = ['2014','2013','2012','2011','2010','2009','2008','2007',
# '2006','2005','2004','2003','2002','2001','2000']
years = ['2014']

for year in years:
    # import my normalised coordinate data
    road_coords = pd.read_csv("../data/road_coords_norm_vals%s.csv" % year, header=0)

    # make a loop over each of the mode types
    mode = ['PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches', 'LightGoodsVehicles',
            'AllHGVs', 'AllMotorVehicles', 'All']
    colors = ['b', 'g', 'r', 'indianred', 'orange', 'purple', 'yellow', 'fuchsia']

    for i, m in enumerate(mode):
        fig = plt.figure(figsize=(8, 8))

        map = Basemap(projection='merc', lat_0=57, lon_0=-135,
                      resolution='h', area_thresh=0.2, llcrnrlon=-3.57, llcrnrlat=50.67,
                      urcrnrlon=-3.45, urcrnrlat=50.75)

        map.readshapefile('../data/roads', 'osm_roads')

        map.drawcoastlines()
        map.drawcountries()
        map.fillcontinents(color='antiquewhite')
        map.drawmapboundary()

        for CP in road_coords["CP"].unique():
            lat = road_coords["Latitude"][road_coords["CP"] == CP].tolist()
            lon = road_coords["Longitude"][road_coords["CP"] == CP].tolist()
            x, y = map(lon, lat)

            markersize = road_coords[m + "%"][road_coords["CP"] == CP].tolist()[0]

            map.plot(x, y, 'o', color=colors[i], markersize=markersize * 200)

        plt.title('Relative AADF for %s %s' % (m, year))

        fig = plt.gcf()

        fig.savefig('../plots/maps/%s/Exeter_%s%s.png' % (year, m, year), dpi=100)

        plt.clf()
