import pandas
import matplotlib.pyplot as plt
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

parser = lambda date: pandas.datetime.strptime(date, '%m/%d/%Y') #tell it how to parse the date in files
dataset = pandas.read_csv('../data/bitcoinprices.csv', parse_dates=['Date'], usecols=[0,7], engine='python') #extract only date and price columns (1 and 7)
dataset.set_index(['Date'], inplace=True)
dataset = dataset['Weighted Price'].replace(to_replace=0, method='ffill') #replace zeroes (missing fields) with previous non zero value

# plt.plot(dataset)
# plt.show()

# autocorrelation_plot(dataset) #258 is good starting point for AR model
# plt.show()

X = dataset.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = []
#$newTest = []
print("got to for loop")
k = 5 #forecast the next k time steps
for i in range(0, len(test)-k+1, 1):
    model = ARIMA(history, order=(1,1,0))
    model_fit = model.fit(disp=0)
    output,stderr,conf = model_fit.forecast(steps=k)
    #print(output)
    #predicted1, predicted2 = output[0], output[1]
    #print (predicted1, predicted2)
    if (i%k == 0):
        #print(output)
        
        #print(predicted)
        #predictions.append(predicted1)
        #predictions.append(predicted2)
        for f in range(k):
            predictions.append(output[f])
            # actual1, actual2 = test[i], test[i+1]
            # history.append(actual1)
            # history.append(actual2)
            history.append(test[i+f])
            #newTest.append(test[i])
            #print('predicted=%f, expected=%f' % (predicted1, actual1))
            #print('predicted=%f, expected=%f' % (predicted2, actual2))
            print('predicted=%f, expected=%f' % (output[f], test[i+f]))
print (len(test), len(predictions))
error = mean_squared_error(test[0:len(predictions)], predictions)
print("MSE: " + str(error))

plt.plot(test)
plt.plot(predictions, color='orange')
plt.show()