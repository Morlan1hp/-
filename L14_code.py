# Licensing Information: You are free to use or extend this file for 
# educational purposes provided that (1) you retain this notice, and 
# (2) you provide clear attribution to the University of Melbourne, 
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020
import time
import random

# Mergesort algorithm
def Merge(B, C, A):
    p = len(B)
    q = len(C)
    i = j = k = 0
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

def test_merge_sort():
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
    Mergesort(array)
    print(array)

# Mode finding algorithm, to find most common element in array
def ModeFinding(A):
    n = len(A)
    Mergesort(A)
    i = 0
    maxfreq = 0
    while i < n:
        runlength = 1
        while i + runlength < n and A[i + runlength] == A[i]:
            runlength = runlength + 1
        if runlength > maxfreq:
            maxfreq = runlength
            mode = A[i]
        i = i + runlength
    return mode

def test_mode_finding():
    a = [42, 78, 13, 13, 57, 42, 57, 78, 13, 98, 42, 33]
    print(ModeFinding(a))

# Algorithms for uniqueness checking, i.e checking if there are duplicate elements in array
def BruteForce(A):
    n = len(A)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                return False
    return True

def Presorting(A):
    n = len(A)
    Mergesort(A)
    for i in range(0, n - 2):
        if A[i] == A[i + 1]:
            return False
    return True

def test_uniqueness_check():
    # Random array of unique integers of length 10000
    a = random.sample(range(1, 100000), 10000)

    start = time.time()
    res_bf = BruteForce(a)
    end = time.time()

    print(f"Brute force: {res_bf}, time: {end-start}")

    start = time.time()
    res_ps = Presorting(a)
    end = time.time()
    
    print(f"Presorting: {res_ps}, time: {end-start}")

if __name__ == "__main__":
    test_merge_sort()
    test_mode_finding()
    test_uniqueness_check()