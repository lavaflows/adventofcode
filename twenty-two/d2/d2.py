#day2

import pdb
import csv
from collections import defaultdict


def read_strategy(filename):
    
    player_one = defaultdict(int)
    player_two = defaultdict(int)
    
    with open(filename,'rt') as file:
        rows = csv.reader(file,delimiter=' ')
        for c1,c2 in tuple(rows):
            pdb.set_trace()

if __name__ == '__main__':
    filename = 'data/d2.txt'
    read_strategy(filename)

