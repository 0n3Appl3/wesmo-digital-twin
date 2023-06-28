import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from dotenv.main import load_dotenv
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

def main():
    # Test retrieving data from database.
    url_post = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test"
    headers = {
        "content-type": "application/json",
    }
    get_response = requests.get(url_post, headers=headers)
    get_response_json = get_response.json()
    print(get_response_json)

    # Load diabetes data (test).
    X, y = load_diabetes(return_X_y=True)
    # Show that the data has been loaded correctly.
    print(X.shape)
    print(X[0])

    # Extract column at index 2.
    X = X[:, 2]
    print(X.shape)
    # Reshape to a 2D array.
    X = X.reshape((-1, 1))
    print(X.shape)

    # Split data into training and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create Linear Regression model and train with the train data.
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict using test data after training.
    y_pred = model.predict(X_test)
    print(y_test)
    print(y_pred)
    # Metric to compare how close are the predicted vs actual values
    # Currently returns a large MSE. Possibly check for outliers (standardscaler), check parameters.
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))

    # Create scatter plot and display.
    plt.scatter(X_test, y_test, color="black")
    plt.plot(X_test, y_pred, color="blue", linewidth=3)
    plt.xlabel("Scaled BMIs")
    plt.ylabel("Disease Progression")
    plt.title("A Graph Plot Showing Diabetes Progression Against BMI")
    plt.show()

if __name__ == "__main__":
    load_dotenv()
    main()