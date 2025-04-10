
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
# import cufflinks as cf    # we don't need 'iplot' from cufflinks, instead we'll directly plot to HTML

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# Enable offline mode for interactive plotting
# cf.go_offline()   # no need to use cufflinks


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
    locations=df2['CODE'],  # Country abbreviations  
    locationmode='ISO-3',  # Correct location mode for world maps 
    # locationmode='country names',  # use this location mode if no country code is given
    z=df2['GDP (BILLIONS)'],  # Color intensities based on country's GDP  
    text=df2['COUNTRY'],  # Name of each country  
    colorbar={'title': 'GDP in billion USD'},  # Title for the color scale  
)

# Modify the layout  
layout_w = dict(  
    title="2014 Global GDP",  
    geo=dict(  
        showframe=False,
        projection={'type': 'mercator'}
        # used 'mercator' instead of 'Mercator'
    )  
)

# Notice no 'locationmode' or 'scope' is used for a world map  
# Create the map  
import plotly.graph_objs as go

choromap_3 = go.Figure(data=[data_w], layout=layout_w)

# Save the figure as an HTML file  
pio.write_html(choromap_3, 'choromap_3.html', include_plotlyjs='./plotly-2.35.2.min.js')

# Notice the color intensity indicates more developed countries like the USA or China  

# More on referance:
    # https://plot.ly/python/reference/#choropleth
    # we can search for projection -> type 
    # for example we can set types "steriographic" or "kavrayskiy7" or "natural earth" to "projection={'type': 'mercator'}"






# ----------------    Geo-Plot: Exercises   ----------------
# Now, let's review choropleth map functionality using simple datasets in Plotly
# Use choropleth map and Plotly documentation

# we'll plot 2 dataset:
# dataset 1 (world map): 2014 world power consumption.
    # Create a choropleth plot showing power consumption by country using 'data' and 'layout'.

# dtaset 2 (USA map): 2012 USA election data
    # Create a plot displaying the Voting-Age Population (VAP) per state.

# Note: Some data may be in floating-point or string format, requiring conversion before use.


# import libraries
import numpy as np
import pandas as pd

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# using local "Plotly.js"
import plotly.io as pio
import plotly.express as px
from plotly.offline import iplot

# ----  Ex1: World power consumption  ----

df_ex1 = pd.read_csv("./data_World_Power_Consumption")
df_ex1.head()


# Let's create our "data" and "layout" objects  
    # If your dataset does not have country abbreviations (ISO Alpha-3 codes), 
    # you need to convert full country names into ISO Alpha-3 codes.
        # We can do this using the "pycountry" library (pycountry provides the ISO databases for the standards). 
        # pip install pycountry

# Function to convert country names to ISO-3 codes
import pycountry
def get_iso3(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except LookupError:
        return None  # Return None if country not found

# Apply the function to create a new 'CODE' column
df_ex1['CODE'] = df_ex1['Country'].apply(get_iso3)

# Drop any rows where conversion failed
rows_before = df_ex1.shape[0]
df_ex1 = df_ex1.dropna(subset=['CODE'])

rows_after = df_ex1.shape[0]
dropped_rows = rows_before - rows_after  

print(f"Dropped rows: {dropped_rows}")

data_ex1 = dict(
    type='choropleth',
    locations=df_ex1['CODE'],  # Country names instead of Country abbreviations 
    locationmode='ISO-3',  # Correct location mode for world maps  
    z=df_ex1['Power Consumption KWH'],  # Color intensities based on country's GDP  
    text=df_ex1['Country'],  # Name of each country  
    colorbar={'title': 'World_Power_Consumption in KWH'},  # Title for the color scale  
)


# Layout  
layout_ex1 = dict(  
    title="2014 world power consumption",  
    geo=dict(  
        showframe=False,
        projection={'type': 'mercator'}
        # used 'mercator' instead of 'Mercator'
    )  
)

# Notice no 'locationmode' or 'scope' is used for a world map  
# Create the map  
import plotly.graph_objs as go

choromap_ex1 = go.Figure(data=[data_ex1], layout=layout_ex1)

# Save the figure as an HTML file  
pio.write_html(choromap_ex1, 'choromap_ex1.html', include_plotlyjs='./plotly-2.35.2.min.js')



# ----  No country code version  ----
# to use "locations = df_ex1['Country']" instead of "locations=df_ex1['CODE']"
    # we need to change the locationmode from 'ISO-3' to  "country names"

df_ex1_v2 = pd.read_csv("./data_World_Power_Consumption")
df_ex1_v2.head()

data_ex1_v2 = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = df_ex1_v2['Country'],
        locationmode = "country names",
        z = df_ex1_v2['Power Consumption KWH'],
        text = df_ex1_v2['Country'],
        colorbar = {'title' : 'Power Consumption KWH'},
      ) 

layout_ex1_v2 = dict(title = '2014 Power Consumption KWH',
                geo = dict(
                    showframe = False,
                    projection = {'type':'mercator'})
                )

# Create the map  
import plotly.graph_objs as go

choromap_ex1_v2 = go.Figure(data=[data_ex1_v2], layout=layout_ex1_v2)

# Save the figure as an HTML file  
pio.write_html(choromap_ex1_v2, 'choromap_ex1_v2.html', include_plotlyjs='./plotly-2.35.2.min.js')




# ----  Ex2 (USA map): 2012 USA election  ----

import pandas as pd

df_ex2 = pd.read_csv("./data_Election_Data")
df_ex2.head()

# Let's create our "data" and "layout" objects  

