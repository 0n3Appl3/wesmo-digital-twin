#import tensorflow as tf
#import numpy as np
#from sklearn.datasets import load_diabetes
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error, r2_score
#import matplotlib.pyplot as plt
# import pandas as pd

def main():
    # SOURCE: OFFICIAL SCIKIT LEARN WEBSITE
    # X = X[:, np.newaxis, 2]

    # X_train = X[:-20]
    # X_test = X[-20:]

    # y_train = y[:-20]
    # y_test = y[-20:]

    # regr = LinearRegression()
    # regr.fit(X_train, y_train)

    # y_pred = regr.predict(X_test)

    # print("Coefficients: \n", regr.coef_)
    # print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

    # plt.scatter(X_test, y_test, color="black")
    # plt.plot(X_test, y_pred, color="blue", linewidth=3)
    # plt.xticks(())
    # plt.yticks(())
    # plt.show()

    # SOURCE: YOUTUBE FREECODECAMP
    pipe = Pipeline([
        ("scale", StandardScaler()),
        ("model", KNeighborsRegressor(n_neighbors=1))
    ])

    mod = GridSearchCV(estimator=pipe,
                 param_grid={'model__n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]},
                 cv=3)
    mod.fit(X, y)
    print(mod.cv_results_)

if __name__ == "__main__":
    main()