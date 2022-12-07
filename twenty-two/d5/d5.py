import csv
import pdb

def read_data(filename):

    data = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for line in rows:
            data.append(line)
    return data


if __name__ == '__main__':
    filename = 'data/d5.txt'
    data = read_data(filename=filename)