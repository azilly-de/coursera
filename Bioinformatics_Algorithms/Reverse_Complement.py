# -*- coding: utf-8 -*-
"""
Solve the Reverse Complement Problem
@author: azilly-de
October 2013
"""
def reverse_complement(pattern):
    patterns = {}
    patterns["A"] = "T"
    patterns["G"] = "C"
    patterns["T"] = "A"
    patterns["C"] = "G"

    complement = "".join([patterns[l] for l in pattern])
  
    return complement[::-1]

if __name__ == '__main__':
    with open("stepic_dataset.txt", "r") as infile:
        data = infile.readlines()
        text = data[0].rstrip()

    solution = reverse_complement(text)
    print(solution)