data_ex2 = dict(
    type='choropleth',  
    colorscale='YlOrRd',  # Yellow-Orange-Red scale  
    reversescale = True,
    locations=df_ex2['State Abv'],  # State abbreviations  
    locationmode='USA-states',  
    z=df_ex2['Voting-Age Population (VAP)'],  # Color intensities based on "Voting-Age Population (VAP)" 
    text=df_ex2['State'],  # Additional info for each state  
    colorbar={'title': 'Voting-Age Population (VAP)'},  # Title for color scale  
    marker=dict(line=dict(color='rgb(255,255,255)', width=1))  # White state borders  
)


# we need to modify:    layout = dict(geo={'scope':'usa'})
layout_ex2 = dict(  
    title="2012 USA election: Voting-Age Population (VAP)",  
    geo=dict(  
        scope='usa',  
        showlakes=True,  
        lakecolor='rgb(85, 173, 240)'  # Blue lakes  
    )  
)

# Create the map  
import plotly.graph_objs as go
choromap_ex2 = go.Figure(data=[data_ex2], layout=layout_ex2)

# Save the figure as an HTML file  
pio.write_html(choromap_ex2, 'choromap_ex2.html', include_plotlyjs='./plotly-2.35.2.min.js')





# ----------------  Offline Plotly using external JSON  ----------------

# To create a Plotly choropleth map fully offline, you'll need to use a local GeoJSON file for the map's geometry data, 
    # as Plotly's default behavior is to fetch this data from online sources.

# Download the necessary GeoJSON file for the map you intend to create.
    # Offline Choropleth world map plot: https://community.plotly.com/t/offline-choropleth-world-map-plot/77243
    # world map: https://cdn.plot.ly/world_110m.json

# Load the GeoJSON File Locally
# If your choropleth needs a GeoJSON file, make sure it’s stored in the same directory as the HTML file.
# /plots/
#     choropleth_map.html
#     local_geojson.json
import json

with open('./plots/world_110m.json') as geojson_file:
    geojson_data = json.load(geojson_file)


# load data
df_ex1_v2 = pd.read_csv("./data_World_Power_Consumption")
df_ex1_v2.head()


# To include geojson_data in our Figure object, 
    # we need to modify "data_ex1_v2" to use "go.Choropleth" with a geojson parameter.

# Also note that we're not going to use the dictionary form
    # because go.Figure(data=[data_ex1_v2], layout=layout_ex1_v2) expects a list of plotly.graph_objs 
    # (e.g., go.Choropleth, go.Scatter, etc.), not a dictionary.

# In earlier examples, go.Figure() automatically converted it into the "appropriate go.Choropleth object" 
    # because type='choropleth' was specified inside the dictionary. 
    # However, this "auto-conversion" does not work when using "geojson", which is required for a fully offline choropleth map.

import plotly.graph_objs as go

data_ex1_v2 = go.Choropleth(
        geojson=geojson_data,  # Include the GeoJSON data
        colorscale = 'Viridis',
        reversescale = True,
        locations = df_ex1_v2['Country'],
        locationmode = "country names",     # using country names directly, instead of "ISO-3"
        z = df_ex1_v2['Power Consumption KWH'],
        text = df_ex1_v2['Country'],
        colorbar = {'title' : 'Power Consumption KWH'},
    )
# Now, go.Figure(data=[data_ex1_v2], layout=layout_ex1_v2) will work without errors.

layout_ex1_v2 = dict(title = '2014 Power Consumption KWH',
                geo = dict(
                    showframe = False,
                    projection = {'type':'mercator'})
                )

# Create the map  
choromap_ex1_v3 = go.Figure(data=[data_ex1_v2], layout=layout_ex1_v2)

# Save the figure as an HTML file  
pio.write_html(choromap_ex1_v3, 'choromap_ex1_v3.html', include_plotlyjs='./plotly-2.35.2.min.js')

# Note:
    # Manually defining go.Choropleth(...) ensures compatibility and avoids errors.
    # Dictionaries work for simpler cases, but do not support geojson, requiring go.Choropleth(...) instead



# -----------------  USA locally  -------------------
import json

with open('./plots/us-states.json') as geojson_file:
    geojson_data = json.load(geojson_file)


# load data
df_ex2 = pd.read_csv("./data_Election_Data")
df_ex2.head()

import plotly.graph_objs as go

data_ex2 = go.Choropleth(
    geojson=geojson_data,  # Include the GeoJSON data
    colorscale='YlOrRd',  # Yellow-Orange-Red scale  
    reversescale = True,
    locations=df_ex2['State Abv'],  # State abbreviations  
    locationmode='USA-states',  
    z=df_ex2['Voting-Age Population (VAP)'],  # Color intensities based on "Voting-Age Population (VAP)" 
    text=df_ex2['State'],  # Additional info for each state  
    colorbar={'title': 'Voting-Age Population (VAP)'},  # Title for color scale  
    marker=dict(line=dict(color='rgb(255,255,255)', width=1))  # White state borders 
    )
# Now, go.Figure(data=[data_ex1_v2], layout=layout_ex1_v2) will work without errors.

layout_ex2 = dict(  
    title="2012 USA election: Voting-Age Population (VAP)",  
    geo=dict(  
        scope='usa',  
        showlakes=True,  
        lakecolor='rgb(85, 173, 240)'  # Blue lakes  
    )  
)

# Create the map  
choromap_ex2 = go.Figure(data=[data_ex2], layout=layout_ex2)

# Save the figure as an HTML file  
pio.write_html(choromap_ex2, 'choromap_ex2_lc.html', include_plotlyjs='./plotly-2.35.2.min.js')


