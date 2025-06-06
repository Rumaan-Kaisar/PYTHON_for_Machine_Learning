
################# 14.1: FULL, 14.3: FULL, NXT >> 14.6 after 14.4, 14.5
# copy: Analyze: analyze this text, get the topics, 
#       output in english: describe the topics on your own knowledge withot losing context, use clarification and fix any misconception (mention them)
#   
#
################# (02-May-25 for 03-May-25)

# Courses: PrTla PY for DS & ML >    14.1, 14.3, 14.6

""" 
    Each Machine Learning algorithm we cover in this section will follow 4 parts:
        A short theory lecture.
        Reading assignment (optional)
        A implementation in Python
        A project exercise/solutiom for portfolio



GPT: Give a simple example of ML pipeline for supervised learning, give a simple short code for better understanding


"""


# ------------    Simple ML Pipeline Example: Predict House Prices    ------------

# Example 1: Simple example of a basic ML pipeline for supervised learning using scikit-learn with a linear regression model:

# A very compact supervised ML pipeline in Python.
        # Get Data & Libraries
        # Train-Test Split
        # Model Training (Linear Regression)
        # Prediction
        # Performance Metric (MSE)

# Dataset & Libraries :
# Sample data (house size in sqft vs. price in $1000)

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {'Size': [2100, 1600, 2400, 1416],
        'Price': [399.9, 329.9, 369.0, 232.0]
        }

df = pd.DataFrame(data)


# Step 1: Data Split
X = df[['Size']]   # features
y = df['Price']    # target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# Step 2: Model Training
model = LinearRegression()
model.fit(X_train, y_train)


# Step 3: Prediction
predictions = model.predict(X_test)


# Step 4: Evaluation
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)




# Example 2: Here's another example of a machine learning pipeline for supervised learning using 
    # the Iris dataset and 
    # scikit-learn

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# 1. Load dataset
iris = load_iris()
X, y = iris.data, iris.target


# 2. Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 3. Create ML pipeline
# This pipeline first scales the data, then applies a classifier
pipeline = Pipeline([
    ('scaler', StandardScaler()),      # Data preprocessing step
    ('classifier', RandomForestClassifier())  # Model training step
])


# 4. Train the model
pipeline.fit(X_train, y_train)


# 5. Make predictions
y_pred = pipeline.predict(X_test)

# 6. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")



# ------------    Key Steps in the Pipeline:    ------------

# 1. Data Loading: Load the dataset (Iris in this case)
# 2. Data Splitting: Divide into training and test sets
# 3. Pipeline Creation:
    # a. Preprocessing: Standardize features (mean=0, variance=1)
    # b. Model: Random Forest classifier
# 4. Model Training: Fit the pipeline on training data
# 5. Prediction: Make predictions on test data
# 6. Evaluation: Assess model performance

# NOTE: real-world pipelines often include more steps like 
    # feature engineering, 
    # hyperparameter tuning, and 
    # cross-validation.



