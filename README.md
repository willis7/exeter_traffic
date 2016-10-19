# Road use in Exeter

Exploring Estimated Average Daily Flows (AADFs) in Exeter with data from 2000 - 2014.

**Before you start**

Create the environment for exeter_traffic:

Inside exeter_traffic:
conda env create -f environment.yml

Run [make_relative_csv.py](/scripts/make_relative_csv.py) to create some more data subsets
which the other scripts can pull from.   The scripts need to be run from
within the scripts folder.

Once you have done the above you should be able to run any of the following scripts, and make adjustments (focusing on
different years for example). You should also adjust the input/output folders in the following scripts. 

### Scripts
`plot_barplots.py`  - Makes 3 sets of barplots for each year: 1) Using all Roads, 2) Inner Roads (Excluding A30 and M5) 3) Outer Roads 
(just A30 and M5). 

`plot_relative_maps.py`  - Makes maps for each Vehicle type for each year. Each map contains normalised values over the Exeter road 
network.

`plot_color_maps.py` - Only plots for 2014 at the moment. Makes a map with different colours for different roads and uses all traffic data.

`plot_timeseries.py` - plot a time series for each of the transport types

