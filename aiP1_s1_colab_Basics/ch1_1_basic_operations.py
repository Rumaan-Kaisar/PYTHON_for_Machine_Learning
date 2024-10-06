
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



