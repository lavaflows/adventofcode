#! /bin/env/python
import pdb
import csv
import sys
from collections import defaultdict
from collections import Counter

def read_file(filename:str,offset=1)-> dict:
    'Read elf data, return elf dictionary of ints'

    with open(filename,'rt') as file:
        
        line = csv.reader(file)
        elf = defaultdict(list)
        elf_count = 0

        for row in line:
            if row:
                elf[elf_count+offset].append(int(row[0]))
            else:
                elf_count+=1        
        return elf


def elf_sorter(data:dict)->list:
    '''Takes elf dictionary of calories caried by elf.
    Creates a tuple of the items() of the dictionary
    with values as the first item of and index (the elf)
    as the second item.

    You can then perform max(), min(), sort() operations on it
    to determine elf carrying most calories. 
    Hint: it's the paranoid elf
    '''
    return [(sum(value),index) for index,value in data.items()]

def data_counter(data:dict,offset=1):
    elf_counter = Counter()
    for elf_no,value in data.items():
        elf_counter[elf_no+offset] += sum(value)
    return elf_counter

def make_report(filename:str,operation)->tuple:
    elf_data = read_file(filename)
    elf_info = elf_sorter(elf_data)
    
    if isinstance(operation,str):
        if operation == 'max':
            data_func = max
        elif operation == 'min':
            data_func = min
    else:
        data_func = operation

    data = data_func(elf_info)

    print(f"Elf {data[1]} has the '{operation}' number of calories: {data[0]}")    

def get_counter(filename:str):
    elf_data = read_file(filename)
    return data_counter(elf_data)

def make_counter_report(filename:str, rank = 3):
    'Get top three Elves carrying most calories.'
    counter = get_counter(filename)
    

    elves = [elf for elf,calories in counter.most_common(rank)]
    calories = sum([calories for elf,calories in counter.most_common(rank)])

    print(f'The top three elves are {elves} with a total of {calories} calories!')




def main(argv):
    if argv[1] == '1':
        # Part 1 of Day 1
        if len(argv) == 4:
            filename = argv[2]
            operation = argv[3]
        else:
            filename = 'data/d1.txt'
            operation = max

        make_report(filename=filename,operation=operation)
    elif argv[1] == '2':
        # Part 2 of Day 1.
        if len(argv) == 4:
            filename = argv[2]
        else:
            filename = 'data/d1.txt'
        
        make_counter_report(filename)

if __name__=='__main__':
    main(sys.argv)