""" 
    ------------------------    ML/DL Pipeline    ------------------------

    1. What is a ML/DL Pipeline?
        A ML or DL pipeline is a sequence of steps that takes raw data and turns it into a trained model ready for predictions. 
        Common steps are:

            * Data preprocessing (cleaning, scaling, feature engineering)
            * Model training
            * Model evaluation
            * Deployment

        In deep learning, extra steps like neural network design and GPU use are added.

        

    2. Why is it called a Pipeline?
        Like an industrial pipeline moves materials through stages, a ML pipeline moves data through steps. 
        Each step processes data or the model, passing its output to the next step. Example:
    
            Raw Data -> Cleaned Data -> Scaled Data -> Trained Model -> Predictions

            

    3. Why is it Important?

            * Standardizes the workflow
            * Reduces errors
            * Enables automation
            * Improves reproducibility
            * Makes deployment easier
            * Saves time by avoiding repetitive manual steps

    Analogy: like a car assembly line where each step must happen in order for the final product to be complete.

    
    ------------------------------------------------------------------------------------------------------------

    What is Pipeline from sklearn.pipeline?
        The "Pipeline" class in scikit-learn links multiple processing and modeling steps into one object. 
        It ensures steps run in order and makes ML workflows cleaner and safer.

        What does it do?

            * Runs a series of transformers (like scalers) followed by a final model.
            * Keeps the correct order.
            * Offers one interface for fit, predict, and score on the entire sequence.
            * Prevents data leakage by keeping test data separate from training transformations.
            * Supports easy hyperparameter tuning with tools like GridSearchCV.

        Example:
                pipeline = Pipeline([
                    ('scaler', StandardScaler()),      # Data preprocessing step
                    ('classifier', RandomForestClassifier())  # Model training step
                ])
    
            Data passes through the "scaler", then to the "model".


        WHY use it?

            * Cleaner, safer code
            * Prevents bugs and data leakage
            * Easier to reproduce results
            * Easier to deploy as one packaged object
            * Simplifies tuning model and preprocessing settings together

            
        WHEN should you use it?
            Almost ALWAYS, especially when:

            * Multiple preprocessing steps exist
            * You want to avoid data leakage
            * Hyperparameter tuning is needed
            * Planning to deploy the model

"""



Hello everyone and welcome to the machine learning of Python lecture.

Now that we've gotten an introduction to machine learning is in this lecture we're going to discuss

how we're going to be using Python and the sikat learn package to perform machine learning with Python

.

Like I mention we're going to be using the sikat learn package.

It's the most popular machine learning package for Python and it has a lot of algorithms already built

into it.

You'll need to install it at your command line or terminal using Konda install sikat learn if you have

an anaconda distribution or install sikat dasht learn if you have another distribution in Python.

Let's talk about the basic structure of how to use sikat learn first.

A quick review of the machine learning process the machine learning process starts off with your data

.

Somehow you need to acquire data and then the next step usually is to clean that data and format it

so that the machine learning model can accept that before you actually give it to the machine learning

model however you're going to split that clean the data into a test set and a training set.

Your train your model or the training set and then in the next step you test your model on the test

set and you iterate your model and tune the parameters of your model until it's ready to deploy.

Now let's go over an example of the process to use psychic learn.

Now don't worry about memorizing any of this.

We're going to get plenty of practice and review all of this when we actually start coding in subsequent

lectures.

This lecture is just the overview of the sikat learn process.

Don't worry about memorizing all the steps you're going to see these steps over and over and will walk

you through each of these steps.

We're actually coding out the algorithms.

This is just an overview so you don't see it for your first time when you're actually coding out all

right every algorithm in sikat learn is exposed via an estimator object.

First you'll import the model and the general form of this is to say from S-K learn family import model

.

So a specific example would look like this.

Let's say we want to perform a linear regression which is going to be the first machine learning algorithm

we learn about.

We'll go ahead and say from S-K learn linear underscore a model where it linear underscore model is

the family of models import and then linear regression and that linear regression is that estimator

object that's the model itself and then the next that is to instantiate that model or estimator.

So the estimator parameters all the parameters of an estimator can be set when it's instantiated in

all of them have suitable default values.

Later on we're going to explore these values and these parameters using shift time in the Jupiter notebook

.

Check all the possible parameters.

For example you can instantiate a linear regression model by specifying a parameter to be normalized

equals true and then after printing the model you just instantiated.

You can go ahead and check out the parameters that were defaulted to the model such as the intercept

true and copy sequel's true again you actually don't need to specify normalized as equal to true.

Those are just additional parameters you can use to tune the model to something more specific.

Once you have your model created your parameters it's time to fit your model on some data.

But remember we should split this data into a training set and a test set.

Let's go over an example of how we can do that.

I'm going to go ahead and say important umpires and P in order to create some fake data then we can

