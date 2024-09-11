
################# 8.1: FULL, 8.2: 0.52
# copy:  
#        
#        
################# (10-Sep-24 for 11-sep-24)

# Courses: PrTla PY for DS & ML >   8.1, 8.2


# ----------------    matplotlib    ----------------
# Since we're now fimiliar with DataFrames, how data is stored in that (and data-Analysis libraries), 
# it's time to learn how can we visualize it

# ----  Intro to Matplotlib  ----
# Matplotlib is Python's most popular plotting library.
# It allows full control over every part of a figure.
# It was created to resemble MatLab's graphical plotting.
# It works with Pandas and Numpy arrays 
# 'Seaborn' (another plotting library) is built on top of 'Matplotlib'
    # We need to understand Matplotlib first to learn Seaborn.



# ----  install  ----

To install Matplotlib:
Run the following command in your terminal or Jupyter notebook:

bash
Copy code
pip install matplotlib


Example 1: Simple Line Plot

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot
plt.plot(x, y)

# Add labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()



Example 2: Bar Plot
python
Copy code
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [3, 8, 1, 10]

# Create a bar plot
plt.bar(categories, values)

# Add labels
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()


