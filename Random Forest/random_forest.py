# -*- coding: utf-8 -*-
"""rf_multi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jDjZkpnCnFsFBmUEH8bDz67X8ouH6EVe
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv("kaggle.csv")  # Replace with the path to your dataset

# Extract features (X) and label (y)
X = data.iloc[:, 2:]  # Select columns from the 3rd column onwards
y = data.iloc[:, 1]   # Select the 2nd column as the label

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=200, criterion='gini', min_samples_split=2, max_depth=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.5f}")

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt

# Obtain the confusion matrix on the testing data
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Calculate the accuracy score on the testing data
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Perform cross-validation on the training data
cv_scores = cross_val_score(rf_classifier, X_train, y_train, cv=5)
print("Cross-Validation Scores:")
print(cv_scores)
print("Average Accuracy:", cv_scores.mean())

# Evaluate the model
accuracy_value = accuracy_score(y_test, y_pred)
classification_report_str = classification_report(y_test, y_pred, digits=5)

# Print the results
print(f'Accuracy: {accuracy_value:.5f}')
print(f'Classification Report:\n{classification_report_str}')