import os

# Directory: List of the folders you want to create
directories = ["py4DS_ch_1_basics",
"py4DS_ch_2_dataFrame",
"py4DS_ch_3_matrices",
"py4DS_ch_4_VIZ_p1"]

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

# "py4DS_ch_1_basics",
# "py4DS_ch_2_dataFrame",
# "py4DS_ch_3_matrices",
# "py4DS_ch_4_VIZ_p1"