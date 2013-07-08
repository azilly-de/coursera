#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
from tempfile import mkdtemp
import os.path as path

def traceBackItems(weights, costMatrix):
    # trace back selected items
	i = len(costMatrix)-1
	currentWeight =  len(costMatrix[0])-1
	marked = []
	for i in range(i+1):
		marked.append(0)			
	while (i >= 0 and currentWeight >=0):
		if (i==0 and costMatrix[i][currentWeight] >0) or (costMatrix[i][currentWeight] != costMatrix[i-1][currentWeight]):
			marked[i] =1
			currentWeight -= weights[i]
		i = i-1
	return marked

def KnapsackDP(values, weights, capacity):
    # Solve 01 knapsack with Dynamic Programming
    items = len(values)    
    costMatrix = np.zeros((items,capacity+1), dtype=np.int)
    
    for i in range(0, items):
        for j in range(0,capacity+1):
            if (weights[i] > j):
                costMatrix[i][j] = costMatrix[i-1][j]
            else:
                costMatrix[i][j] = max(costMatrix[i-1][j], values[i] +costMatrix[i-1][j-weights[i]])

    value = costMatrix[items-1][capacity]
    taken = traceBackItems(weights, costMatrix)
    optimal = 1
    return (value, taken, optimal)
    
def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    items = len(values)

    ans = KnapsackDP(values, weights, capacity)
    value = ans[0]
    taken = ans[1]
    optimal = 0
    
    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(optimal) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

