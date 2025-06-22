
# Courses: PrTla PY for DS & ML >    14.4, 14.5  >>  details in ipynb


# --------------------------------  CLASSIFICATION example using scikit-learn  --------------------------------
# Example 1: Basic scikit-learn Classification Workflow 
#               Using the built-in "Iris dataset" and "Logistic Regression model"
# covering:
    # data loading
    # model training
    # prediction
    # performance evaluation
# with commonly used classification metrics


# 1. Import libraries
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# 2. Load dataset
# Using Iris dataset: a classic multi-class classification problem
iris = datasets.load_iris()
X = iris.data             # Features
y = iris.target           # Labels (0, 1, 2)


# 3. Split dataset into training and test sets
# 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# 4. Instantiate the classifier
model = LogisticRegression(max_iter=200)  # Ensure convergence with increased iterations


# 5. Fit (train) the model
model.fit(X_train, y_train)


# 6. Make predictions on test set
predictions = model.predict(X_test)


# 7. Evaluate performance
# Accuracy Score
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, predictions)
print("\nConfusion Matrix:\n", cm)

# Classification Report (Precision, Recall, F1-score per class)
report = classification_report(y_test, predictions, target_names=iris.target_names)
print("\nClassification Report:\n", report)


# Accuracy: Overall correctness
    # Confusion Matrix: Summary of correct & incorrect predictions for each class
    # Classification Report: Detailed metrics

    # Precision: Out of predicted positives, how many were correct.
    # Recall: Out of actual positives, how many were correctly predicted.
    # F1-score: Harmonic mean of precision and recall.




# --------------------------------  REGRESSION example using scikit-learn  --------------------------------
# Example 2: proper regression example using scikit-learn, covering:

    # Data loading
    # Model training
    # Prediction
    # Performance evaluation with key regression metrics: MSE, RMSE, MAE, and R² score


# 1. Import libraries
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 2. Load dataset
# California Housing is a good regression dataset (predicting house prices)
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

X = housing.data             # Features
y = housing.target           # Labels (median house value)

# 3. Split dataset into training and test sets
# 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Instantiate the regression model
model = LinearRegression()

# 5. Fit (train) the model
model.fit(X_train, y_train)

# 6. Make predictions on test set
predictions = model.predict(X_test)


# 7. Evaluate performance

# Mean Squared Error (MSE)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error (MSE):", mse)

# Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print("Root Mean Squared Error (RMSE):", rmse)

# Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error (MAE):", mae)

# R² Score (Coefficient of Determination)
r2 = r2_score(y_test, predictions)
print("R² Score:", r2)

