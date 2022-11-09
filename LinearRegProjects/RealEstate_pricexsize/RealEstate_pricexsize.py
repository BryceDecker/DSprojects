import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

data = pd.read_csv('real_estate_price_size.csv')
print(data.describe())
#median < mean implies some skewdness to data set
y = data['price']
x1 = data['size']

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
print(results.summary())
plt.scatter(x1, y)
yhat = 223.18*x1 + 101900
fig = plt.plot(x1, yhat, lw=4, c='orange', label='regression line')
plt.xlabel('Size (sq. ft.)', fontsize=20)
plt.ylabel('Cost (USD)', fontsize=20)
plt.show()

#r^2 result implies some relationship between the two variables.
