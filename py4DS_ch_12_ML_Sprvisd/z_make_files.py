# import os

# Directory: List of the folders you want to create

file_names = ['pyDS_ch12_1_LgReg',
'pyDS_ch12_2_KNN',
'pyDS_ch12_3_DcsnTre_RndFst',
'pyDS_ch12_4_SVM',
'pyDS_ch12_5_KMeans_Clstr',
'pyDS_ch12_6_PCA']



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
            f.write("\n################# 0: FULL\n# copy:  \n#        \n#        \n################# (16-Dec-25 for 17-Dec-25)\n\n# Courses: PrTla PY for DS & ML >    1\n")
        print(f"{file_names[i]}.py is created sucuessfully")
    except:
        print("files '%s' can not be created" % file_names[i])

# run windows cmd/terminal inside the working directory
# python z_make_files.py


"""  
    ----  File structure  ----

    pyDS_ch11_1

1. Logistic Regression
2. K Nearest Neighbors
3. Decision Trees and Random Forests
4. Support Vector Machines
5. K Means Clustering
6. Principal Component Analysis


----  compressed, vowel-reduced shorthand  ----
LgReg
KNrstNbr
DcsnTre_RndFst
SprtVctMch
KMeNsClstr
PrncplCmpAnl

pyDS_ch12_1_LgReg
pyDS_ch12_2_KNN
pyDS_ch12_3_DcsnTre_RndFst
pyDS_ch12_4_SVM
pyDS_ch12_5_KMeans_Clstr
pyDS_ch12_6_PCA

"""

