
# Courses: A-Z PY for Data-Science    6.11, 6.12, 6.13


# ------------    Load Dataset & Libraries    ------------
# Import the following packages needed to perform the analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# plot shown in Jupyter Notebook
%matplotlib inline  
# expand the figure-width
plt.rcParams['figure.figsize'] = 8, 4


# Loading Dataset
# Import the csv dataset
movies = pd.read_csv("./MovieRatings.csv")     # load datset

# -=-=-  Explore the data  -=-=-
# Visualize the dataframe
movies

# rename the column names to single-string names
movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']
movies.head()    # view dataset


# ----   convert 'numerical-type',' object-type' to "categorical-type"   ----
movies.Film = movies.Film.astype("category") # use assignment '=' to update the dataset
movies.Genre = movies.Genre.astype("category")   
movies.Year = movies.Year.astype("category")   
movies.info()   # check the data-type changes




# ------------    Dashboard    ------------
# What is a dashboard?
    # a dasboard is a combination of charts
    # for example sub-plot we built previously is a king of dashboard
    # because it combines two types of plot with different informations

# In this section we'll use "subplot" to create a 'Dashboard'
    # we'll populate those dashboard with different types of chart
    # we'll use a 2x2 subplot

# We'll include our dashboard:
    # kdeplot
    # violinplot
    # colored kdeplot

sns.set_style('darkgrid')   # change style
dshBd, axes = plt.subplots(2, 2, figsize = (15, 15))    # 2x2 subplot
# Note: we don't use 'sharex', 'sharey' at the first try, 
    # because we need to view all different plots first
# dshBd, axes = plt.subplots(2, 2, figsize = (15, 15), sharex=True, sharey=True)
    # used 'sharex', 'sharey' attributes to set all same 'xlim & ylim'

# kdeplot: 
    # BudgetMillions' vs 'AudienceRating'
    # BudgetMillions' vs 'CriticRating'
    # notice 2D indexes used

k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes[0, 0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes[0, 1])
k_BA.set(xlim=(-40, 250))   # setting the RANGE for k_BA
k_BC.set(xlim=(-40, 250))   # setting the RANGE for k_BC
# We use k_BC "k_BC.set(xlim=(-20, 160))" but it can be done with 'subplots' attribute "sharex"
    # the reason is: we have different kind of plots (we don't know how they look), 
    # so we do it manually


# violinplot: we put violinplot at (1, 0)
vlp_1 = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre', ax=axes[1, 0])


# kdeplot (shaded): CriticRating vs AudienceRating at (1, 1) i.e. ax=axes[1, 1]
    # combine 'shades' & 'border'  to get a overlaied plot
    # notice we also used ax=axes[1, 1] for the outlines 'kDe2'
    # we put two plots in one plotting space (overlaying)
# if we dont specify the axes, the plots will be added to the last subplot
kDe1 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds', ax=axes[1, 1])
kDe2 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds', ax=axes[1, 1]) # ads border on top of 'kDe5'
# kDe2 = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds', ax=axes[0, 0]) # different axes

# So it's so simple to add charts to a 'Dashboard'




# ------------    Non-Seaborn plot    ------------
# how do we add a 'non-seaborn' plot into our diagram?
    # above we'll used ony sns (seaborn) plots
# How do we add a plt (pyplot) chart, EG: 'Histogram', to visualize distribution?

# ERR: we can not use 'sns' syntax to add a 'plt.hist' for example in the 4th digram of our dashboard
hs_1 = plt.hist(movies.CriticRating, rwidth=.8, ax=axes[1, 1])
# rwidth=.8 gaps between bars

# we must use following 'pyplot' syntax: The procedure is bit diffeent
    # actually we use now the "standared approach", above we used a 'seaboarn way'

# standared approach: since 'dshBd, axes = plt.subplots()' is pyplot entity
    # we use 'axes[i, j].hist()' instead of "plt.hist()"
    # because each axes[i, j] itself is a 'pyplot-object'
axes[1, 1].hist(movies.CriticRating, rwidth=.8)    



# Following dashboard uses a histogram as 'non-seaboarn' plot
sns.set_style('darkgrid')   # change style
dshBd_2, axes_2 = plt.subplots(2, 2, figsize = (15, 15))    # 2x2 subplot

