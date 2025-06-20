
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




# Example 3: Basic scikit-learn Process for Regression

# 1. Import necessary libraries and modules
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# 2. Create the model (estimator)
    # Note: 'normalize' is deprecated in recent versions of scikit-learn — will raise a warning or error.
            # Correct modern usage: just instantiate the model without 'normalize'
            # model = LinearRegression(normalize=True)

model = LinearRegression()  # Create a Linear Regression model

# 3. Check the model's default parameters settings
print(model)
print(model.get_params())


# 4. Create dataset
    # Features (X) — a 5x2 array, Labels (y) — a list of 5 values
X = np.arange(10).reshape((5, 2))   # 5 samples, 2 features per sample
y = np.arange(5)                    # Numeric labels: 0, 1, 2, 3, 4

print("\nX:\n", X)
print("\ny:\n", y)


# 5. in one line (Optional): You can also create both X and y in one line:
    # X, y = np.arange(10).reshape((5, 2)), np.arange(5)


# 6. Split the dataset into training and testing sets
    # test_size=0.3 means 30% test data, 70% training data
    # random_state=42: Sets the random seed so that the split is reproducible 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Display the splits
print('\nX_train:\n', X_train)
print('\nX_test:\n', X_test)
print('\ny_train:\n', y_train)
print('\ny_test:\n', y_test)


# 7. Train (fit) the model on training data
model.fit(X_train, y_train)


# 8. Make predictions on the test set
predictions = model.predict(X_test)


# 9. Display predictions
print('\nPredictions on X_test:\n', predictions)


# 10. (Optional) Evaluate model performance. Eg: R² score
score = model.score(X_test, y_test)
print("\nModel R² score on test set:", score)


