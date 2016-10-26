# Make stacked bar plots with various combinations of roads
# Need to have run make_relative_csv.py before this to make the
# Exeter_city_only.csv csv

import matplotlib.pyplot as plt
import os
import pandas as pd

# read in all the data make a bar plot for each road
exeter_city = pd.read_csv("../data/Exeter_city_only.csv", header=0)

years = [2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007,
         2006, 2005, 2004, 2003, 2002, 2001, 2000]

for year in years:
    # select a year and make a barplot with the distribution of vehicles for each road.
    exeter_year = exeter_city[exeter_city["AADFYear"] == year]

    mode = ['PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches', 'LightGoodsVehicles',
            'AllHGVs']

    # make a dataframe of just the columns we want to stack in the bar plot
    exeter_year = exeter_year[["Road", "PedalCycles", "Motorcycles",
                               "CarsTaxis", "BusesCoaches", "LightGoodsVehicles", "AllHGVs"]]

    # prepare the dataframe for plotting
    exeter_year.set_index(exeter_year["Road"], inplace=True, drop=True)
    exeter_year.drop('Road', axis=1, inplace=True)

    ###### Group by Roads, All roads.

    # groupby road first
    exeter_ = exeter_year.groupby(exeter_year.index)
    data_group = exeter_.agg(['mean'])

    # Normalise across vehicle types for each road
    for m in mode:

        new_val_list = []
        for i in range(len(data_group)):
            new_val = data_group[m].iloc[i][0] / data_group.iloc[i].sum()  # sum across the row
            new_val_list.append(new_val)

        data_group[m + "%"] = new_val_list

        # extract just the columns we want for the bar plot
    data_group = data_group[["PedalCycles%", "Motorcycles%", "CarsTaxis%",
                             "BusesCoaches%", "LightGoodsVehicles%", "AllHGVs%"]]

    # Fix the column headers so the legend looks normal!
    data_group.columns = ["PedalCycles%", "Motorcycles%", "CarsTaxis%",
                          "BusesCoaches%", "LightGoodsVehicles%", "AllHGVs%"]

    data_group.plot.bar(stacked=True)

    plt.title('Road useage by vehicle type %s' % str(year))

    fig = plt.gcf()

    directory = "../plots/barplots/all_roads/relative/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    fig.savefig('../plots/barplots/all_roads/relative/Allroads_barplot%s_relative.png' % str(year))

    # Perhaps we just want to focus on the smaller roads in Exeter. Lets drop rows with M5 or 
    exeter_outer = exeter_year[(exeter_year.index == "M5") | (exeter_year.index == "A30")]
    exeter_inner = exeter_year[(exeter_year.index != "M5") & (exeter_year.index != "A30")]

    ########## Inner

    # groupby road first
    exeter_ = exeter_inner.groupby(exeter_inner.index)
    data_group = exeter_.agg(['mean'])

    # Normalise across vehicle types for each road
    for m in mode:

        new_val_list = []
        for i in range(len(data_group)):
            # data_group[m+"%"].iloc[i][0] =
            new_val = data_group[m].iloc[i][0] / data_group.iloc[i].sum()  # sum across the row
            new_val_list.append(new_val)

        data_group[m + "%"] = new_val_list

        # extract just the columns we want for the bar plot
    data_group = data_group[["PedalCycles%", "Motorcycles%", "CarsTaxis%", "BusesCoaches%",
                             "LightGoodsVehicles%", "AllHGVs%"]]

    # Fix the column headers so the legend looks normal!
    data_group.columns = ["PedalCycles%", "Motorcycles%", "CarsTaxis%",
                          "BusesCoaches%", "LightGoodsVehicles%", "AllHGVs%"]

    data_group.plot.bar(stacked=True)

    plt.title('Inner Road useage by vehicle type %s' % str(year))

    fig = plt.gcf()

    directory = "../plots/barplots/inner_roads/relative/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    fig.savefig('../plots/barplots/inner_roads/relative/inner_barplot%s_relative.png' % str(year))

    ########## Outer

    # groupby road first
    exeter_ = exeter_outer.groupby(exeter_outer.index)
    data_group = exeter_.agg(['mean'])

    # Normalise across vehicle types for each road
    for m in mode:

        new_val_list = []
        for i in range(len(data_group)):
            # data_group[m+"%"].iloc[i][0] =
            new_val = data_group[m].iloc[i][0] / data_group.iloc[i].sum()  # sum across the row
            new_val_list.append(new_val)

        data_group[m + "%"] = new_val_list

        # extract just the columns we want for the bar plot
    data_group = data_group[["PedalCycles%", "Motorcycles%", "CarsTaxis%", "BusesCoaches%",
                             "LightGoodsVehicles%", "AllHGVs%"]]

    # Fix the column headers so the legend looks normal!
    data_group.columns = ["PedalCycles%", "Motorcycles%", "CarsTaxis%",
                          "BusesCoaches%", "LightGoodsVehicles%", "AllHGVs%"]

    data_group.plot.bar(stacked=True)

    plt.title('Outer Road useage by vehicle type %s' % str(year))

    fig = plt.gcf()

    directory = "../plots/barplots/outer_roads/"
    if not os.path.exists(directory):
        os.makedirs(directory)
    fig.savefig('../plots/barplots/outer_roads/outer_barplot%s_relative.png' % str(year))
