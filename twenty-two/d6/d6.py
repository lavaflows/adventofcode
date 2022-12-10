import pdb
from collections import deque

def read_file(filename:str)->list:
    '''
    Read elf file with message. Return list.
    '''
    data = []
    with open(filename,'rt') as file:
        for line in file:
            data.append(line)
    return data

def find_marker(data:list, maxlen=4)->tuple:
    '''
    Using deque from collections, append each character with a max of 'maxlen'
    Compare the length of unique count of items (set) if its equal to 'maxlen'
    Then you've found the start marker.
    Returns tuple with marker and the message marker.
    '''
    deque_marker = deque(maxlen=maxlen)
    for char_mark,char in enumerate(data,start=1):
        deque_marker.append(char)
        if len(set(deque_marker)) == maxlen:
            return (char_mark,deque_marker)
    return None


if __name__ =='__main__':
    filename = 'data/d6.txt'
    data = read_file(filename)
    
    four_data = [find_marker(row) for row in data]
    print(f'Part 1: Marker found at {four_data[0]}')
    
    fourteen_data =  [find_marker(row,maxlen=14) for row in data]
    print(f'Part 1: Marker found at {fourteen_data[0]}')
