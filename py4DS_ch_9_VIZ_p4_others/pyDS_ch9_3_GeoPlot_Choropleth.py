
################# 12.1: full, 12.2: 5.40
# copy:
#        
#        
################# (09-Feb-25 for 11-Feb-25)

# Courses: PrTla PY for DS & ML >    12.1, 12.2, 12.3, 12.4, 12.5


# ----------------    Geographical Plotting    ----------------
# more: https://plotly.com/python/choropleth-maps/

# Choropleth Maps:
    # A Choropleth map uses colors to represent data across geographic regions.  

# Challenges in Geographical Plotting:  
    # Data often comes in varying formats (e.g., GeoJSON, Shapefiles).  
    # Requires specialized libraries for specific datasets.  

# Why Plotly?  
    # Built-in interactive features for zooming, hovering, and customization.  
    # Matplotlib's "Basemap" is deprecated (use "Cartopy" instead), but Plotly is simpler for web-ready maps.  



# Let's create a Choropleth map using Plotly!  
# It allows us to plot information on either a global or nationwide scale.  
# Choropleth maps can be challenging at first due to Plotly's syntax,  
    # so we'll use this notebook for reference.
    # also ther's a "cheat sheet" pdf for plotly:
        # https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf

# We'll focus on:  
    # Nationwide scale plots  
    # Real-world data with larger nationwide plots  
    # World-scale plots

# import libraries
import numpy as np
import pandas as pd
import cufflinks as cf

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# Enable offline mode for interactive plotting
cf.go_offline()


# using local "Plotly.js"
import plotly.io as pio
import plotly.plotly as ptly
import plotly.express as px
from plotly.offline import iplot


# first we build our data-dictionary
# We'll use the dict() method to create a dictionary.
    # to cast a list to the dictionary

data = dict(type = 'choropleth',
            locations = ['AZ', 'CA', 'NY'],
            loactionmode = 'USA-states',
            colorscale = 'Portland',
            text = ['text 1', 'text 2', 'text 3'],
            z = [1.0, 2.0, 3.0],
            colorbar = {'title':'colorbar title goes here'}
        )

# Define key elements:
    # "type": Set as 'choropleth'
    # "locations": List of state abbreviations (e.g., ['AZ', 'CA', 'NY']).
    # "locationmode": Set to 'USA-states'. It'll let plotly know that we're doing this in US-level
        # theres' also different location modes, more in "documentation"
    # "colorscale": Choose a predefined color scheme (e.g., 'Portland') 
        # we can however use other colorscaleas such as green, grays
    # "text": List of hover text values, i.e. each of the locations.
    # "z": actual values shown in to the coloscale.
    # "colorbar": Dictionary defining the "color bar title".

# We use this kind of notation because it follows Plotly's documentation.



