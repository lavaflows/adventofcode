# day 3

import csv
import pdb
from collections import Counter
from collections import defaultdict

def read_file(filename:str)->list:
    with open(filename,'rt') as file:
        rows = csv.reader(file)    
        data = []    
        for line in rows:
            data.append(line)             
        return data

def compartments(rucksack):
    mid = len(rucksack) // 2
    c1 = [priority(i) for i in rucksack[:mid]]
    c2 = [priority(i) for i in rucksack[mid:]]
    return (c1,c2)

def priority(char:str):
    encoded = char.encode('utf-8')
    if encoded[0] < b'a'[0]:    # Upper case
        return encoded[0] - b'A'[0] + 27
    else:
        return encoded[0] - b'a'[0] + 1


def read_compartment(rucksack):

    common_item = []
    for sack in rucksack:
        c1,c2 = compartments(sack[0])
        for i in c1:
            if i in c2:
                common_item.append(i)
                break

    return common_item





if __name__ == '__main__':
    filename = 'data/d3.txt'
    d = read_file(filename)
    add = sum(read_compartment(d))
    
   
    sets = [set(r[0]) for r in d]
    
    counter = 0
    group = defaultdict(list)

    for i,v in enumerate(sets,start=1):
        if i % 3 == 0:
            group[counter].append(v)
            counter += 1            
        else:
            group[counter].append(v)

    intersection = []

    for v in group.values():
        intersection.append(v[0].intersection(v[1],v[2]))



    
        