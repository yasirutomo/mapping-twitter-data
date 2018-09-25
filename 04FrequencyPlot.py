'''
    Muhammad Nur Yasir Utomo (yasirutomo@gmail.com)
'''

import json
from matplotlib import pyplot as plt
import numpy as np


def main():
    file_concern = "geotagged/stream_sampleoutputstream.json"

    with open(file_concern, 'r') as f:
        # count occurrence
        d = {}
        for line in f:
            tweet = json.loads(line)
            location = tweet['location']

            location = int(location) if location.isdigit() else location
            if location in d:
                d[location] += 1
            else:
                d[location] = 1
        print("")
        print(d)

        # separate key and value
        country = []
        freq = []
        for i in d:
            country.append(i)
            freq.append(d[i])
        print("")
        print(country)
        print(freq)

        # prepare plot common bar chart
        plt.bar(country, freq, label="Number of Tweet", color="b")
        plt.xlabel('Country')
        plt.ylabel('Frequency')
        plt.title('Interesting Graph')
        plt.legend()
        label = freq
        for i in range(len(freq)):
            plt.text(x=country[i], y=freq[i], s=label[i], size=10)
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    main()