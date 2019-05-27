#!/usr/bin/python2

# Python 2.7.12
import numpy as np
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
	read_y = np.loadtxt('test.txt', delimiter=',', usecols=(1, ))
	read_x = np.loadtxt('test.txt', delimiter=',', usecols=range(1))
	x = np.array(read_x).reshape((-1, 1))
	y = np.array(read_y)
	print(x)
	print(y)
	model = LinearRegression()
	model.fit(x, y)
	model = LinearRegression().fit(x, y)
	r_sq = model.score(x, y)
	print('coefficient of determination:', r_sq)
	print('intercept:', model.intercept_)
	print('slope:', model.coef_)
	new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
	print('intercept:', new_model.intercept_)
	print('slope:', new_model.coef_)
	y_pred = model.predict(x)
	print('predicted response:', y_pred)
	y_pred = model.intercept_ + model.coef_ * x
	print('predicted response:', y_pred)
	x_new = np.arange(5).reshape((-1, 1))
	print(x_new)
	y_new = model.predict(x_new)
	print(y_new)
