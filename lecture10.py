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
# # Binary Search

# %%
def BinSearch(A, k):
    # A is an array
    lo = 0
    hi = len(A) - 1
    # lo indexes A, hi indexes A
    
    while lo <= hi:
        # m indexes A
        m = lo + (hi - lo) // 2
        
        if A[m] == k:
            
            return m
        if A[m] > k:
            hi = m - 1
            
        else:
            lo = m + 1
            
    return -1


BinSearch([1, 2, 3, 5, 8, 13], 8)

# %% [markdown]
# # Lomuto Partition

# %%
def LomutoPartition(A, lo, hi):
    # A is an array, lo indexes A, hi indexes A
    p = A[lo]
    s = lo # s indexes A
    
    # i indexes A
    for i in range(lo + 1, hi + 1):
        
        if A[i] < p:
            s = s + 1
            
            A[s], A[i] = A[i], A[s]
            
    A[s], A[lo] = A[lo], A[s]
    
    return s



array = [3, 1, 4, 5, 9, 2, 6, 8]
lo = 0
hi = len(array) - 1

LomutoPartition(array, lo, hi)


# %% [markdown]
# # Quick Select

# %%
def QuickSelect(A, lo, hi, k):
    # A is an array, lo indexes A, hi indexes A
    
    # s indexes A
    s = LomutoPartition(A, lo, hi)
    if s - lo == k - 1:
        
        return A[s]
    else:
        if s - lo > k - 1:
            
            return QuickSelect(A, lo, s - 1, k)
        else:
            
            return QuickSelect(A, s + 1, hi, (k - 1) - (s - lo))


array = [3, 1, 4, 5, 9, 2, 6, 8]
QuickSelect(array, 0, len(array) - 1, 7)

# %% [markdown]
# # Interpolation Search

# %%
def InterpolationSearch(A, k):
    # A is an array
    # lo indexes A
    # hi indexes A
    lo = 0
    hi = len(A) - 1
    while lo < hi:
        
        if A[lo] > k or A[hi] < k:
            break
        if lo == hi:
            if A[lo] == k:
                
                return lo
            else:
                break
        m = lo + (k - A[lo]) * (hi - lo) // (A[hi] - A[lo]) # m indexes A
        
        if A[m] == k:
            
            return m
        if A[m] > k:
            hi = m - 1
            
        else:
            lo = m + 1
            
    return -1


for i in range(15):
    InterpolationSearch([1, 2, 3, 5, 8, 13], i)

# %%