# kdeplot:
k_BA = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', ax=axes_2[0, 0])
k_BC = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', ax=axes_2[0, 1])
k_BA.set(xlim=(-40, 250))   # setting the RANGE for k_BA
k_BC.set(xlim=(-40, 250))   # setting the RANGE for k_BC

# violinplot: we put violinplot at (1, 0)
vlp_1 = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre', ax=axes_2[1, 0])

# Histogram
axes_2[1, 1].hist(movies.CriticRating, rwidth=.8) 
plt.show() 

# Note: To learn more, visit 'matplotlib' documentation
    # in seaboarn we cannot use "axes_2[1, 1].kdeplot", 
    # because, "axes_2[1, 1]" is a pyplot object, it's not a 'seaboarn object'
        # seaborn is created on top of pyplot like an 'add-on'
        # so "axes_2" doesn't know anything about 'seaboarn', i.e. kdeplot or violinplot
        # that's why we need to sepcify the location in 'seaborn' using: "ax=axes_2[1, 0]" as argumet
        # but 'hist' is a pyplot function, therefore 'axes_2[1, 1].hist()' works
    # hence following cause error
axes_2[1, 0].violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre')    # ERR
# it also disables the next 'sub-plots'




# ------------    Styling Dashboard    ------------
# Styling Tips:
    # we can style our existing Dashboard to look more professional
    # To make more interesting to make people read it

# We'll style our previous Dashboard as below:
    # How to style?
        # we first style 'k_BA' and 'k_BC' as we did for 'kDe1' (shade, cmap or color map)
        # we'll use different color map for 'k_BA' and 'k_BC' because they related to 'budget and ratings'
        # so that reader can differ 'k_BA' and 'k_BC' from 'kDe1'

# Tip 1: How to get all available color easily?
    # TYPO: make a typo in cmap='Reds'. Eg: cmap='Redos12'
    # it'll generate an error with showing all available colors
    # copy all those color to a list and use that later
    # Reverse: to reverse a colormap use '_r'. Eg: 'inferno' to 'inferno_r'

sns.set_style('darkgrid')   # change style
dshBd_3, axes_3 = plt.subplots(2, 2, figsize = (15, 15))    # 2x2 subplot


# -=-=-=-   kdeplot   -=-=-=-
# Plot [0,0]
    # we'll use 'inferno' for sahding and 'cool' for outlines
k_BA_s = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', shade=True, shade_lowest=True, cmap='inferno', ax=axes_3[0, 0])
k_BAo_s = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', cmap='cool', ax=axes_3[0, 0])

# Plot [0,1]
k_BC_s = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', shade=True, shade_lowest=True, cmap='inferno', ax=axes_3[0, 1])
k_BC_s = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', cmap='cool', ax=axes_3[0, 1])

# setting x range for 'k_BA' and 'k_BC'
k_BA_s.set(xlim=(-40, 250))   # setting the RANGE for k_BA
k_BC_s.set(xlim=(-40, 250))   # setting the RANGE for k_BC


# -=-=-=-   violinplot   -=-=-=-
# Plot [1,0]
vlp_1_s = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre', ax=axes_3[1, 0])


# -=-=-=-   kdeplot (shaded)   -=-=-=-
# Plot [1,1]
kDe1_s = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds', ax=axes_3[1, 1])
kDe2_s = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds', ax=axes_3[1, 1]) # ads border on top of 'kDe5'
plt.show() 



""" 
Getting all colors using 'ERR'
ValueError: ['infernyo' is not a valid value for name; supported values are 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 
'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 
'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 
'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 
'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 
'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'crest', 'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare', 
'flare_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 
'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 
'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 
'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 
'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r']

"""



# -=-=-=-    Changing Seaborn BACKGROUND & GRID style    -=-=-=-
    # the background in plot [0,0] & [0,1] are coming from "shade_lowest=True" it's not the real background
    # from the color skim "inferno"
    # To change the background, we need to set for the 'sns' seaboarn style
sns.set_style('darkgrid')
# the other preset styles are: white, whitegrid, dark, darkgrid, ticks
    # to change further, we need to pass "kwargs" in a dictionary
sns.set_style('darkgrid', {"axes.facecolor":"black"})
# Note: 'darkgrid' isn't actually black, its kinda bluish background
    # We also get our grids

# To disable the grids we set: 'darkgrid' to 'white' or 'dark'; 
    # then it'll ovveride by the kwargs "axes.facecolor":"black"
    # also we can set 'shade_lowest=False' for all KDE plots
