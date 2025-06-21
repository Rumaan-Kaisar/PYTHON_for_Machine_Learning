
################# 14.4, 14.5: FULL
# copy: Analyze: analyze this text, get the topics, 
#       output in english: describe the topics on your own knowledge withot losing context, use clarification and fix any misconception (mention them)
#        
################# (18-Jun-25 for 20-Jun-25)

# Courses: PrTla PY for DS & ML >    14.4, 14.5

# make a sample scikit-learn used "classification" ml code with basic steps and proper dataset
# main focus is performance analysis demonstration
# evaluation process


# CHECKPOINT 1/2

# rev[17-Jun-2025]

# Excellent request — let's build a clean, practical **classification example using scikit-learn**, covering **data loading, model training, prediction, and performance evaluation** with commonly used classification metrics.



# Example: Basic scikit-learn Classification Workflow

# Using the built-in Iris dataset and Logistic Regression model**


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

