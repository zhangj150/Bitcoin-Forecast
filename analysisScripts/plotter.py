import pandas
import matplotlib.pyplot as plt


def visualize(filename):
    #get sentiment data vs time
    parser = lambda date: pandas.datetime.strptime(date, '%m/%d/%Y')
    dataset = pandas.read_csv(filename, parse_dates=[0], usecols=[0,4] , date_parser=parser, engine='python')
    #print (dataset.head(10))
    dataset.set_index(['EventTimeDate'], inplace=True) #tell pandas which column is the actual dates
    dataset=dataset.groupby(dataset.index).mean() #combine duplicate dates by mean of sentiments
    #print (dataset.head(10))

    return dataset


def visualizeBitcoinPrices(filename):
    parser = lambda date: pandas.datetime.strptime(date, '%m/%d/%Y') #tell it how to parse the date in files
    dataset = pandas.read_csv(filename, parse_dates=['Date'], usecols=[0,7], engine='python') #extract only date and price columns (1 and 7)
    dataset.set_index(['Date'], inplace=True)
    dataset = dataset['Weighted Price'].replace(to_replace=0, method='ffill') #replace zeroes (missing fields) with previous non zero value
    print (dataset.head(10))

    return dataset

def main():
    sentiments = visualize("data/BITCOIN_82453_GD2.0_CLEAN(2).csv")
    bitcoinPrices = visualizeBitcoinPrices('data/bitcoinprices.csv')

    fig = plt.figure()

    plot1 = fig.add_subplot(311)
    plot1.set_title("sentiments over time")
    plot1.plot(sentiments)
    plot1.plot(pandas.rolling_mean(sentiments, window=10, min_periods=3)) #rolling mean for sentiments data
    

    plot2 = fig.add_subplot(313)
    plot2.set_title("bitcoin prices over time")
    plot2.plot(bitcoinPrices)

    plt.show()

if __name__ == "__main__": main()