sns.set_style('white', {"axes.facecolor":"black"}) 

dshBd_3, axes_3 = plt.subplots(2, 2, figsize = (15, 15))    # 2x2 subplot

# -=-=-=-   kdeplot   -=-=-=-
# Plot [0,0]
k_BA_s = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', shade=True, shade_lowest=False, cmap='inferno', ax=axes_3[0, 0])
k_BAo_s = sns.kdeplot(data=movies, x='BudgetMillions', y='AudienceRating', cmap='cool', ax=axes_3[0, 0])
# Plot [0,1]
k_BC_s = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', shade=True, shade_lowest=False, cmap='inferno', ax=axes_3[0, 1])
k_BC_s = sns.kdeplot(data=movies, x='BudgetMillions', y='CriticRating', cmap='cool', ax=axes_3[0, 1])
# setting x range for 'k_BA' and 'k_BC'
k_BA_s.set(xlim=(-40, 250))
k_BC_s.set(xlim=(-40, 250))

# -=-=-=-   violinplot   -=-=-=-
# Plot [1,0]
vlp_1_s = sns.violinplot(data=movies, x='Genre', y='CriticRating', hue='Genre', ax=axes_3[1, 0])

# -=-=-=-   kdeplot (shaded)   -=-=-=-
# Plot [1,1]
kDe1_s = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds', ax=axes_3[1, 1])
kDe2_s = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='Reds', ax=axes_3[1, 1]) # ads border on top of 'kDe5'
plt.show() 


# ----  rev[28-feb-24]  ----
# Styling Violinplot and last KDE-plot
    # we use different color for the last KDE than the first two
        # We use 'gist_gray_r' for contour outline.
        # for shading we use 'blue_r'
        # lighter color will be on outline for the outside, for inside we'll get light shading with darker outlines
        # notice how we used reversed colors
    # for violinplot, we'll use a parmeter: "palette" for color. Eg: palette='cool'
        # we don't use 'hue' anynore
        # we've used palette='YlOrRd'. for Yellow-Orange-Red palatte.

# -=-=-=-   violinplot   -=-=-=-
# Plot [1,0]
vlp_1_s = sns.violinplot(data=movies, x='Genre', y='CriticRating', palette='YlOrRd', ax=axes_3[1, 0])

# -=-=-=-   kdeplot (shaded)   -=-=-=-
# Plot [1,1]
kDe1_s = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, shade=True, shade_lowest=False, cmap='Blues_r', ax=axes_3[1, 1])
kDe2_s = sns.kdeplot(x=movies.CriticRating, y=movies.AudienceRating, cmap='gist_gray_r', ax=axes_3[1, 1]) # ads border on top of 'kDe5'

# This 'styled dashboard' is good for the Presentation. 
    # It stands out more and make people curious
    # It is fun and vibrant, 
    # Makes your presentation attractive that audience wants to learn more about the data
# Other Dashboards (no-style) is suitable for academic-publication/paper.




# ------------    some Finishing Touches    ------------
# Previously we've learned to style our dashboards
    # we can go on more about 'Styling and Visualization'
    # Through the previous sections we learned only fundamnetal techniques.
    # so we can learn more techniques from web/documentation

# as finishing touch for example: we can improve "Stacked Histogram" that we previously created 
    # it wwas built using 'pyyplot' instead of 'seaborn' and it needs following:
            # adding a "Title"
            # changing the axis
            # increasing font size, 
            # Axis titles
            # modifying Legends and make it more visible by changing color

# Though our previous "Stacked Histogram" visualizing the data and telling some stories
    # Those are 'Thematical-edits' that we can do for final presentation
    



# ------------    THEMATIC EDITS    ------------

# -=-=-  2 ways of styling grid  -=-=-

# way 1: use 'seaborn-style':
    # even though we're doing 'pyplot', but we can still apply 'seaborn' style
    # remember 'seaborn' is just a addon on top of 'pyplot'
    # here its affecting a 'non-seaborn' pyplot visualization
list_1 = list()
all_genre = list()
for gen in movies.Genre.cat.categories:
    list_1.append(movies[movies.Genre == gen].BudgetMillions) 
    all_genre.append(gen)   

