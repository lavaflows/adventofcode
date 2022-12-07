import csv
import pdb

def read_data(filename):

    data = []
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        for line in rows:
            data.append(line)
    
    return data

def overlap(data,overlap_at_all=False):
    containment_pair_count = 0
    track_pairs = []

    for elf1, elf2 in data:
        #Start and end of each elfs range
        s1,e1= elf1.split('-')
        s2,e2 = elf2.split('-')

        elf1_range = [section for section in range(int(s1),int(e1)+1)]
        elf2_range = [section for section in range(int(s2),int(e2)+1)]
        
        if overlap_at_all:
            if len(set(elf1_range).intersection(set(elf2_range))) > 0:           
                containment_pair_count += 1
                # Track pair overlap (can be changed to be each pair in case they ask later.)
                track_pairs.append(set(elf1_range).intersection(set(elf2_range)))
        else:
            if len(elf1_range) == len(set(elf1_range).intersection(set(elf2_range))):
                containment_pair_count += 1
                # Track pair overlap (can be changed to be each pair in case they ask later.)
                track_pairs.append(set(elf1_range).intersection(set(elf2_range)))
            elif len(elf2_range) == len(set(elf2_range).intersection(set(elf1_range))):
                containment_pair_count += 1
                # Track pair overlap (can be changed to be each pair in case they ask later.)
                track_pairs.append(set(elf1_range).intersection(set(elf2_range)))
            

    return containment_pair_count

if __name__ == '__main__':
    filename = 'data/d4.txt'
    data = read_data(filename=filename)

    
    print(f'Overlap count: {overlap(data)}')
    print(f'Overlap at all count: {overlap(data,overlap_at_all=True)}')