use sikat learn to do a train test split splitting our data into a training set and a testing set is

the same for mid-scale learn cross underscore validation in poor train tests.

Then we're have our sets of data.

X and Y or X are the actual features and Y is the actual label for each of those feature rows using

train to split.

You pasan X and Y and you passin the test size.

Then again don't worry too much about fully memorize this or even fully understanding it.

We're going to get a lot more practice with this process later on but just as an overview you can use

train test split on your features and labels and sikat learn will automatically output your training

set and your testing set.

So we have X train and a white train and then X test and white test and you can see how these arrays

are outputted here.

Basically you just have your labels for your training and testing data as well as your features for

your training and testing data.

Now that we have split the data we can train or fit our model on the training data.

And this is done through the model fit method.

Basically you take your model.

Remember we instantiated it as a linear regression estimator and then you say model fit and you pass

in your training data you pass in your X training data which the features of your data and then you

passen your y training data which are the training labels.

Now the model has been fit and trained on the training data and the models rates predict labels or values

on the test set.

Keep in mind I'm showing an example of a supervised learning process.

The process for an unsupervised model is going to be a little different because you're actually not

going to have those labels very supervised learning model.

We get the predicted values using the Predict method.

They'll go ahead and say model but predict.

Passing your test data those are your test features and predictions off of that.

Then you can evaluate our model by comparing our predictions to the correct values.

The evaluation method depends on what sort of machine learning algorithm you are using different evaluation

methods are used for regression vs classification vs clustering etc..

Let's go ahead and get a quick recap of all of this.

Sikat learn really strives to have a uniform interface across all methods and we're going to see examples

of these below.

Even a psych estimator object named model these following methods are available on all estimators.

You're going to be able to fit to the training data then for supervised learning applications.

This is going except to arguments the data X and the labels.

Why for unsupervised learning applications this only accepts a single argument.

The data which makes sense because unsupervised learning works of unlabeled data that I'm supervised

.

Estimators you're going to have a predict method which given a trains model is going to predict the

label of a new set of data.

This method accepts one argument the new data which is going to be X underscore new.

In this example or in the previous example it was x underscore.

Test.

And then this returns the learned label for each object in the array.

Also available unsupervised supervised estimators The predict underscore prob the method and then for

classification problems some estimators provide that method which returns the probability that a new

observation has in each categorical label.

In this case the label of the highest probability is returned by model predict method

reclassification or regression problems.

You also have a score method available and most in most estimators implement this method and scores

are between 0 and 1 with a larger score indicating a better fit.

Also available in unsupervised estimators is the model not predict which is going to allow us to predict

labels in clustering algorithms

in unsupervised meters.

You also have modeled but transform where given an unsupervised model you can transform new data into

the new basis.

Now we'll get a lot more into this when we talk about unsupervised learning algorithms.

But basically this also accepts one argument.

This X new and returns the new representation of the data based off of the unsupervised model again

will get a lot more into this and in-depth and actually explain this in a lot more detail when we talk

about unsupervised machine learning problems.

Finally we have modeled fit underscore transform unsupervised estimators some estimators implement this

method which more efficiently performs a fit in a transform on the same input data.

Right now you may be wondering well how do I choose an algorithm classification versus regression versus

clustering.

If you go ahead and just google search sikat learn algorithm cheat sheet you should get an image that

looks like this.

And this is from the official sikat learned documentation.

But basically this is a bit of a decision tree or a walkthrough guide on how to actually go about choosing

an algorithm and if we go ahead and start off you'll see that it asks you the more than 50 samples.

If not you should really get more data.

If you do have more than 50 samples then asks you Are you trying to predict the category predict the

quantity.

Whether your label is data.

Cetera.

All right.

Let's go ahead and start using Python for machine learning by starting our first machine learning algorithm

which is going to be linear regression.

Thanks everyone and I'll see you at the next lecture

