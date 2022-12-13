'''
Strategy:
Use a generator (using yield) to return rows of the file so that we can iterate through it line by line
and process/add relevant data to a data structure based on its value.

example: If $ is detected then its a command
        parse_command(text after $)
            if $cd, update current directory
            listen for next command (ls), associate all results from ls forward to
            that current directory.
        
        Create a hiearchy (list? linked list?) showing directories and files.
        Store metrics for each in a tuple (file|dir and size = 0 if dir, X if file where x is a positive integer.)

        data = {'/': 
                {'dir' : [('gnpd', 0), ('jsv', 0)],
                 'file': [('a.txt', 1234), ('b.txt', 4321)]
                }
            }
            tuple = (name, type, size)
            tuple = {'}

            Use a simple dictionary to tell you where
            {'/': {'file': [('a',1), ('b',2), ('c',3)], 'dir': [('d',0), ('e',1), ('f',2)]}}
            Use a list (pop) to track which directory you're in. Append for cd, pop ..
'''

import pdb
from collections import defaultdict
from pprint import pprint

def read_file(filename):
    with open(filename, 'rt') as file:
        for line in file:
            yield line.splitlines()

def parse_command(command):
    if command.startswith('$') and 'cd' == command.split(' ')[1]:
        identifier, value1, value2 = command.split(' ')
        return ('cmd',value1,value2)
    elif command.startswith('$') and command.endswith('ls'):
        
        identifier, value1 = command.split(' ')
        return ('cmd',value1,None)
    else:
        value1,value2 = command.split(' ')
        if value1.isdigit():
            return ('data',int(value1),value2)
        else:
            return ('data', value1, value2)
def is_dir(value):
    return (value == 'dir') or (value == '/')

def process_commands(commands):
    filesystem = defaultdict(list)
    current_dir = []
    for cmd in commands:
        cmd,v1,v2 = parse_command(cmd[0])    
        if cmd == 'cmd':
            if v1 == 'cd':
                filesystem[v2] = []
                if v2 == '..':
                    current_dir.pop()
                else:
                    current_dir.append(v2)
        elif cmd == 'data':
            if isinstance(v1,int):             
                filesystem[current_dir[-1]].append({'file':(v1,v2)})
            elif is_dir(v1):
                filesystem[v2] = []
                filesystem[current_dir[-1]].append({'dir':(0,v2)})

    return filesystem

def total_size(directory, filesystem):
    start = filesystem[directory]
    count = 0
    
    for data in start:
        #print(data)
        if 'dir' in data:  
            count += total_size(data['dir'][1],filesystem)
        elif 'file' in data:
            count += data['file'][0]    
    return count

def sum_all_dirs(filesystem, threshold=100000):
    keys = filesystem.keys()
    
    totals = [total_size(dir,filesystem) for dir in keys if total_size(dir,filesystem) <= threshold]
    return sum(totals)

def main():
    gen = read_file(filename)
    fs = process_commands(gen)
    #directory = input('Enter directory:')
    #print(f'The total size of directory: {directory} is {total_size(directory,fs)}')
    print(f'The total size of with at most 100000 is: {sum_all_dirs(fs)}')
    return fs
    


if __name__ == '__main__':
    filename = 'data/d7.txt'
    fs = main()
    
    