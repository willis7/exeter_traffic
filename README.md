# exeter_traffic
Exploring Estimated Average Daily Flows (AADFs)

Using [Jupyter Notebook](http://jupyter.org/) with the Anaconda (2.4.1) Python 3.5.

If you use these scripts I assume you have a local copy of `AADF_Devon_VehicleFlows.csv` and `Exeter_box.csv`. I can provide if needed. 

1) The first thing you need to do is run [notebooks/Exeter_area.ipynb](/notebooks/Exeter_area.ipynb) to create a subset of data for Exeter 
using AADF_Devon_VehicleFlows.csv


2) The second thing is [/scripts/make_relative_csv.py](/scripts/make_relative_csv.py) should be run next to create some more data subsets 
which the other scripts can pull from.   

Once you have run the two scripts above, you should be able to run any of the following scripts, and make adjustments as you want.
Bear in mind you might want to adjust the input/output folders in the following scripts. 

### Scripts
`plot_barplots.py`  - Makes 3 sets of barplots for each year: 1) Using all Roads, 2) Inner Roads (Excluding A30 and M5) 3) Outer Roads 
(just A30 and M5) . 

`plot_relative_maps.py`  - Makes makes for each Vehicle type for each year. Each map contains normalised values over the Exeter road 
network.

`plot_color_maps.py` - Only plots for 2014 at the moment. Makes a map with different colours for different roads and uses all traffic data.

`plot_timeseries.py` - plot a time series for each of the transport types

### Notebooks

All of the initially exploration and working is scattered across these.



