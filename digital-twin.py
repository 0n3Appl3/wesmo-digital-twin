from dotenv.main import load_dotenv
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import threading
import requests
import asyncio
import socketio
import random

error_prefix = "[ERROR] "

# Create a new Async Socket IO server
sio = socketio.AsyncClient()

#
# Event fires when 'event' packet is received from the server.
#
@sio.event
async def event(data):
    print("Message received: ", data)
    # Pretend results are processed for digital twin and send to server and then to all connected web browser clients
    sio.emit("send-twin-results", random.randrange(1, 100, 2))
    # main()

#
# Connects to the battery dashboard backend server.
#
async def connect_to_backend():
    test_sql()
    try:
        await sio.connect(os.environ.get('VITE_BACKEND_URL'))
        await sio.wait()
    except Exception as error:
        print_error("A connection error has occurred!", error)

#
# TEMPORARY: Testing GET requests to the backend server.
#
def test_sql():
    url_get = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test"
    headers = {
        "content-type": "application/json",
    }
    try:
        get_response = requests.get(url_get, headers=headers)
        get_response_json = get_response.json()
        print(get_response_json)
    except requests.ConnectionError as error:
        print_error("A connection error has occurred!", error)

def print_error(message, error):
    global error_prefix
    print("-------\n" + error_prefix + message +
          "\n\n" +
          str(error) +
          "\n-------")

def save_result(result):
    # Example data JSON (not actual one)
    new_data = {
        "id": "null",
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

#
# NOT YET TESTED
#
def predict_neural():
    #
    # NOTE: Data normalisation and scaling not yet taken into account.
    #

    # # Read data
    # df = pd.DataFrame(json)

    # # Target
    # target_column = ['<insert target column>']

    # X = df['<insert parameter column>'].values
    # y = df[target_column].values.ravel()

    # X = X.reshape((-1, 1))
    # y = y.reshape((-1, 1))
    X, y = make_regression(n_samples=1000, n_features=4, random_state=1)

    # Split data into train and test.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    # Scale the data
    # scaler = StandardScaler()
    # scaler.fit(X_train)
    # X_train_scaled = scaler.transform(X_train)
    # X_test_scaled = scaler.transform(X_test)

    pipe = Pipeline([
        ("scale", StandardScaler()),
        ("model", MLPRegressor(hidden_layer_sizes=3, random_state=1, max_iter=15000))
    ])

    hyperparameters = {
        'mlpregressor__hidden_layer_sizes': [(5,)],
        'mlpregressor__activation': ['logistic', 'relu', 'tanh'],
    }

    # model = GridSearchCV(make_pipeline(StandardScaler(), MLPRegressor(random_state=123)), hyperparameters, cv=10, n_jobs=-1)
    # model = make_pipeline(StandardScaler(), MLPRegressor(hidden_layer_sizes=5, random_state=1, max_iter=15000))
    # model = MLPRegressor(hidden_layer_sizes=3, random_state=1, max_iter=15000)
    # model = GridSearchCV(make_pipeline(StandardScaler(), MLPRegressor(random_state=1)), hyperparameters, cv=10)
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    # single_pred = model.predict(X_test[0].reshape(-1, 1))
    # save_result(single_pred)
    print(pipe.score(X_test, y_test))
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

#
# NOT YET TESTED
#
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
    # main()
    t1 = threading.Thread(predict_neural())
    t2 = threading.Thread(asyncio.run(connect_to_backend()))

    t1.start()
    t2.start()

    t1.join()
    t2.join()