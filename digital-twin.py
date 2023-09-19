from dotenv.main import load_dotenv
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler, normalize
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import requests
import asyncio
import socketio

# Create a new Async Socket IO server
sio = socketio.AsyncClient()

# Error message prefix
error_prefix = "[ERROR] "

# MLP
grid_search = None
# LSTM
normaliser = None
model = Sequential()

# Model features
voltage = None
current = None
temperature = None

#
# Event fires when 'event' packet is received from the server.
#
@sio.event
async def event(message: str):
    global sio, voltage, current, temperature
    print("Message received: ", message)
    message_array = message.split(" ")

    if (message_array[0] == "6B2"):
        voltage = int(message_array[1] + message_array[2], 16) / 10
        current = int(message_array[3] + message_array[4], 16) / 10
    elif (message_array[0] == "6B3"):
        temperature = int(message_array[8], 16)

    if (voltage != None and current != None and temperature != None):
        print('we have a voltage, current and temperature value. using them to predict soc')
        # predict_soc()
        voltage = None
        current = None
        temperature = None
    # Pretend results are processed for digital twin and send to server and then to all connected web browser clients
    # sio.emit("send-twin-results", random.randrange(1, 100, 2))
    # main()

#
# Connects to the battery dashboard backend server.
#
async def connect_to_backend():
    global sio
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

# def save_result(result):
#     # Example data JSON (not actual one)
#     new_data = {
#         "id": "null",
#         "<column-2>": result,
#     }
#     # Example REST API endpoint (not actual one)
#     url_post = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test-3"
#     headers = {
#         "content-type": "application/json",
#     }
#     # Send POST request.
#     post_response = requests.post(url_post, json=new_data, headers=headers)
#     post_response_json = post_response.json()
#     print(post_response_json)

#
# Trains the LSTM neural network. (NOT YET TESTED)
#
def train_model():
    global normaliser
    # Read JSON data and convert into data frame.
    json = '<insert data>'
    df = pd.DataFrame(json)

    # Specify the target column.
    target_column = ['<insert target column>']

    # Get the input and target values from columns.
    X = df['<insert parameter column>'].values
    y = df[target_column].values.ravel()

    # Normalise the imput data
    normaliser = MinMaxScaler()
    X_normalised = normaliser.fit_transform(X)

    # Split the data into train and test batches.
    X_train, X_test, y_train, y_test = train_test_split(X_normalised, y, test_size=0.2, random_state=1)

    # Make the LSTM neural network
    lstm = LSTM(5, input_shape=(X_train.shape[1], X_train.shape[2]))
    dense = Dense(1)
    model.add(lstm)
    model.add(dense)
    model.compile(loss="mean_squared_error", optimiser="adam")

    # Fit the model.
    model.fit(X_train, y_train, epochs=100, batch_size=50, verbose=1)

    # Evaluate model on test data
    loss, accuracy = model.evaluate(X_test, y_test)
    print("Test Loss: %.2f", loss)
    print("Test Accuracy: %.2f", accuracy)

#
# Trains the MLP Regressor neural network.
#
def train_model_MLP():
    global grid_search
    # Read JSON data and convert into data frame.
    json = '<insert data>'
    df = pd.DataFrame(json)

    # Specify the target column.
    target_column = ['<insert target column>']

    # Get the input and target values from columns.
    X = df['<insert parameter column>'].values
    y = df[target_column].values.ravel()

    # Normalise the input data
    X_normalised = normalize(X, axis=1)

    # Split the data into train and test batches.
    X_train, X_test, y_train, y_test = train_test_split(X_normalised, y, test_size=0.2, random_state=1)

    # Make a pipeline that scales the data and uses the MLP Regressor neural network.
    pipe = make_pipeline(
        StandardScaler(),
        MLPRegressor()
    )
    # Set the paramaters of the MLP Regressor
    parameters = {
        "hidden_layer_sizes": (5, 5),
        "activation": "relu",
        "random_state": 1,
        "max_iter": 15000, 
    }
    # Make a Grid Search
    grid_search = GridSearchCV(pipe, parameters, cv=10)

    # Fit the model.
    grid_search.fit(X_train, y_train)
    y_pred = grid_search.best_estimator_.predict(X_test)

    # Metrics
    print("Mean Squared Error: %.2f" % mean_squared_error(y_test, y_pred))
    print("Mean Absolute Error: %.2f" % mean_absolute_error(y_test, y_pred))
    print("R2 Score: %.2f" % r2_score(y_test, y_pred))

#
# Predict battery state of charge using LSTM and send to dashboard. (NOT YET TESTED)
#
def predict_soc(voltage, current, temperature):
    global normaliser, model, sio
    data = np.array([[voltage, current, temperature]])
    data = normaliser.transform(data)
    prediction = model.predict(data)
    json = {
        "soc": 'test'
    }
    print("Predicted SOC: " + str(json))
    sio.emit("send-twin-results", json)

#
# Predict battery state of charge using MLP Regressor and send to dashboard.
#
def predict_soc_MLP(input):
    global grid_search, sio
    prediction = grid_search.best_estimator_.predict(input)
    json = {
        "soc": prediction
    }
    sio.emit("send-twin-results", json)

#
# Prints a formatted console error.
#
def print_error(message, error):
    global error_prefix
    print("-------\n" +
          error_prefix + message +
          "\n\n" +
          str(error) +
          "\n-------")

#
# Get data from the Postgres database and train mdoel.
#
def main():
    # Get data and convert into JSON.
    url_get = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test"
    get_response = requests.get(url_get)
    get_response_json = get_response.json()
    #train_model(get_response_json)

#
# Load dotenv, train model and listen for new data.
#
if __name__ == "__main__":
    load_dotenv()
    # main()
    asyncio.run(connect_to_backend())