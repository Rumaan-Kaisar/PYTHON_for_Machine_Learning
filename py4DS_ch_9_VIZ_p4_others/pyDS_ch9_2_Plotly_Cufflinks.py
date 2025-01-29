
################# 11.1: full, 11.2: 8.32
# copy: plot_fig5
#        
#        
################# (28-Jan-25 for 29-Jan-25)

# Courses: PrTla PY for DS & ML >    11.1, 11.2

# ------------    Plotly and cufflinks    ------------

# We'll learn a bit about the background of Plotly and Cufflinks, 
# which allow us to create "Interactive Visualizations".

# 'Plotly' is an interactive, open-source visualization library, 
# 'Cufflinks' connects 'Plotly' with 'pandas'.
# These libraries enable us to generate "Interactive Visualizations" directly from our DataFrame.



# ----  Installation  ----
# Before exploring these libraries, ensure they are installed using pip:
#       pip install plotly
#       pip install cufflinks



# ----  Official Website:    https://plotly.com/ (formerly plot.ly)
# Plotly is also a hosting company that can host your 'visualizations' and 'dashboards'. 
# However, if you handle it yourself, the library is entirely free and open-source.

# Plotly is compatible with multiple languages and tools, including:
# Python, R, MATLAB, Excel, and JavaScript.

# Our focus will be on using Plotly with Python.



# ----  Getting started with Python:    https://plotly.com/python/, https://plotly.com/python/getting-started/
# Is Plotly for Python Free?
    # Yes, Plotly for Python is free and open-source, licensed under the MIT license.
    # You can install and use it at no cost. 
# Plotly allows you to create, view, and share charts and maps offline, 
    # without requiring registration, tokens, or accounts.

# To install Plotly's Python package, use the package manager pip inside your terminal.
#       pip install plotly
# or    pip install plotly==5.24.1
# or    conda install -c plotly plotly=5.24.1


# --------    Test Plotly    --------

# test plotly: Makes an "HTML" file
    # The HTML file will embed Plotly.js (so the HTML will be havier, > 4.5mb)
    # However, we can use 'cdn' to imbed Plotly.js, makes the HTML much light-weight
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('first_figure.html', auto_open=True)


# plotly.offline, Standalone HTML:
    # Offline mode will save an HTML file locally and open it inside your web browser.

import plotly
print(plotly.__version__) # version > 1.9.4 required

from plotly.graph_objs import Scatter, Layout 

plotly.offline.plot({
    "data": [
        Scatter(x=[l, 2, 3, 4], y=[4, 1, 3, 7])
    ],
    "layout": Layout(
        title="hello world"
    )
})


# ----  cufflinks  ----
# We need to connect Plotly to Pandas.
    # install:      pip install cufflinks
# It's a productivity tool that allows us to quickly call plots (similar to pandas df.plot).
# However, instead of static plots, we're creating interactive visualizations with Plotly.

# https://pypi.org/project/cufflinks/
# https://github.com/santosjorge/cufflinks




# ------------  import libraries, setup  ------------
# import libraries
import numpy as np
import pandas as pd
import cufflinks as cf

# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')


# check plotly version
import plotly
print(plotly.__version__)   # version > 1.9.4 required




# --------    Show pltly figures in jypyter nb    --------

# Use plotly in ipynb: render through Plotly.js but not saved to notebook (not recomended)
    # ERR: Mime type rendering requires nbformat>=4.2.0 but it is not installed
    # pip install --upgrade nbformat
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.show()


# another way to see it in notebook (not recomended)
# use offline version
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# For Notebooks
init_notebook_mode(connected=True)
# For offline use
cf.go_offline()

# create a DataFrame
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.head()

# show plotly in notebook
df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)




# --------    use 'cdn' or 'plotly-2.35.2.min.js in working directory'    --------
    # The HTML file's large size is primarily due to the embedded Plotly.js.
    # To reduce the size, we can use 'cdn' to load Plotly.js externally.
    # Alternatively, we can download "Plotly.js" to our working directory and reference it locally.

# using 'cdn'
import plotly.io as pio
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
pio.write_html(fig, 'plot_lc.html', include_plotlyjs='cdn')


# ---- Best way: use 'cdn' or local "plotly.js" file path ----
# For a minimal offline approach, follow these steps:
#   1. Download the Plotly.js file (e.g., plotly-2.35.2.min.js).
#   2. Create the HTML using plotly.io and set include_plotlyjs='.\plotly-2.35.2.min.js'.
#   3. This uses the local "plotly.js" file path instead of 'cdn'.

# using local "Plotly.js"
import plotly.io as pio
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
pio.write_html(fig, 'plot_lc.html', include_plotlyjs='.\plotly-2.35.2.min.js')




# ------------    plotly plots    ------------

