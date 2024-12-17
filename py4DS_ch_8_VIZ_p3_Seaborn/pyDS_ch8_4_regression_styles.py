
################# 9.6
# copy:  
#        
#        
################# (15-Dec-24 for 17-Dec-24)

# Courses: PrTla PY for DS & ML >    9.6, 9.7


# ------------    Regression Plots    ------------
# Seaborn includes many tools for regression plots (Regression will be discussed later in the machine learning section)
# For now, we'll focus on the lmplot() function

# import libraries
import seaborn as sns
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# lets load a builtin dataset of seaborns: 'tips'
tips = sns.load_dataset('tips')
tips.head()


# ----  lmplot  ----
# lmplot: Displays linear models and allows:
# Splitting plots by features.
# Coloring using the hue parameter (based off of features)


