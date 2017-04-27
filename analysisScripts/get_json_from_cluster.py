"""
get_json_from_cluster
Cluster file is .csv, looks like:

month,day,year,site,occurrences,url
1,6,2015,coindesk.com,84,http://www.coindesk.com/accenture-blockchain-major-technology-insurers/
1,15,2015,fusion.net,1,http://fusion.net/story/255949/bitcoin-failed-says-mike-hearn/
2,18,2015,newsdaily.com,4,http://newsdaily.com/2015/02/u-s-marshals-to-auction-50000-bitcoins-from-silk-road/
2,18,2015,lycos.com,5,http://news.lycos.com/technology/us-marshals-to-auction-50000-bitcoins-from-silk-road-fc370165fee64baa069255fe5973b9eb/
2,18,2015,techspot.com,2,http://www.techspot.com/news/59791-us-marshals-auction-50000-additional-bitcoins-seized-silk.html
2,18,2015,abril.com.br,4,http://exame.abril.com.br/tecnologia/noticias/

Need to convert to JSON format

"""

import csv

parents = []
dictionary = {}
growing_urls = ""

cluster_num = 27

with open("cluster_%s.csv" % cluster_num, "r") as data_file:
    reader = csv.reader(data_file)
    for line in reader:
        if line[3] not in parents:  # new term to enter into dictionary
            parents.append(line[3])
            dictionary[line[3]] = line[4]
        else:
            growing_urls = dictionary[line[3]] + "," + line[4]
            dictionary[line[3]] = growing_urls

all_stuff = ""

for key in dictionary:
    innermost = ""  # innermost child of json
    # split up dictionary key by comma
    all_urls = dictionary[key].split(",")  # returns a list of each url

    if len(all_urls) == 1:  # there is only 1 article url
        innermost = '{"parent": "%s", "name": "%s"}' % (key, dictionary[key])
    else:  # there are multiple article urls
        index = 0
        for url in all_urls:
            if index == len(all_urls) -1:  # is the last url
                innermost += '{"parent": "%s", "name": "%s"}' % (key, url)  # last url
            else:
                innermost += '{"parent": "%s", "name": "%s"},' % (key, url)  # not last, need comma
            index += 1

    second = '{"parent": "Cluster %s", "name": "%s", "_children": \n\t\t[%s]},\n\t\t' % (cluster_num, key, innermost)
    all_stuff += second

json_txt = '[{"parent": null, "name": "Cluster %s", "children": \n\t[%s' % (cluster_num, all_stuff)
json_txt = json_txt[:-4] + "\n]}]"

with open("cluster%s.json" % cluster_num, "w") \
        as out_file:
    out_file.write(json_txt)
