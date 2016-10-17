## This script makes a csv file with the data needed to
# make plots in plot_relative_maps.py

# You need to run
import os
import pandas as pd
import numpy as np
import seaborn as sns 
import statsmodels.api as sm
import matplotlib.pyplot as plt


# check to see if we have Exeter_city_only.csv already
# if not, create it
path = "../data/Exeter_city_only.csv"
if os.path.isfile(path) == False:

    # data is in the data directory.
    data = pd.read_csv("../data/AADF_Devon_VehicleFlows.csv", header = 0)

    # I used http://www.gridreferencefinder.com/ to get these coordinates. I manually drew a box and 
    # made pointers for the 
    # four corners of the box
    exeter_coords = pd.read_csv("../data/Exeter_box.csv", header = 0)

    max_east = max(exeter_coords["Easting"])
    max_north = max(exeter_coords["Northing"])
    min_east = min(exeter_coords["Easting"])
    min_north = min(exeter_coords["Northing"])

    # extracting data just for Exeter using the max and min coordinates above.
    exeter_data = data[(data["Easting"] > min_east) & (data["Easting"] < max_east) & (data["Northing"] 
    > min_north) & (data["Northing"] < max_north) ]

    # Save data_exeter for future use
    exeter_data.to_csv("../data/Exeter_city_only.csv", index=False)

else: # read in the already created file
    exeter_data = pd.read_csv("../data/Exeter_city_only.csv", header = 0)  

# We want to make a seperate file for each year. Store the years in a list to 
# loop over
years = exeter_data["AADFYear"].unique()

for year in years:
  
    # extract data for 2014
    exeter_year = exeter_data[["AADFYear","CP","PedalCycles","Motorcycles",
    "CarsTaxis","BusesCoaches","LightGoodsVehicles","AllHGVs",
    "AllMotorVehicles"]][exeter_data["AADFYear"] == year]

    # Add a column which is all traffic for each point
    exeter_year["All"] = exeter_year["PedalCycles"] + exeter_year["AllMotorVehicles"]

    mode = ['PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches', 
    'LightGoodsVehicles','AllHGVs',   'AllMotorVehicles','All']

    # add a new column with the % of AADF relative to the other Exeter roads
    for m in mode:
       
       exeter_year[m+"%"] = exeter_year[m]/exeter_year[m].sum()
       
     
    # import the mapping data from road_coords.csv
    road_coords = pd.read_csv("../data/road_coords.csv", header = 0)

    # Loop over the unique CP values in exeter_2014 and insert an extra column to 
    # the road_coords with the % values for each of the road categories
    
    for m in mode:
        # set new column to 0 initially
        road_coords[m+"%"] = 0
        
        for CP in exeter_year["CP"]:       
            n = len(road_coords[road_coords["CP"] == CP]) 
            road_coords[m+"%"][road_coords["CP"] == CP] = exeter_year[m+"%"][exeter_year["CP"] == \
            CP].tolist() * n

    # Save the new dataframe of points for later use
    road_coords.to_csv('../data/road_coords_norm_vals%s.csv'%str(year), index = False)
  

    
    