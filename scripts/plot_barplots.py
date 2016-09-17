# Make stacked bar plots with various combinations of roads
# Need to have run make_relative_csv.py before this to make the
# Exeter_city_only.csv csv

import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

# read in all the data make a bar plot for each road
exeter_city = pd.read_csv("../data/Exeter_city_only.csv", header = 0)

years = ['2014','2013','2012','2011','2010','2009','2008','2007',
'2006','2005','2004','2003','2002','2001','2000']


for year in years:
    # select a year and make a barplot with the distribution of vehicles for each road.
    exeter_year = exeter_city[exeter_city["AADFYear"] == 2014]