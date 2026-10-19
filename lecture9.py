# %%
# Licensing Information: You are free to use or extend this file for
# educational purposes provided that (1) you retain this notice, and
# (2) you provide clear attribution to the University of Melbourne,
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# August 2021, derived from material created in January 2020 for
# the same subject

# An annoying Colab issue:
# matplotlib 3.2 seems to be the default, so we tell it to install
# a newer version. This will cause an error when you first run it,
# telling you that you need to restart the runtime. After seeing
# that error choose Runtime -> Restart runtime from the menu above.
# Then execute this part again and things should work OK.

# %% [markdown]
# # Insertion Sort

# %%
def InsertionSort(A):
    # A is an array
    
    for i in range(1, len(A)): # i indexes A
        
        v = A[i]
        j = i - 1 # j indexes A
        while j >= 0 and v < A[j]:
            
            A[j + 1] = A[j]
            j = j - 1
        
        A[j + 1] = v
        




A = [3, 1, 4, 5, 9, 2, 6, 8, 7, 0]
InsertionSort(A)


# %% [markdown]
# # Shellsort
# Using Knuth's gap sequence: 1, 4, 13, 40, 121, ... See Knuth (1997), "Shell's method". The Art of Computer Programming. Volume 3: Sorting and Searching (2nd ed.).

# %%
import math

# the initial gap for an array of length n should not be larger than ceil(n/3)
# each time through the loop we at least multiple g by 3
# the loop will certainly terminate when g = n
# hence it will run for O(log3(n)) iterations
def GetInitialGap(n):
    g = 4
    prev = 1
    while g <= math.ceil(n/3.0):
        prev = g
        g = (g * 3) + 1
    return prev

def ShellSort(A): # A is an array
    g = GetInitialGap(len(A))
    while g >= 1:
        # sort with gap g
        b = 0
        
        while b < g:
            i = b + g
            
            while i < len(A): # i indexes A
                
                v = A[i]
                j = i - g;
                
                while j >= b and v < A[j]: # j indexes A
                    
                    A[j + g] = A[j]
                    j = j - g
                
                A[j + g] = v
                i = i + g
            
            b = b + 1
        
        # previous gap in the sequence [1,4,13,40,121,...]
        g = int((g - 1) / 3)  # ensure the result is an integer, not a float

A = [11,10,9,8,7,6,5,4,3,2,1]

ShellSort(A)


