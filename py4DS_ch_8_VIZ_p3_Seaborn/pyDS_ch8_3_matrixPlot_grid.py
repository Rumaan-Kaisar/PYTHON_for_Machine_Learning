
################# 9.4: FULL
# copy:  
#        
#        
################# (30-Nov-24 for 01-Dec-24)

# Courses: PrTla PY for DS & ML >    9.4, 9.5

# ------------    matrix plots    ------------

# We'll learn how to create matrix plots (primarily heatmaps) in Seaborn.

# import libraries
import seaborn as sns
# shows figures in ipynb
%matplotlib inline

# To remove 'warnings' use 'filterwarnings'
import warnings
warnings.filterwarnings('ignore')

# lets load a builtin dataset of seaborn. we import 2 datasets: 'tips' and 'flights'
    # tips: a dataset of restaurant patrons' tipping behavior
    # flights: shows the number of passengers for each month of given years
tips = sns.load_dataset('tips')
tips.head()

flights = sns.load_dataset('flights')
flights.head()

