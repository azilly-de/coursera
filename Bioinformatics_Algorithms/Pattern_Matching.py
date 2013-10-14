# -*- coding: utf-8 -*-
"""
Pattern Matching Problem: Find all occurrences of a pattern in a string
@author: azilly-de
October 2013
"""
def pattern_matching(pattern, genome):
    matches = []    

    for i in range(0, len(genome)-1):
        word = genome[i:len(pattern)+i]
        if(word == pattern):
            matches.append(str(i))

    return " ".join(matches)

if __name__ == '__main__':
#    with open("stepic_dataset.txt", "r") as infile:
    with open("Vibrio_cholerae.txt", "r") as infile:
        data = infile.readlines()
#        pattern = data[0].rstrip()
        genome = data[0].rstrip() # 1

    #solution = pattern_matching(pattern, genome)    
    solution = pattern_matching("CTTGATCAT", genome)
    print(solution)
