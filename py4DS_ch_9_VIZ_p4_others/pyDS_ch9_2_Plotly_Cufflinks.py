
################# 11.1: full, 11.2:
# copy:
#        
#        
################# (21-Jan-25 for 22-Jan-25)

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

# test plotly:
import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('first_figure.html', auto_open=True)


# Standalone HTML:
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


