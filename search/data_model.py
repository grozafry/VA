import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def get_regression_val(modeling_data: list, input_mileage: float):
    
    mileage, price = np.array(modeling_data).T
    """
    price is dependent variable, mileage is independent variable
    """

    M = np.array(mileage).reshape(-1, 1)
    P = np.array(price)  
    I = np.array([input_mileage]).reshape(-1, 1)

    M_train, M_test, P_train, P_test = train_test_split(M, P, test_size=None, random_state=42)

    model = LinearRegression()
    model.fit(M_train, P_train)

    plt.scatter(M, P, color='blue', label='Data Points')
    plt.plot(M, model.predict(M), color='red', label='Regression Curve')

    suraj_input = I
    plt.scatter(suraj_input, model.predict(suraj_input), color='green', label='Suraj Data Prediction')

    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.legend()
    # plt.savefig('my_chart.png')
    plt.show()

    return round(model.predict(suraj_input)[0], -2)
