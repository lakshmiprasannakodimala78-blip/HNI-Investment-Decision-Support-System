from sklearn.linear_model import LinearRegression
import numpy as np

def revenue_trend_prediction(years, revenue):
    model = LinearRegression()
    X = np.array(years).reshape(-1, 1)
    y = np.array(revenue)
    model.fit(X, y)
    return model.predict(X)
