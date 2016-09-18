# This script will plot a time series for each of the transport types
# named in the var transport and stored the output as a png in the /plots/tseries 
# folder


import pandas as pd
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

    plt.fill_between(data_group.index, (data_group['mean'] + data_group['std']), 
                 (data_group['mean'] - data_group['std']), color = 'b', alpha = 0.2) 
    
    # Annotate with the slope and confidence interval
    
    # to place the point half way up the page, take the maximum y value and /2
    plot_y_slope = (max(data_group['mean']) + max(data_group['std']))*0.9
    # to place the point half way up the page, take the maximum y value and /2
    plot_y_r = (max(data_group['mean']) + max(data_group['std']))*0.8
    # to place the point half way up the page, take the maximum y value and /2
    plot_y_conf = (max(data_group['mean']) + max(data_group['std']))*0.7
    
    
    
    print(f.summary)
     
    
    
    # Annotate with the slope and confidence interval
    #plt.text(2000,int(plot_y_slope),"slope = %s"%str(round(f.params[0],3)))
    plt.text(2000,int(plot_y_r),"$r^2$ = %s"%str(round(f.rsquared,3))) 
    plt.text(2000,int(plot_y_conf),"conf_int = %s - %s"%(str(round(f.conf_int()[0][0],3)), 
                                                         str(round(f.conf_int()[1][0],3))))
    fig = ax.get_figure()

    fig.savefig('../plots/tseries/%s_tseries.png'%transport_type)