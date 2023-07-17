from dotenv.main import load_dotenv
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import mysql.connector
import requests

# Testing mysql library (not relevant to requests library)
db = mysql.connector.connect(
    host=os.environ.get('VITE_DB_HOST'),
    user=os.environ.get('VITE_DB_USER'),
    password=os.environ.get('VITE_DB_PASSWORD'),
)

def save_result(result):
    # Example data JSON (not actual one)
    new_data = {
        "<column-1>": 0,
        "<column-2>": result,
    }
    # Example REST API endpoint (not actual one)
    url_post = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test-3"
    headers = {
        "content-type": "application/json",
    }
    # Send POST request.
    post_response = requests.post(url_post, json=new_data, headers=headers)
    post_response_json = post_response.json()
    print(post_response_json)

def main():
    # Get data
    url_get = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test"
    get_response = requests.get(url_get)
    get_response_json = get_response.json()
    predict_model(get_response_json)

def predict_model(json):
    # Read data
    df = pd.DataFrame(json)

    # DEVELOPMENT ONLY - Display data retrieved from REST API endpoint.
    #print(df.to_string())
    #return

    # Target
    target_column = ['<insert target column>']

    X = df['<insert parameter column>'].values
    y = df[target_column].values.ravel()

    X = X.reshape((-1, 1))
    y = y.reshape((-1, 1))

    # Split data into train and test.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Scale the data
    scaler = StandardScaler()
    scaler.fit(X_train)
    scaler.fit(y_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    y_train_scaled = scaler.transform(y_train)
    y_test_scaled = scaler.transform(y_test)

    # Apply linear regression using train data.
    model = LinearRegression()
    model.fit(X_train_scaled, y_train_scaled)

    # Make prediction using test data.
    y_pred = model.predict(X_test_scaled)
    #print(y_pred)
    single_pred = model.predict(X_test_scaled[0].reshape(-1, 1))
    save_result(single_pred)

    # DEVELOPMENT ONLY - Show scatter plot of the data.
    plt.scatter(X_test_scaled, y_test_scaled, color="black")
    plt.plot(X_test_scaled, y_pred, color="blue", linewidth=3)
    plt.show()

    # DEVELOPMENT ONLY - Examples of metrics.
    print("Mean squared error: %.2f" % mean_squared_error(y_test_scaled, y_pred))
    print("Coefficient of determination: %.2f" % r2_score(y_test_scaled, y_pred))
    print("Accuracy on training set: {:.2f}".format(model.score(X_train_scaled, y_train_scaled)))
    print("Accuracy on test set: {:.2f}".format(model.score(X_test_scaled, y_test_scaled)))
    print("Mean absolute percentage error: %.2f" % mean_absolute_percentage_error(y_test_scaled, y_pred))

if __name__ == "__main__":
    load_dotenv()
    main()