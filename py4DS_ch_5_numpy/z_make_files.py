# import os

# Directory: List of the folders you want to create

file_names = ["pyDS_ch5_1_numpy_intro",
"pyDS_ch5_2_numpy_array_indexing",
"pyDS_ch5_3_numpy_operatn"]



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


# "pyDS_ch5_1_numpy_intro",
# "pyDS_ch5_2_numpy_array_indexing",
# "pyDS_ch5_3_numpy_operatn"