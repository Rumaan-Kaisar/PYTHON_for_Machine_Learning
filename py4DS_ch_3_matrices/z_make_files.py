# import os

# Directory: List of the folders you want to create
file_names = ["pyDS_ch3_1_prj_info_Bsktbl",
"pyDS_ch3_2_mtrix_dict",
"pyDS_ch3_3_visualize",
"pyDS_ch3_4_functions",
"pyDS_ch3_5_prj_FW"]



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


# "pyDS_ch3_1_prj_info_Bsktbl",
# "pyDS_ch3_2_mtrix_dict",
# "pyDS_ch3_3_visualize",
# "pyDS_ch3_4_functions",
# "pyDS_ch3_5_prj_FW"