
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

# To install Matplotlib Run the following command in your terminal or Jupyter notebook:
# use pip or conda
pip install matplotlib
# or 
conda install matplotlib

# --------    official website: matplotlib.org    --------
# gallery:
    # different types of plots, we can use any of those
    # eg: pie or polar chart -> pie chart

# doc:
    # documentation for usage and how to plot
    # just be familier with common functions


# Example 1: Simple Line Plot

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




# Example 2: Bar Plot

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


