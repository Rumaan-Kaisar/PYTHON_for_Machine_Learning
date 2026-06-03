
################# 0: FULL
# copy:  
#        
#        
################# (03-Jul-26 for 05-Jul-26)

# Courses: PrTla PY for DS & ML >    1

# polish in textbook form
# compare and simplified pointwise


""" 
    ----------------    Project: Titanic dataset (Logistic Regression in Python)    ----------------

    Learning Objectives:
        Learn how to use Logistic Regression in Python.
        Build a model that predicts whether a "Titanic passenger survived or not".
        Understand the "basic steps" of a machine learning "classification project".
    
        Data-source:  https://www.kaggle.com/competitions/titanic
        Dataset:    Titanic - Machine Learning from Disaster

        
    The Titanic Dataset:
        The Titanic dataset is one of the most popular beginner datasets in machine learning.
        We're going to use a semi-cleaned version derived from the original source,

    Goal: 
        Predict whether a passenger survived the disaster. i.e. "survival status"


    ----------------    www.kaggle.com    ----------------

    Kaggle is a platform for data science and machine learning.
    This is also a online community and data science hosting Web site.
    
    What Kaggle Provides:

        Datasets:
            Thousands of datasets for practice and research. Each dataset usually includes:
                * Data files
                * Descriptions
                * Documentation

            Such as "Airplane crashes since 1908".                
            https://www.kaggle.com/datasets/saurograndi/airplane-crashes-since-1908


        Competitions:
            Companies and organizations post real-world problems.
            Participants build machine learning models to solve them.
            Rewards may include:
                * Cash prizes
                * Recognition
                * Job opportunities

        Learning Community:
                * Tutorials
                * Shared notebooks
                * Discussion forums

        Notebooks (Kernels):
            An online coding environment similar to "Google Colab" or "Jupyter Notebook".
            Write and run Python (and some other language) code directly in the browser.
            Access Kaggle datasets without downloading them locally.
            Share notebooks publicly with the community.
            Use free CPU/GPU resources (subject to limits).

                            
    --------  Dataset overview  --------

    Typical project files:
                working directory/
                ├── data_titanic_train.csv
                ├── data_titanic_test.csv
                └── pyDS_ch12_1_LgReg_ex_TTNC.ipynb

    We're going to use these two datasets to perform logistic regression in Python.
    Now let's apply some machine learning techniques to this Titanic dataset.
    



    
---- cp1



All right.
I went ahead and clear the toolbar and the header just give us some more room.
Let's go ahead and get started with our imports.
I do Panas the pie as MP and then let me go ahead and do my visualization imports.
I must say map plot lived up high plot as Piazzi I like importing seaborne as asinus.
And then since I'm using the note book I'd say map plot lib in line.
Perfect.


Well we're going to go ahead and start doing is by reading in the Titanic train c a c file into a panda
state of frame and created data from Coltrane and say PD read cxxviii and I can actually just start
typing Titanic and if I click tab here it will auto complete to the options available for me.
So in this case I want to do this titanic underscore train dot CSV run that and then I'm going to go
ahead and check the head of the data frame just to get an idea of what's in there.


It looks like we have a passenger write the column A survive which notice it's a 0 or 1 so 0 if they
did not survive what if they did survive.
P class which is the passenger class so the passengers can be in first class second class or third class
depending on where they are in the ship.
There is also the name of the passenger the sex or gender the passenger of the string male or female
.
The age of the passenger if they happen to know it.
And then this sibb s.p that indicates the number of siblings or spouses aboard and then parse S.H. indicates
the number of parents children aboard.
And then there's a ticket number a passenger fare how much they paid for their ticket.
And if we go ahead and scroll over to the right we'll see a couple more columns.
There is cabin which is the cabin they were in.
If it's known and then embarked and it's a port of impartation so see for Cherbourg.
Queue for Queenstown and as for Southampton.
All right.
Those are the basic columns.


=====================  cp 2: Dataset preview


---------------------------   Data Analysis  ---------------------------



Let's go ahead and begin some exploratory data analysis.
Now a lot of times you're going to have missing data.
We're going to go ahead and do as you see Born to create a simple heat map to see where we're missing
the most of our data.


=========== Heatmap

I'm going to go ahead and do this.
I have my training data and if I say is null as a method on it let me go ahead and just show you what
this looks like at least what part of the output looks like that is the data frames too big.
But you basically get booleans of true and false so you'll get a false if is not null.
Or a true if it is null.
So remember back to that very first cabin it was.
And so it was unknown it was null.
So it went ahead and put true there with this sort of data frame.
I can actually make a heat map so I'm going to say this and I say Asinus that heat map and then I'm
going to add a few more arguments so we don't get a bunch of tick labels.
I will say Why tick labels is equal to false.
I'm going to go ahead and say C bar is equal to false because we're not doing an actual color bar.
And then I'm going to finally pass and see map as this.
Let's go in and see what this gives us.
All right.
So notice what I've created here.
I've created a heat map of those boolean values those true and false statements and due to this.
See map does color mapping every yellow dash here basically stands for a true point where true it was
null.
So we can just glimps now order data from a very far bird's eye view and check out that yes we're missing
some age information are missing a lot of Cabane information and we're missing just essentially one
row of embarked roughly about 20 percent of that age data is missing and the proportion of age missing
is likely small enough for a reasonable replacement of some form of imputation meaning I can actually
use the knowledge of the other columns to fill in reasonable values for that age column.
Looking at the cabin column however it looks like we're just missing too much of that data to do something
useful with it at a basic level.
We're going to go ahead and probably drop this later or change it to send up some other feature like
Cabane known 1 or 0.

=====================  cp 3: Heatmap of Missing data


---- cp2


---- cp3


---- cp5



"""

