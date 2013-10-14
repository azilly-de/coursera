# -*- coding: utf-8 -*-
"""
Naive solution of frequent words problem
@author: azilly-de
October 2013
"""
def frequent_words_naive(text, k):
    lower_bound = 0
    upper_bound = k
    words =set()
    
    for i in range(0,len(text)-1):
        word = text[lower_bound:upper_bound]
        lower_bound += 1
        upper_bound += 1
        if(len(word) == k):
            words.add(word)
    
    
    freq_dict = {}
    for word in words:
        freq_dict[word] = 0
        lower_bound = 0
        upper_bound = k
        
        for i in range(0,len(text)-1):
            test = text[lower_bound:upper_bound]
            if(test == word):
                freq_dict[word] += 1
            lower_bound += 1
            upper_bound += 1
    
    counts_sorted = [ky for ky in sorted(freq_dict.items(), key=lambda x:x[1])]
    return counts_sorted[::-1]

if __name__ == '__main__':
    with open("stepic_dataset.txt", "r") as infile:
        data = infile.readlines()
        text = data[0].rstrip()
        number = int(data[1].rstrip())

    solution = frequent_words_naive(text,number)    
    for i in solution:
        print("{} {}").format(i[0],i[1])

    