import csv
import numpy as np

if __name__ == "__main__":
    reader=csv.reader(open('TEZOS_1_GD2.0_CLEAN.csv', 'r'), delimiter=',')
    writer=csv.writer(open('TEZOS_1_GD2.0_CLEAN(2).csv', 'w'), delimiter=',')
    entries = set()

    for row in reader:
       key = row[2]

       if key not in entries:
          writer.writerow(row)
          entries.add(key)
    reader2=csv.reader(open('TEZOS_1_GD2.0_CLEAN(2).csv', 'r'), delimiter=',')
    data1 = list(reader2)
    row_count = len(data1)
    print(row_count)
    amtMent = np.zeros(row_count)
    print(amtMent)
    #
    # reader=csv.reader(open('FACTOM_181_GD2.0_CLEAN.csv', 'r'), delimiter=',')
    # for row in reader:
    #    key = row[2]
    #
    #    if key not in entries:
    #       writer.writerow(row)
    #       entries.add(key)
    #    else:
    #       reader2=csv.reader(open('FACTOM_181_GD2.0_CLEAN(2).csv', 'r'), delimiter=',')
    #       data = []
    #       for row in reader2:
    #           data.append(row)
    #
    #       for i in range(row_count):
    #
    #           if data[i][2] == key:
    #
    #               amtMent[i] += 1
    #
    # print(amtMent)
    # np.savetxt("factomAmt.csv", amtMent, delimiter=",")
