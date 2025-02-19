
################# 12.1: full, 12.2: full, 12.3: 1.19
# copy: coroplot_2, ipynb, this py
#        
#        
################# (18-Feb-25 for 19-Feb-25)

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
# import plotly.plotly as ptly      # deprecated
import plotly.express as px
from plotly.offline import iplot




""" 
        Now, we need to begin building our data dictionary. 
        The easiest way to do this is by using the dict() function with the following general structure:  

        type = 'choropleth'
        locations = List of states  
        locationmode = 'USA-states'
        colorscale = Choose a predefined or custom scale  
        text = List or array of text to display per point  
        z = Array of values for the z-axis (determining state color)
        colorbar = {'title': 'Colorbar Title'}
"""
# Choosing a Colorscale
# You can select from predefined color scales, such as:  
    # 'pairs'
    # 'Greys'
    # 'Greens'
    # 'Bluered'
    # 'Hot'
    # 'Picnic'
    # 'Portland'
    # 'Jet'
    # 'RdBu'
    # 'Blackbody'
    # 'Earth'
    # 'Electric'
    # 'YIOrRd'
    # 'YIGnBu'

# or create a custom colorscale (https://plot.ly/python/heatmap-and-contour-colorscales/)
# Here we make it like below:

# first we build our data-dictionary
# We'll use the dict() method to create a dictionary.
    # to cast a list to the dictionary

data = dict(type = 'choropleth',
            locations = ['AZ', 'CA', 'NY'],
            locationmode = 'USA-states',
            colorscale = 'Portland',
            text = ['text 1', 'text 2', 'text 3'],
            z = [1.0, 2.0, 3.0],
            colorbar = {'title':'colorbar title goes here'}
        )

# Define key elements:

    # "type": 
        # Set as 'choropleth'
        # In our "data" object, 'type' specifies what kind of geographical plot we're doing.  
    
    # "locations": 
        # List of state abbreviations (e.g., ['AZ', 'CA', 'NY']).
    
    # "locationmode": 
        # Set to 'USA-states'. It'll let plotly know that we're doing this in US-level
        # Since we're working with the USA, we specify 'USA-states'. This applies at the state level.  
        # theres' also different location modes, more in "documentation"
        # For more detail (e.g., county level), refer to the documentation.

    # "text": 
        # List of hover text values, i.e. each of the locations.
        # a list of text labels for each location in the 'locations' list, passed in the same indexed sequence.
    
    # "z": 
        # actual values shown in to the coloscale.
        # Values representing the color intensity for each location. 
        # Later, we'll see how to color different states by intensity.

    # "colorscale": 
        # Defines a specific color scale for the plot.
        # Choose a predefined color scheme (e.g., 'Portland') 
        # we can however use other colorscaleas such as green, grays

    # "colorbar": 
        # Represents the "title" of the color scale.
        # Dictionary defining the "color bar title".


# This formatting must be followed. For more details, refer to the documentation. 
    # We use this kind of notation because it follows Plotly's documentation.


# Now we create a Layout object/variable, it'll be a nested dictionary
layout = dict(geo={'scope':'usa'})

# Notice that we have two main objects:
    # 1. 'data' in dictionary form
    # 2. 'layout'

# These are then passed into graph_objs.Figure()
# Finally, the figure is plotted using iplot

# so we need to use graph_objs.figure
import plotly.graph_objs as go

choromap_1 = go.Figure(data= [data], layout=layout)
# notice, "data" is already in dict form, but we're putting it inside a list

# ----  Plot the figure  ----
# fig1 = iplot(choromap_1, asFigure=True)
# notice that, here "iplot" is from "plotly.offline" not "cufflinks "
    # here, it just displays the plot
    # so "asFigure=True" won't work here
# since it's not a dict or Figure, 
    # we must use "choromap_1" directly from go.Figure() to save as HTML

# ----  Save the figure as an HTML file  ----
# pio.write_html(fig1, 'choromap_1.html', include_plotlyjs='./plotly-2.35.2.min.js')    # ERR

# The reason why df1.iplot(asFigure=True, kind='scattermatrix') works while 
    # iplot(choromap_1, asFigure=True) does not is because they come from different libraries.
        # df1.iplot() is from cufflinks
        # iplot(choromap_1) is from plotly.offline

# display the plot
iplot(choromap_1)

# Save the figure as an HTML file
pio.write_html(choromap_1, 'choromap_1.html', include_plotlyjs='./plotly-2.35.2.min.js')