# Plotly functions to create different types of plots  
# Example Plotly functions for various visualizations:  
    # 1. go.Scatter: For line plots, scatter plots  
    # 2. go.Bar: For bar plots  
    # 3. go.Pie: For pie charts  
    # 4. go.Box: For box plots  
    # 5. go.Histogram: For histograms  
    # 6. go.Heatmap: For heatmaps  
    # 7. go.Surface: For 3D surface plots  

# You can explore and customize each plot by adding traces and updating layouts. 
"""  
# Example:  
import plotly.graph_objects as go

# Line plot example
fig = go.Figure(data=go.Scatter(x=["A", "B", "C"], y=[10, 20, 30]))
fig.show()
"""

# Let's create 2 dataframes

# df1: normal distribution of 100 rows and 4 columns
df1 = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df1.head()

# df2: used categorical data, notice dictionary style
df2 = pd.DataFrame({'Category';['A', 'B', 'C'], 'val':[32, 43, 50]})
df2


# lets plot using malpotlib
df1.plot()



# ----  Plot using Plotly & iplot  ----
import plotly.io as pio
from plotly.offline import iplot

# Generate the plot
fig2 = df1.iplot(asFigure=True)
# The asFigure=True parameter is used in Cufflinks' iplot() function to ensure 
    # that it returns a Plotly Figure object instead of rendering the plot directly in the notebook.
    # Instead of rendering the plot, iplot() returns a Plotly Figure object.
    # This allows you to manipulate, save, or customize the figure further before displaying or exporting it.
# By Default When you call iplot() without asFigure=True, it immediately renders the plot in the notebook.

# Save the plot as an HTML file using a local Plotly.js file
pio.write_html(fig2, 'plotly_fig2.html', include_plotlyjs='./plotly-2.35.2.min.js')



# lets see an alternative way to plot without using iplot()
    # alternative: plotly.offline.plot()
from plotly.offline import plot
import plotly.graph_objects as go

# Create a simple figure
fig3 = go.Figure(data=go.Scatter(x=df1.index, y=df1['A']))

# Save the plot as an HTML file
plot(fig3, filename='plotly_fig3.html', include_plotlyjs='./plotly-2.35.2.min.js', auto_open=True)



# Create a line plot for all columns
fig4 = go.Figure()

for column in df1.columns:
    fig4.add_trace(go.Scatter(x=df1.index, y=df1[column], mode='lines+markers', name=column))

# Update layout
fig4.update_layout(
    title="Line Plot for All Columns",
    xaxis_title="Index",
    yaxis_title="Values",
    template="plotly_white"
)

# Show the plot
fig4.show()

# Save the plot as an HTML file
plot(fig4, filename='plotly_fig4.html', include_plotlyjs='./plotly-2.35.2.min.js', auto_open=True)



# ----  Enable Hovermode on axis & features  ----
# magic of: iplot, plotly & cufflinks
import plotly.io as pio
from plotly.offline import iplot

# Generate the plot
fig5 = df1.iplot(asFigure=True, kind='line', title="Comparison Hover Example")
# By using kind='line', you're explicitly instructing Cufflinks to render the data as a line chart.
# For numeric data, it usually defaults to kind='line'.
# Custom Plot Types: You can specify other plot types using kind, such as 'bar', 'scatter', 'box', 'surface', etc.

# Update the layout to enable hover comparisons
fig5.update_layout(
    hovermode='x unified',  # Enable hover comparison
    xaxis_title="Index",
    yaxis_title="Values"
)

# Save the plot as an HTML file using a local Plotly.js file
pio.write_html(fig5, 'plotly_fig5.html', include_plotlyjs='./plotly-2.35.2.min.js')

# features: 
    # zoom-in: By marking selection-box (or use the buttnon)
    # zoom-out: double click (or use the buttnon)
    # capture as png
    # pan/move the whole plot
    # Hover on the plot
    # Hover on the X-axis
    # trun on/off a plot by 2x-clicking on legend




# ------------    scatter, bar, box, ratio, heatmap and more    ------------
# use 'kind' to set plot-type

# scatterplot: need x and y (we set those for column)
    # by default it'll connect the points by line, so we've used "mode=marker"
    # we can also set size
import plotly.io as pio
from plotly.offline import iplot

# Generate the plot
# fig6 = df1.iplot(asFigure=True, kind='scatter', x='A', y='B')
fig6 = df1.iplot(asFigure=True, kind='scatter', x='A', y='B', mode='markers')

# Save the plot as an HTML file using a local Plotly.js file
pio.write_html(fig6, 'plotly_fig6_2.html', include_plotlyjs='./plotly-2.35.2.min.js')



# Barplot : we now use a categorical DataFrame
fig7 = df2.iplot(asFigure=True, kind='bar', x='Category', y='val')
pio.write_html(fig7, 'plotly_fig7.html', include_plotlyjs='./plotly-2.35.2.min.js')

