from dotenv.main import load_dotenv
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import threading
import requests
import asyncio
import socketio

error_prefix = "[ERROR] "
grid_search = None

voltage = None
current = None
temperature = None

# Create a new Async Socket IO server
sio = socketio.AsyncClient()

#
# Event fires when 'event' packet is received from the server.
#
@sio.event
async def event(message: str):
    global sio, voltage, current, temperature, soc
    print("Message received: ", message)
    message_array = message.split(" ")

    if (message_array[0] == "6B2"):
        voltage = int(message_array[1] + message_array[2], 16) / 10
        current = int(message_array[3] + message_array[4], 16) / 10
    elif (message_array[0] == "6B3"):
        temperature = int(message_array[8], 16)

    if (voltage != None and current != None and temperature != None):
        print('test')
        # predict_soc()
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

def print_error(message, error):
    global error_prefix
    print("-------\n" +
          error_prefix + message +
          "\n\n" +
          str(error) +
          "\n-------")

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

def main():
    # Get data
    url_get = os.environ.get('VITE_BACKEND_URL') + "/api/v1/rest-test"
    get_response = requests.get(url_get)
    get_response_json = get_response.json()
    #predict_model(get_response_json)

#
# NOT YET TESTED
#
def predict_neural():
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

    grid_search.fit(X_train, y_train)
    y_pred = grid_search.best_estimator_.predict(X_test)

    # single_pred = model.predict(X_test[0].reshape(-1, 1))
    print("Mean Squared Error: %.2f" % mean_squared_error(y_test, y_pred))
    print("Mean Absolute Error: %.2f" % mean_absolute_error(y_test, y_pred))
    print("R2 Score: %.2f" % r2_score(y_test, y_pred))

def predict_soc(input):
    global grid_search, sio
    prediction = grid_search.best_estimator_.predict(input)
    json = {
        "soc": prediction
    }
    sio.emit("send-twin-results", json)

if __name__ == "__main__":
    load_dotenv()
    # main()
    #t1 = threading.Thread(predict_neural())
    t2 = threading.Thread(asyncio.run(connect_to_backend()))

    #t1.start()
    t2.start()

    #t1.join()
    t2.join()