# --------  Note:  
# If we use plot() instead of iplot(), the plot is shown in an HTML file in a new browser window.  



# ----------------    USA map: Using CSV Dataset    ----------------
# Another example with real data and more options  
# Agricultural exports by state in the USA  
# Example commodities: beef, pork, poultry, dairy, fruits  

import pandas as pd

df1 = pd.read_csv("./data_US_AGRI_Exports")
df1.head()

# Let's create our "data" and "layout" objects  

data = dict(type='choropleth',  
            colorscale='YlOrRd',  # Yellow-Orange-Red scale  
            locations=df1['code'],  # State abbreviations  
            locationmode='USA-states',  
            z=df1['total exports'],  # Color intensities based on total exports  
            text=df1['text'],  # Additional info for each state  
            colorbar={'title': 'Millions USD'},  # Title for color scale  
            marker=dict(line=dict(color='rgb(255,255,255)', width=2))  # White state borders  
        )

# Explanation of parameters:  
#   - 'colorscale': Using 'YlOrRd' (Yellow-Orange-Red)  
#   - 'locations': State abbreviations stored in df1['code']  
#   - 'locationmode': 'USA-states' specifies a state-level map  
#   - 'z': Total exports determine color intensities  
#   - 'text': Labels from df1['text'], but often needs customization  
#   - 'colorbar': Title represents exports in millions of USD  
#   - 'marker': Defines state borders in white with a width of 2  

# we need to modify:    layout = dict(geo={'scope':'usa'})
layout = dict(  
    title="2011 USA Agricultural Exports",  
    geo=dict(  
        scope='usa',  
        showlakes=True,  
        lakecolor='rgb(85, 173, 240)'  # Blue lakes  
    )  
)

# Create the map  
import plotly.graph_objs as go
choromap_2 = go.Figure(data=[data], layout=layout)

# Save the figure as an HTML file  
pio.write_html(choromap_2, 'choromap_2.html', include_plotlyjs='./plotly-2.35.2.min.js')

# Notice as we hover over the "states", we can see all the "text".  
# We can also see that the "lakes" are "blue".  
# Observe the color scale and the title.  

# Also, notice the spacing (white lines) between the states—this is due to the "marker" setting:  
    # marker=dict(line=dict(color='rgb(255,255,255)', width=2))  
    # We can increase the width if needed.  

# Although the syntax and order might be confusing at first, Plotly works this way.  
    # That's why we'll use this notebook as a reference 
    # and also refer to the documentation for Plotly's choropleth maps.  
# Most of the time, we'll just copy and paste the code and fill in the gaps for our particular dataset.  
# However, these techniques are valuable because they help create clear and visually appealing geographical plots.  




# ----------------    WORLD Map: Using CSV Dataset    ----------------
# Now we'll plot at the international level
# We'll consider the world GDP dataset of 2014

import pandas as pd

df2 = pd.read_csv('./data_World_GDP')
df2.head()

# Contains Country Names, GDP in billions, and Country Codes (similar to the USA state codes we've seen earlier)
    # In this case, we'll use "GDP in billions" as the "z" color intensity value
    # We'll pass the "Country Codes" to the choropleth mapping
    # Additionally, we can use "Country Names" as the text value in our choropleth

# "data" and "layout". More on Plotly documentation: https://plot.ly/python/reference/#choropleth  
# We'll get all the argument details (e.g., projection)  

data_w = dict(
    type='choropleth',
    locations=df2['code'],  # Country abbreviations  
    locationmode='ISO-3',  # Correct location mode for world maps  
    z=df2['GDP (BILLIONS)'],  # Color intensities based on country's GDP  
    text=df2['COUNTRY'],  # Name of each country  
    colorbar={'title': 'GDP in billion USD'},  # Title for the color scale  
)

# Modify the layout  
layout_w = dict(  
    title="2014 Global GDP",  
    geo=dict(  
        showframe=False,
        projection={'type': 'Mercator'} 
    )  
)

# Notice no 'locationmode' or 'scope' is used for a world map  
# Create the map  
import plotly.graph_objs as go

choromap_3 = go.Figure(data=[data_w], layout=layout_w)

# Save the figure as an HTML file  
pio.write_html(choromap_3, 'choromap_3.html', include_plotlyjs='./plotly-2.35.2.min.js')

# Notice the color intensity indicates more developed countries like the USA or China  
