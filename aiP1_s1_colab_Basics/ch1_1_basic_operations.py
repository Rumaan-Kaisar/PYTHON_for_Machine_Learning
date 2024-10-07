
# checking python
!python --version
!pip --version
!pip list


# install other versions for example:   python 3.5
!sudo apt-get update -y
!sudo apt-get install python3.5



# --------  connect to Google drive  --------
# Run the following code to mount your Google Drive to Colab:
from google.colab import drive
drive.mount('/content/drive')

# You'll see a URL -> select your Google account, and allow Colab to access your Google Drive.
# You'll get a code. Copy it and paste it back into the Colab cell
# Now Google Drive is mounted and accessible in the "/content/drive/" directory.

# mount to a "custom path". Say we want to mount at: "/content/drive/MyDrive/_MLDL"
from google.colab import drive
drive.mount('/content/drive/MyDrive/_MLDL')


# ----  interact  with the files  ----
!ls /content/drive/MyDrive/
# Access folder "Colab Notebooks" using the following path:
# Note: The backslash (\) is used before spaces in the folder name, i.e., Colab\ Notebooks
!ls /content/drive/MyDrive/Colab\ Notebooks

# ---- current working directory  ----
!pwd    # displays the full path of the current working directory in the Colab environment

# If you want to change directories:
%cd /content/drive/MyDrive/Colab\ Notebooks
!pwd    # current working directory now changed
!ls     # list the file contents of the current working directory



# - - - -    preview the dataset    - - - -
import pickle

# Open the pickle file in read-binary mode
with open('./all_data_5.pickle', 'rb') as file:
    data1 = pickle.load(file)

# Now, the 'data' variable contains the contents of your pickle file
print(data1)

# - = - = - = -    Advanced    - = - = - = -
# Open Compressed Pickle
    # Sometimes, pickle files are compressed, then you need to decompress it first. 
    # It could use different methods, for example: zlib, gzip, bz2. We can use:
            # zlib.decompress()
            # gzip.decompress()
            # bz2.decompress()

import pickle
import zlib

# Open the compressed pickle file
with open('./all_data_5.pickle', 'rb') as file:
    # Step 1: Read the binary content
    compressed_data = file.read()
    
    # Step 2: Decompress the binary content
    decompressed_data = zlib.decompress(compressed_data)
    
    # Step 3: Unpickle the decompressed data
    data = pickle.loads(decompressed_data)

print(data)


# ----  view images  ----
image_prev = data['images']
label_prev = data['label']
print(image_prev.shape)
print(label_prev.shape)

"""  
    (27558, 36, 36, 3): This refers to the shape of image_prev. 
        It contains 27,558 images, 
        each of size 36x36 pixels, 
        with 3 color channels (likely RGB).

    (27558,): This refers to label_prev, which contains 27,558 labels, with one label for each image. 
        The shape (27558,) indicates that it is a one-dimensional array of labels.
"""


# ----  images  ----
# To preview images from your dataset in a grid format using matplotlib and seaborn, 
# you can use plt.imshow() to display each image and organize them in subplots.
import matplotlib.pyplot as plt

# Create subplots
fig, axes = plt.subplots(20, 40, figsize=(80, 40))  
# creates a grid of subplots arranged in 20 rows and 40 columns 
# with the overall figure size specified as 80 inches wide and 40 inches tall.

for i, ax in enumerate(axes.flat):
    # Display an image
    ax.imshow(image_prev[i])  # Display the i-th image
    ax.axis('off')            # Turn off axis labels/ticks

plt.show()

"""  
    The figsize=(80, 40) specifies the "overall size" of the "entire figure" (not the size of each individual subplot).
    Each subplot will have its own dimensions based on the figure size divided by the number of rows and columns:
"""


