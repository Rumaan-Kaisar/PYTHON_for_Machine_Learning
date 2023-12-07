# import os

# Directory: List of the folders you want to create
from importlib.metadata import files


file_names = ["pyDS_ch2_1_pandas_imprt_Xplr_colRenm",
"pyDS_ch2_2_subsetting",
"pyDS_ch2_3_basic_opr",
"pyDS_ch2_4_filtering",
"pyDS_ch2_5_at_iat",
"pyDS_ch2_6_seaborn_viz",
"pyDS_ch2_7_kwarg_RECAP",
"pyDS_ch2_8_HW_wrldTrnd"]



# Parent Directory path
# parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

# Path
# path = os.path.join(parent_dir, directory)
for i in range (0, len(file_names)):
    # path = "./"+directories[i]
    # Create the files
    try:
        # os.makedirs(path, exist_ok = True)
        with open(f"{file_names[i]}.py", "w") as f:     # creates an empty 'py'
            f.write("\n################# 348: FULL\n# copy:  \n#        \n#        \n################# (26-sep-23 for 27-sep-23)\n\n# Courses: A-Z PY for Data-Science    0\n")
        print(f"{file_names[i]}.py is created sucuessfully")
    except:
        print("files '%s' can not be created" % file_names[i])

# run windows cmd/terminal inside the working directory
# python z_make_files.py



# "pyDS_ch1_1_variables_operators",
# "pyDS_ch1_2_loops_control",
# "pyDS_ch1_3_inDntN_HW",
# "pyDS_ch1_4_list_tuples",
# "pyDS_ch1_5_functn_pkg",
# "pyDS_ch1_6_Numpy_array",
# "pyDS_ch1_7_prj_HW"


# "pyDS_ch2_1_pandas_imprt_Xplr_colRenm",
# "pyDS_ch2_2_subsetting",
# "pyDS_ch2_3_basic_opr",
# "pyDS_ch2_4_filtering",
# "pyDS_ch2_5_at_iat",
# "pyDS_ch2_6_seaborn_viz",
# "pyDS_ch2_7_kwarg_RECAP",
# "pyDS_ch2_8_HW_wrldTrnd",


# "pyDS_ch3_1_prj_info_Bsktbl",
# "pyDS_ch3_2_mtrix_dict",
# "pyDS_ch3_3_visualize",
# "pyDS_ch3_4_functions",
# "pyDS_ch3_5_prj_FW"


# Try to create 'ipynb' files
"""
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "################# 4.6: 1:55\n",
    "# copy:  \n",
    "#        \n",
    "#        \n",
    "################# (15-nov-23 for 17-nov-23)\n",
    "\n",
    "# Courses: A-Z PY for Data-Science    4.6, 4.7"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.3 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.3"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b7534786ec8a9cff2926c7e81f9ca1d65065bc188d16e9c2279a84a4000586bc"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

"""

