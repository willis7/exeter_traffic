# Make stacked bar plots with various combinations of roads
# Need to have run make_relative_csv.py before this to make the
# Exeter_city_only.csv csv

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# read in all the data make a bar plot for each road
exeter_city = pd.read_csv("../data/Exeter_city_only.csv", header = 0)


years = [2014,2013,2012,2011,2010,2009,2008,2007,
2006,2005,2004,2003,2002,2001,2000]


for year in years:
    # select a year and make a barplot with the distribution of vehicles for each road.
    exeter_year = exeter_city[exeter_city["AADFYear"] == year]
    
    mode = ['PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches', 'LightGoodsVehicles', 
           'AllHGVs', 'AllMotorVehicles']
    
        
    # make a dataframe of just the columns we want to stack in the bar plot
    exeter_year = exeter_year[["Road","PedalCycles","Motorcycles",
                              "CarsTaxis","BusesCoaches","LightGoodsVehicles", "AllHGVs"]]
    
    # prepare the dataframe for plotting
    exeter_year.set_index(exeter_year["Road"], inplace = True, drop = True)
    exeter_year.drop('Road', axis=1, inplace=True)
    
    exeter_year.plot.bar(stacked = True)
    
    plt.title('Road useage by vehicle type (CPs) %s'%str(year))
    
    fig = plt.gcf()

    fig.savefig('../plots/barplots/all_roads/eachCP_%s.png'%str(year))

    # Perhaps we just want to focus on the smaller roads in Exeter. Lets drop rows with M5 or 
    exeter_outer = exeter_year[(exeter_year.index == "M5") | (exeter_year.index == "A30")]
    exeter_inner = exeter_year[(exeter_year.index != "M5") & (exeter_year.index != "A30")]
    
    # group by road
    # Inner
    group_inner = exeter_inner.groupby(exeter_inner.index).mean()
    
    group_inner.plot.bar(stacked = True)
    
    plt.title('Inner Road useage by vehicle type %s'%str(year))
    
    fig = plt.gcf()
    fig.savefig('../plots/barplots/inner_roads/inner_barplot%s.png'%str(year))
    
    # Outer
    group_outer = exeter_outer.groupby(exeter_outer.index).mean()
    
    group_outer.plot.bar(stacked = True)
    
    plt.title('Outer Road useage by vehicle type %s' %str(year))
    
    fig = plt.gcf()
    fig.savefig('../plots/barplots/outer_roads/outer_barplot%s.png'%str(year))
    
    # Group all roads
    group_year = exeter_year.groupby(exeter_year.index).mean()
    
    group_year.plot.bar(stacked = True)
    plt.title('All Road useage by vehicle type %s' %str(year))
    fig = plt.gcf()
    fig.savefig('../plots/barplots/all_roads/each_road_barplot%s.png'%str(year))
    
    # Make a plot normalised over each road. 
   
    
    
    
    
    
    
    