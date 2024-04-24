
# # Split data into features (X) and target variable (y)
# X = data[['Height', 'Weight', 'Gender']]
# y = data['Index']

# print(X)

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# # Choose a model and train it
# model = LinearRegression()
# model.fit(X_train, y_train)

# joblib.dump(model, 'linear_regression_model.pkl')

# # Make predictions on the test set
# y_pred = model.predict(X_test)

# # Evaluate the model
# mse = mean_squared_error(y_test, y_pred)
# print('Mean Squared Error:', mse)