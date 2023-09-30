import matplotlib.pyplot as plt
import numpy as np
import warnings #to remove the warnings
warnings.filterwarnings('ignore')


#creating dataSet
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
#plotting the graph of given the dataSet


plt.plot(x,y)
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()



#Creating arrays out of the given dataSet
X_Arr = np.array([x]).reshape(-1,1)
Y_Arr = np.array(y)



X_Arr_Test = np.array([np.linspace(0, 2*np.pi, 5000)]).reshape(-1,1)

#training the model

'''
from sklearn import preprocessing
Transforming_Catalyst = preprocessing.LabelEncoder()

#converting Y_Arr from a continuous dataSet to a categorical dataSet to fit the model in a categorical model like Logistic Regression
Y_Arr_Transformed = Transforming_Catalyst.fit_transform(Y_Arr)

model = LinearRegression()
model.fit(X_Arr, Y_Arr)
#y_pred = model.predict(X_Arr)
plt.plot(x,y_pred)
'''


#training the model for prediction
model = np.poly1d(np.polyfit(x, y, 4))

#predictiing y values
y_pred = model(X_Arr_Test)

#plotting the predicted values
plt.plot(X_Arr_Test, y_pred, color = 'blue')
plt.title('Test Values')
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()