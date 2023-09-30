import numpy as np

input_vector = np.array([1.72, 1.23])
weights_1 = np.array([1.26, 0])
weights_2 = np.array([2.17, 0.32])
bias = np.array([0.0])


# creating a non - linear function in order to create more variety of predictions.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# prediction function
def predict(input_vector, weights, bias):
    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2


prediction = predict(input_vector, weights_2, bias)

print(f"The prediction result is: {prediction}")

target = 0  # the final value we want to reach.
# error in prediction
error = np.square(prediction - target)  # amplifying the error in order to make the error more proimnent.

# finding the derivative for error. which is the squared value of (prediction - target)
derivative = 2 * (prediction - target)

print(f"1. Prediction : {prediction}   Error: {error}    Derivative : {derivative}")

# adjusting the weights based on derivative
weights_1 -= derivative
weights_2 -= derivative

prediction = predict(input_vector, weights_1, bias)

error = np.square(prediction - target)

derivative = 2 * (prediction - target)

print(f"2. Prediction : {prediction}   Error: {error}    Derivative : {derivative}")


def sigmoid_derivative(x):
    sigmoid(x) * (1 - sigmoid(x))


'''
dot_product_1 = np.dot(input_vector, weights_1)
print(f"Dot Product 1: {dot_product_1}")

dot_product_2 = np.dot(input_vector, weights_2)
print(f"Dot Product 2 : {dot_product_2}")
'''
