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


#partial

#model = ARIMA(dataset, order=(258, 1, 0))
#model_fit = model.fit(disp=0)
#print (model_fit.summary())
X = dataset.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
print("got to for loop")
for i in range(len(test)):
    model = ARIMA(history, order=(10,2,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    predicted = output[0]
    predictions.append(predicted)
    actual = test[i]
    history.append(actual)
    print('predicted=%f, expected=%f' % (predicted, actual))
error = mean_squared_error(test, predictions)
print("MSE: " + str(error))

plt.plot(test)
plt.plot(predictions, color='orange')
plt.show()