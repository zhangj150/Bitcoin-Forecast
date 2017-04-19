import pandas
import matplotlib.pyplot as plt
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error


dataset = pandas.read_json('../data/etherprices.json', convert_dates=['date']) #extract only date and price columns (1 and 7)
dataset['date'] = pandas.to_datetime(dataset['date'], unit='s')
dataset.set_index(['date'], inplace=True)
dataset = dataset['weightedAverage'].replace(to_replace=0, method='ffill') #replace zeroes (missing fields) with previous non zero value

print(dataset.head())

X = dataset.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = []
#$newTest = []
print("got to for loop")
k = 10 #forecast the next k time steps
for i in range(0, len(test)-k+1, 1):
    if (i%k == 0):
        model = ARIMA(history, order=(3,1,0))
        model_fit = model.fit(disp=0)
        output,stderr,conf = model_fit.forecast(steps=k)
        
        for f in range(k):
            predictions.append(output[f])
            history.append(test[i+f])
            print('predicted=%f, expected=%f' % (output[f], test[i+f]))
print (len(test), len(predictions))
error = mean_squared_error(test[0:len(predictions)], predictions)
print("MSE: " + str(error))

plt.plot(test)
plt.plot(predictions, color='orange')
plt.title("Ether Prices (blue) vs Predicted (orange)")
plt.ylabel("Ether Value in USD")
plt.xlabel("Time")
plt.show()