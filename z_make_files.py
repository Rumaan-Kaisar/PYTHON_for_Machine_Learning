# import os

# Directory: List of the folders you want to create
file_names = ["py_ch12_1_1_HTTP_intro",
"py_ch12_1_2_Verbs_APIs",
"py_ch12_1_3_PyRequest",
"py_ch12_1_4_API_Project"]



# Parent Directory path
# parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

# Path
# path = os.path.join(parent_dir, directory)
for i in range (0, len(file_names)):
    # path = "./"+directories[i]
    # Create the files
    try:
        # os.makedirs(path, exist_ok = True)
        f = open(f"{file_names[i]}.py", "w") # creates an empty 'py' 
        print(f"{file_names[i]}.py is created sucuessfully")
    except:
        print("files '%s' can not be created" % file_names[i])

# run windows cmd/terminal inside the working directory
# python z_make_files.py


# "py_ch12_1_1_HTTP_intro",
# "py_ch12_1_2_Verbs_APIs",
# "py_ch12_1_3_PyRequest",
# "py_ch12_1_4_API_Project"
