
################# 15.1:
# copy: 2 data, py, ipynb
#       
#   
#
################# (01-Jul-25 for 02-Jul-25)

# Courses: PrTla PY for DS & ML >  15.1 (ipynb), 15.3, 15.4, 15.5, 14.6  >>  details in ipynb

# a clear, pointwise simplification with mid-ground details while preserving full context:
# Use folloing as interactive note-code


""" 
    Project 1:
        Now we'll use scikit-learn in Python to create a linear regression model.

        After that, we'll work on your own portfolio project exercise, and once completed, the solutions will be reviewed and discussed.

"""


Linear Regression with Python: Practical Implementation

# Data exploration
After covering the theory behind linear regression, it’s time to implement a linear regression model using scikit-learn in Python. The initial focus will be on working with a housing dataset to predict housing prices based on various features. As this is an introductory implementation, emphasis will be placed on getting the basic workflow correct rather than complex data cleaning, which will be addressed later.

To begin, the necessary libraries are imported: pandas and numpy for data manipulation, along with matplotlib and seaborn for data visualization. For displaying plots within Jupyter Notebooks, %matplotlib inline is also set.

The dataset is loaded into a Pandas DataFrame using pd.read_csv(). This housing dataset contains several columns: each row represents a house, with columns including the address, the price the house was sold for, and various city-level statistics such as population, average number of bedrooms and rooms, average house age, and average income. It’s important to note that the address values are artificially generated for demonstration purposes.

Before proceeding with modeling, it's good practice to inspect the dataset. The .info() method provides an overview of the data types and number of entries for each column. The .describe() method offers summary statistics for the numeric columns, including mean, minimum, maximum, and standard deviation. If needed, the column names can be listed using df.columns.

To visualize and explore the data, simple plots can be created. One effective option is using Seaborn's pairplot() function, which generates histograms for each variable and scatter plots for each pairwise combination of columns. This reveals general distributions and potential relationships between features. For example, the average number of bedrooms appears segmented, typically between 2 to 6 bedrooms.

Next, it’s useful to examine the distribution of the target variable — in this case, house prices. A distribution plot shows that the prices are roughly normally distributed, centered around $1 million to $1.5 million. This kind of visualization helps identify whether target values are skewed or normally distributed, although this dataset happens to be clean.

Another valuable step is to generate a heatmap of the correlation matrix. The .corr() method computes the pairwise correlation coefficients between all numeric columns. This matrix can be visualized using Seaborn's heatmap(), where higher values indicate stronger linear relationships between variables. The diagonal of the heatmap naturally shows a perfect correlation of 1 for each feature with itself. Including annotations with the actual correlation values (annot=True) helps in assessing these relationships numerically.

Once data exploration is complete, the next step is to focus on applying scikit-learn to train a linear regression model. This will involve defining the feature and target variables, splitting the data into training and test sets, creating and fitting the regression model, making predictions, and finally evaluating the model’s performance.

This structured workflow forms the foundation for supervised learning tasks using regression in Python.



The first step in building a linear regression model is to split the dataset into two parts: one containing the feature variables (X) used for training, and another containing the target variable (y) that the model will learn to predict. In this case, the Price column is the target variable. The Address column is excluded because it contains text data that linear regression cannot handle directly. Later, techniques such as Natural Language Processing (NLP) can be applied to process textual information, but for now, it is removed from the model.

The feature columns are selected by accessing the list of column names and excluding the target variable and irrelevant columns. The feature set X is then created from these selected columns, while y is assigned the values from the Price column.

Once the features and target variables are prepared, the next step is to split the data into a training set and a testing set. The training set is used to train the model, while the testing set evaluates the model’s performance on unseen data. This split is performed using scikit-learn’s train_test_split() function, which can be imported from sklearn.model_selection.

When using train_test_split(), the feature data X and target data y are passed as arguments, along with a test_size parameter, which defines what proportion of the data should be reserved for testing. A common choice is 30% or 40%. Additionally, specifying a random_state ensures that the random splitting of the data is reproducible — meaning the same split will be generated every time the code is run with the same value, providing consistent results for debugging and comparison.

For example, setting test_size=0.4 allocates 40% of the data for testing, while random_state=101 ensures consistent splits. The function returns four outputs: X_train, X_test, y_train, and y_test, representing the feature and target data for both training and testing sets.

After splitting the data, the next step is to create and train the linear regression model. This is done by importing the LinearRegression class from sklearn.linear_model. The model can then be instantiated and fitted to the training data.

This structured workflow — preparing data, splitting into training and testing sets, creating the model, and training it — forms the foundation for building reliable supervised learning models using scikit-learn in Python.



Once the LinearRegression model is imported from scikit-learn, the next step is to instantiate it by creating an instance of the LinearRegression class. This instance serves as the linear regression model object. By calling the .fit() method on this object, the model can be trained on the prepared training data. The fit() method takes two arguments: the training features X_train and the corresponding target values y_train. Once executed, the model is trained and ready for evaluation. It is important to note that this method modifies the model object in place and does not need to be assigned to a new variable.

