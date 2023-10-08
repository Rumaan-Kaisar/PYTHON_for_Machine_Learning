import os

# Directory: List of the folders you want to create
directories = ['py_ch_1_intro',
'py_ch_2_countables',
'py_ch_3_control_statement',
'py_ch_4_functions',
'py_ch_5_OOP',
'py_ch_6_modules_packages',
'py_ch_7_exception',
'py_ch_8_file_IO',
'py_ch_9_Decorators_Generators',
'py_ch_10_GUIs',
'py_ch_11_adv_obj_DS']

# Parent Directory path
# parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

# Path
# path = os.path.join(parent_dir, directory)
for i in range (0, len(directories)):
    path = "./"+directories[i]

    # Create the directory
    try:
        os.makedirs(path, exist_ok = True)
        f = open(f"{path}/content_topics.txt", "w") # creates an empty text file
        print("Directory '%s' created successfully" % directories[i])
    except OSError as error:
        print("Directory '%s' can not be created" % directories[i])

# run windows cmd/terminal inside the working directory
# python create_folder.py

