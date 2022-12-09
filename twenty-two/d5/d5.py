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
    move_pattern = re.compile(r'(move \d)')
    from_pattern = re.compile(r'from \d')
    to_pattern = re.compile(r'to \d')

    mo = move_pattern.search(moves).group()
    fr = from_pattern.search(moves).group()
    to = to_pattern.search(moves).group()

    return (int(mo[len(mo)-1]),int(fr[len(fr)-1]),int(to[len(to)-1]))

def move_commands(crate, moves):
    
    adjusted_crate = copy.deepcopy(crate)
    
    for move_no,move in enumerate(moves,start=1):
        no_items,from_crate,to_crate = parse_moves(move)
        count = 1
        while count <= no_items:          
            print(f'Move # {move_no} - On: {count} out of {no_items}: Moving to {adjusted_crate[to_crate]}')
            try:
                item = adjusted_crate[from_crate].pop()            
                adjusted_crate[to_crate].append(item)
            except IndexError as err:
                pdb.set_trace()
                raise         
            count += 1
    
    return adjusted_crate




if __name__ == '__main__':
    filename = 'data/d5.txt'
    crates, moves = read_data(filename=filename)
    crate_data = crate_creation(crates)
    z = move_commands(crate_data, moves)
    keys = [i for i in z.keys()]
    keys.sort()

    ontop = ''
    for i in keys:
        ontop+=z[i][len(z[i])-1]