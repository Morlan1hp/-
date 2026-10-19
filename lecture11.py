# %%
# Licensing Information: You are free to use or extend this file for
# educational purposes provided that (1) you retain this notice, and
# (2) you provide clear attribution to the University of Melbourne,
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

# An annoying Colab issue:
# matplotlib 3.2 seems to be the default, so we tell it to install
# a newer version. This will cause an error when you first run it,
# telling you that you need to restart the runtime. After seeing
# that error choose Runtime -> Restart runtime from the menu above.
# Then execute this part again and things should work OK.


# %% [markdown]
# # Merge Sort

# %%
def Merge(B, C, A):
    # A is an array, B is an array, C is an array
    p = len(B)
    q = len(C)
    i = j = k = 0     # k indexes A, i indexes B, j indexes C
    while i < p and j < q:
        
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
        else:
            A[k] = C[j]
            j = j + 1
        k = k + 1
    
    if i == p:
        A[k: p + q] = C[j: q]
        
    else:
        A[k: p + q] = B[i: p]
        


def Mergesort(A):
    if len(A) > 1:
        n = len(A)
        B = A[:n // 2]
        C = A[n // 2:]
        
        Mergesort(B)
        
        Mergesort(C)
        
        Merge(B, C, A)
        



array = [3, 1, 4, 1, 5, 9, 2, 6]
Mergesort(array)


# %% [markdown]
# # Hoare Partition

# %%
def HoarePartition(A, lo, hi):
    # A is an array
    p = A[lo]
    i = lo
    j = hi
    # i indexes A
    # j indexes A
    while i < j:
        
        while i < hi and A[i] <= p:
            i = i + 1
            
        while j >= lo and A[j] > p:
            j = j - 1
            
        A[i], A[j] = A[j], A[i]
        
    A[i], A[j] = A[j], A[i]
    
    A[lo], A[j] = A[j], A[lo]
    
    return j



array = [3, 1, 4, 5, 9, 2, 6, 8]
HoarePartition(array, 0, len(array) - 1)

# %% [markdown]
# # Quick Sort

# %%

# Note we could also use LomutoPartition from lecture 10 but
# using Hoare's partitioning algorithm is more traditional
def Quicksort(A, lo, hi):
    # A is an array
    
    if lo < hi:
        s = HoarePartition(A, lo, hi)
        Quicksort(A, lo, s - 1)
        Quicksort(A, s + 1, hi)




array = [3, 1, 4, 5, 9, 2, 6, 8]
Quicksort(array, 0, len(array) - 1)



