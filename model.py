import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import joblib

# Load your dataset
df = pd.read_csv('BMI.csv')

df.head()
print(df.columns)

# Preprocessing: Convert categorical variables into numerical format if needed
gender_map = {'Male': 0, 'Female': 1}

# Apply mapping using map function
df['Gender'] = df['Gender'].map(gender_map)
print(df.head())

# # Split data into features (X) and target variable (y)
X = df[['Height', 'Weight', 'Gender']]
y = df['Index']

# print(X)

# # Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# # Choose a model and train it
model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, 'bmi_model.pkl') 

# # Make predictions on the test set
y_pred = model.predict(X_test)

# # Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)
