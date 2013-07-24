# Please fill out this stencil and submit using the provided submission script.
## Problem 1
def myFilter(L, num):
    return [x for x in L if x % num != 0]


## Problem 2
def myLists(L): pass


## Problem 3
def myFunctionComposition(f, g): pass
#     {f[k]:v for (k,v) in g.items()}


## Problem 4
# Please only enter your numerical solution.
complex_addition_a = 5 + 3j 
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j


## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    sum = 0
    for i in L:
        sum += i
    return sum
    

## Problem 7
def myProduct(L):
    prod = 1
    for i in L:
        prod *= i
    return prod
    

## Problem 8
def myMin(L):
    min = L[0]
    for i in L:
        if(i < min):
            min = i
    return min
    

## Problem 9
def myConcat(L):
    return "".join(L)


## Problem 10
def myUnion(L):
    union = set()
    for i in L:
        union |= i
    return union
