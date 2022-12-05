#day2

import pdb
import csv
from collections import defaultdict


def read_strategy(filename):
    
    data = []
    with open(filename,'rt') as file:
        rows = csv.reader(file,delimiter=' ')
        for line in rows:
            data.append(line)
    return data

def calculate_stat(data):
    p1,p2 = data

    rock = ['A','X']
    paper = ['B','Y']
    scissor = ['C','Z']

    if calculate_hand_score(p1) == calculate_hand_score(p2):
        return (3+calculate_hand_score(p1),3+calculate_hand_score(p2))
    elif p1 in rock and p2 in scissor:
        return (6+calculate_hand_score(p1),calculate_hand_score(p2))
    elif p1 in paper and p2 in rock:
        return (6+calculate_hand_score(p1),calculate_hand_score(p2))
    elif p1 in scissor and p2 in paper:
        return (6+calculate_hand_score(p1),calculate_hand_score(p2))
    else:
        return (calculate_hand_score(p1),6+calculate_hand_score(p2))

def calculate_wld(data):
    #Calculate win lose draw.
    p1,p2 = data

    #Rock, Paper, Scissor loses to 'B' (paper), 'C' (scissor), 'A' (rock).
    # example: Rock loses to Paper (A loses to B)
    loser_condition = ['B','C','A']   
    win_condition = ['C','A','B'] 
    

    if p2 == 'Y': #needs to end in draw
        return (3+calculate_hand_score(p1),3+calculate_hand_score(p1))
    elif p2 == 'X': #lose
        losing_hand = ['A','B','C'][loser_condition.index(p1)]
        return (6+calculate_hand_score(p1),calculate_hand_score(losing_hand))
    elif p2 == 'Z': #win
        winning_hand = ['A','B','C'][win_condition.index(p1)]
        return (calculate_hand_score(p1),6+calculate_hand_score(winning_hand) )



def calculate_hand_score(data,point_offset=1):
    hand = [['A','B','C'],['X','Y','Z']]

    the_hand = []
    if data < 'X':
        the_hand = hand[0]
    elif data >= 'X':
        the_hand = hand[1]
           
    return point_offset+the_hand.index(data)


if __name__ == '__main__':

    from collections import Counter
    filename = 'data/d2.txt'
    data = read_strategy(filename)
    counter_score_p1 = Counter()

    for i in data:
        p1,p2 = calculate_stat(i)
        counter_score_p1['p1'] += p1
        counter_score_p1['p2'] += p2

    counter_score_p2 = Counter()

    for i in data:
        p1,p2 = calculate_wld(i)
        counter_score_p2['p1'] += p1
        counter_score_p2['p2'] += p2

    print(f'Part 1: {counter_score_p1}, where p2 is our hand.')
    print(f'Part 2: {counter_score_p1}, where p2 is our hand.')