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

def visualizeNumMentions(filename):
    parser = lambda date: pandas.datetime.strptime(date, '%m/%d/%Y') #tell it how to parse the date in files
    dataset = pandas.read_csv(filename, parse_dates=[0], usecols=[0,1], engine='python')
    dataset.set_index(['Column 1 1'], inplace=True)
    #dataset = dataset[1].replace(to_replace=0, method='ffill')
    return dataset
def main():
    name = 'consensys'
    sentiments = visualize("~/Downloads/" + name + ".csv") #edit here
    bitcoinPrices = visualizeBitcoinPrices('../data/bitcoinprices.csv')
    mentions = visualizeNumMentions("../data/lineGraph/BITCOIN_S_line_graph_dates_mentions.csv")

    #fig = plt.figure()

    #plot1 = fig.add_subplot(311)
    plt.title("Sentiments Over Time")
    plt.plot(sentiments)
    plt.plot(pandas.rolling_mean(sentiments, window=10, min_periods=3)) #rolling mean for sentiments data
    plt.savefig('../images/sentiments/' + name + 'Tone.png', bbox_inches='tight')
    
    # plot2 = fig.add_subplot(312)
    # plot2.set_title("Number of mentions")
    # plot2.plot(mentions)
    # plot2.plot(pandas.rolling_mean(mentions, window=10, min_periods=3))

    # plot3 = fig.add_subplot(313)
    # plot3.set_title("bitcoin prices over time")
    # plot3.plot(bitcoinPrices)

    plt.show()

if __name__ == "__main__": main()