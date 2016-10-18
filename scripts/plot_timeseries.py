# This script will plot a time series for each of the transport types
# named in the var transport and stored the output as a png in the /plots/tseries 
# folder


import pandas as pd
import os
import numpy as np
import seaborn as sns 
import statsmodels.api as sm
import matplotlib.pyplot as plt

# import just the Exeter data
exeter_data = pd.read_csv("../data/Exeter_city_only.csv", header = 0)

transport = ["PedalCycles","Motorcycles","CarsTaxis","BusesCoaches","LightGoodsVehicles","AllHGVs", 
"AllMotorVehicles"]

for transport_type in transport:
    
    
    group = exeter_data.groupby(['AADFYear'])
      
    data_group = group[transport_type].agg(['mean','std'])
    
    print(group[transport_type])
    
    # fit a regression line
    model = sm.OLS(data_group["mean"],sm.add_constant(exeter_data["AADFYear"].unique()))

    f = model.fit()
    
    # Plot the data
    
    plt.figure()
    
    ax = sns.tsplot(data=data_group['mean'], time = data_group.index)

    ax.set(ylabel="Mean AAHD", title = "Mean flow of %s in Exeter City Roads" %transport_type)
    
    plt.plot(f.fittedvalues,'--')

    # Annotate with the slope and confidence interval
    
    # to place the point half way up the page, take the maximum y value and /2
    plot_y_slope = (max(data_group['mean']))*0.98
    # to place the point half way up the page, take the maximum y value and /2
    plot_y_r = (max(data_group['mean']))*0.88
    # to place the point half way up the page, take the maximum y value and /2
    plot_y_conf = (max(data_group['mean']))*0.8

    print(f.summary)


    # Annotate with the slope and confidence interval
    plt.text(0,0.8, "$r^2$ = %s" % str(round(f.rsquared, 3)), transform = ax.transAxes, verticalalignment = 'center' )

    fig = ax.get_figure()
    
    directory = "../plots/tseries"
    if not os.path.exists(directory):
        os.makedirs(directory)

    fig.savefig('../plots/tseries/%s_tseries.png'%transport_type)