After fitting the model, its learned parameters can be examined. The model’s intercept is accessed through the .intercept_ attribute, representing the predicted value when all features are zero. The coefficients for each feature are available via the .coef_ attribute, providing insights into how changes in each feature influence the predicted target variable.

For better readability, these coefficients can be organized into a pandas DataFrame, associating each coefficient value with its corresponding feature. This structured view helps interpret how each independent variable affects the dependent variable. For example, a positive coefficient indicates that increasing the corresponding feature leads to an increase in the predicted value, assuming all other features remain constant. Similarly, a negative coefficient would imply a decrease in the predicted value.

In this artificial dataset, interpreting these coefficients may not yield meaningful insights since the data is randomly generated. However, in practical applications using real datasets, this analysis can reveal valuable relationships. A recommended alternative for working with realistic housing price data is the Boston Housing Dataset, a classic dataset commonly used in regression problems.

The Boston dataset can be loaded from scikit-learn using from sklearn.datasets import load_boston. This function returns a dictionary-like object containing the dataset’s features, target values (housing prices in thousands of dollars), and descriptive details. By accessing .data, .feature_names, and .target, one can retrieve the dataset's feature matrix, column names, and target values, respectively. Although this dataset is somewhat outdated, it provides a reliable starting point for regression analysis on real housing data.

To summarize the workflow so far:

The dataset was loaded using pandas.

Basic exploratory data analysis was performed.

The data was divided into features (X) and the target variable (y).

The data was split into training and testing sets using train_test_split from sklearn.model_selection, with specified test_size and random_state values for reproducibility.

A linear regression model was created and trained on the training set.

The model’s intercept and coefficients were examined and organized for easier interpretation.

An example was provided on how to access and analyze a real dataset using scikit-learn’s load_boston function.

In the next step of the analysis, predictions will be generated from the trained model using the test data, and the model’s performance will be evaluated by comparing these predictions with the actual target values.




-------------------------------------------
PART 2:

In the second part of the linear regression workflow, the focus shifts to generating predictions from the trained model. After creating and fitting the linear regression model to the training dataset, the next step is to use this model to predict target values based on new, unseen data — specifically, the features from the test dataset.

To make predictions, the .predict() method of the trained model is called, with the test feature set (X_test) passed as an argument. This generates an array of predicted values corresponding to the test data. Since the original dataset was split into a training and test set, the true values for the test set are stored in y_test. Comparing these true values against the model's predictions helps assess the model's accuracy.

A quick and useful way to visualize this comparison is by creating a scatter plot of the actual target values (y_test) against the predicted values. Ideally, if the model performed perfectly, the points would lie along a straight diagonal line. A well-performing model will show points clustering closely around this line, indicating accurate predictions.

Another important diagnostic step is to examine the distribution of residuals — the differences between the actual values and the predicted values. This can be visualized using a histogram of residuals, calculated as y_test - predictions. If the residuals are roughly normally distributed, it suggests that the linear regression model is an appropriate fit for the data. An abnormal distribution of residuals, on the other hand, may indicate issues with the data or suggest that a different type of model would be more suitable.

Finally, evaluating the model numerically involves calculating standard regression evaluation metrics. There are three commonly used metrics for this purpose: Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). These metrics quantify the average difference between predicted and actual values in various ways, providing a clearer understanding of the model's performance.

This structured workflow — generating predictions, visualizing actual vs. predicted values, analyzing residuals, and applying quantitative performance metrics — forms the basis for assessing and refining regression models in practical machine learning tasks.


There are three commonly used evaluation metrics for regression problems: Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). These metrics measure the difference between predicted and actual values in various ways, providing insight into the model’s accuracy.

Mean Absolute Error (MAE) is the simplest to interpret. It represents the average of the absolute differences between predicted values and the actual values. This gives a straightforward measure of the model’s average error.

Mean Squared Error (MSE), on the other hand, calculates the average of the squared differences between the predicted and actual values. Squaring the errors penalizes larger errors more severely, making MSE particularly useful in real-world applications where larger errors are more problematic.

Root Mean Squared Error (RMSE) is the square root of the MSE. It is often preferred because it expresses the error in the same units as the target variable, making it more interpretable in practical terms. Like MAE and MSE, RMSE serves as a loss function that the model aims to minimize.

These metrics can be easily computed in Python using the sklearn.metrics module. The mean_absolute_error() and mean_squared_error() functions accept the true target values and the model’s predictions as inputs. The RMSE can be calculated by taking the square root of the MSE using NumPy’s sqrt() function.

Once the evaluation metrics are computed, they provide a clear numerical summary of the model’s performance on the test data. Lower values for these metrics indicate a better-fitting model.

The full workflow of this linear regression implementation involves several steps: importing the necessary libraries, loading and inspecting the data, splitting it into training and testing sets, fitting a linear regression model, making predictions, and then evaluating those predictions both visually (using residual plots and scatterplots) and numerically (using regression metrics).

This process demonstrates the fundamental cycle of building and assessing a supervised machine learning model. To extend this practice, learners are encouraged to apply the same workflow on real datasets such as the Boston housing dataset or datasets from sources like Kaggle. These exercises help reinforce concepts and develop skills for applying machine learning to real-world data problems.