sns.set_style("whitegrid")  # applying seaborn-style to 'non-seaborn' pyplot visualization
# all_genre = list(movies.Genre.cat.categories)   # for lebels
hs_3 = plt.hist(list_1, bins=30, stacked=True, rwidth=.8, label=all_genre)
plt.legend()
plt.show()


# way 2: use 'subplots' Hack:
    # it'll allow us to 'Resize' the chart
    # its applicable to many other different graphs/charts

    # we'll create a 'subplots', but with "only one item"
        # we won't specify any parameters, it'll create a 'subplots with one item' 
        # fig, ax = plt.subplots()
        # The trick is: we've seen any changes will applied to 'last-box of the subplots'
            # when we created a 'subplots with one item',
            # the new plot 'hs_3 = plt.hist()' will be on top of the 'subplot'
            # thus the grid from 'subplot' autometically applied to 'hs_3 = plt.hist()'
        
        # Note: 'subplot' and 'subplots' are different
    
    # We apply both 'seaborn' & subplots'
        # 'seaborn' to apply styling
        # 'subplots' for resizing and more styling

sns.set_style("whitegrid")  # applying seaborn-style

list_1 = list()
all_genre = list()
for gen in movies.Genre.cat.categories:
    list_1.append(movies[movies.Genre == gen].BudgetMillions) 
    all_genre.append(gen)   

fig, ax = plt.subplots() # applying "subplot"

# following 'hs_3 = plt.hist()' is created inside the 'fig' of the 'subplot with one item'
hs_3 = plt.hist(list_1, bins=30, stacked=True, rwidth=.8, label=all_genre)
plt.legend()
plt.show()




# ----    change the 'subplot size'    ----
# we can now apply 'fig.set_size_inches()' to our subplot
sns.set_style("whitegrid")  # applying seaborn-style
list_1 = list()
all_genre = list()
for gen in movies.Genre.cat.categories:
    list_1.append(movies[movies.Genre == gen].BudgetMillions) 
    all_genre.append(gen)   

fig, ax = plt.subplots() # applying "subplot"
# Now we can easily change the size of the figure
fig.set_size_inches(11.7, 8.27)     # size of A4 paper
# Notice we now controll the size of the visualization by controlling the 'figure of a subplot'

# following 'hs_3 = plt.hist()' is created inside the 'fig' of the 'subplot with one item'
hs_3 = plt.hist(list_1, bins=30, stacked=True, rwidth=.8, label=all_genre)
plt.legend()
plt.show()




# ----    Adding title, axis-lables, tick-size, Legends    ----
sns.set_style("whitegrid")  # applying seaborn-style, We apply both 'seaborn' & subplots'
list_1 = list()
all_genre = list()
for gen in movies.Genre.cat.categories:
    list_1.append(movies[movies.Genre == gen].BudgetMillions) 
    all_genre.append(gen)   

fig, ax = plt.subplots() # applying "subplot"
fig.set_size_inches(11.7, 8.27)     # size of A4 paper

hs_3 = plt.hist(list_1, bins=30, stacked=True, rwidth=.8, label=all_genre)
# ----    Adding title    ----
plt.title("Movie Budget Distribution", fontsize=35, color="Darkblue", fontname="Consolas")
# we use following 'kwargs'
    # Increase font size: fontsize = 35
    # color = "Darkblue"
    # fontname = "Roboto"
    # for more kwrgs, use Google to find-out
# ----    axis-lables    ----
plt.xlabel("Budget", fontsize=25, color="Green")
plt.ylabel("Number of Movies", fontsize=25, color="Red")
# ----    tick-size, fontsize of the x-axis, y-axis ticks    ----
plt.xticks(fontsize=20, color="Green")
plt.yticks(fontsize=20, color="Red")
# ----    modify legends    ----
    # we already applied 'plt.legend()', we just need to adjust some parameters
    # size: prop={'size':20}
    # background and frame: frameon=True
    # rounded frame: fancybox=True
    # shadow=True
    # transperancy: framealpha=1
        # to make it transparent, we can use framealpha=0.5
# ----  rev[6-mar-24]  ----
plt.legend(prop={'size':20}, frameon=True, fancybox=True, shadow=True, framealpha=1)
# label color: change plt.hist's label color, color=["Red", "Salmon", "Blue"]
plt.show()


# Note
    # remove gap between the bars (side): rwidth=1
    # Legends: use 'label = all_genre' attribute
    


