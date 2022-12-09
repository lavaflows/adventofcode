import csv
import re
import copy
from collections import defaultdict
from pprint import pprint

import pdb


def read_data(filename):

    crates = []
    moves = []

    switch = False
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for line in rows:
            if not line:
                switch = True
                continue
            if not switch:
                crates.append(line[0])
            else:
                moves.append(line[0])
    return (crates,moves)

def get_item_index(data:str)->list:
    #  input: ' 1 2 3 4 5 ', returns index where numbers are located
    items = data.replace(' ','')
    return [data.index(char) for char in items]

def crate_creation(data:list):

    crates = defaultdict(list)
    index_data = data.pop()
    column_index = get_item_index(index_data)    
    res =[[row[index] for index in column_index] for row in data]

    for row in data:
        for crate_num,index in enumerate(column_index,start=1):
            if row[index] != ' ':
                crates[crate_num].insert(0,row[index])
            else:
                continue
    
    return crates

def parse_moves(moves):
    import re
    pattern = re.compile(r'\d+')
    mo,fr,to = pattern.findall(moves)

    return (int(mo),int(fr),int(to))

def move_commands(crate, moves,mover_version=9000, silence=True):
    
    adjusted_crate = copy.deepcopy(crate)
    
    if mover_version == 9000:
        for move_no,move in enumerate(moves,start=1):
            no_items,from_crate,to_crate = parse_moves(move)
            count = 1
            while count <= no_items:          
                if not silence:
                    print(f'Move # {move_no} - On: {count} out of {no_items}: Moving to {adjusted_crate[to_crate]}')
                try:
                    item = adjusted_crate[from_crate].pop()            
                    adjusted_crate[to_crate].append(item)
                except IndexError as err:
                    raise         
                count += 1
    elif mover_version == 9001:
        for move_no,move in enumerate(moves,start=1):
            no_items,from_crate,to_crate = parse_moves(move)
            count = 1
            item = []
            while count <= no_items:
                if not silence:
                    print(f'Move # {move_no} - On: {count} out of {no_items}: Moving to {adjusted_crate[to_crate]}')
                try:
                    item.insert(0,adjusted_crate[from_crate].pop())
                except IndexError as err:
                    raise         
                count += 1
            adjusted_crate[to_crate].extend(item)
    
    return adjusted_crate




if __name__ == '__main__':
    filename = 'data/d5.txt'
    crates, moves = read_data(filename=filename)
    crate_data = crate_creation(crates)
    move_9000 = move_commands(crate_data, moves,mover_version=9000)
    keys = [i for i in move_9000.keys()]
    keys.sort()

    ontop_9000 = ''
    for i in keys:
        ontop_9000+=move_9000[i][len(move_9000[i])-1]

    move_9001 = move_commands(crate_data, moves,mover_version=9001)
    keys = [i for i in move_9001.keys()]
    keys.sort()

    ontop_9001 = ''
    for i in keys:
        ontop_9001+=move_9001[i][len(move_9001[i])-1]

    print(f'Part 1: Crates on top are: {ontop_9000}')
    print(f'Part 2: Crates on top are: {ontop_9001}')