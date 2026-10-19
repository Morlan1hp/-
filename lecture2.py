# %% [markdown]
# # Code for Animation

# %%
# Licensing Information: You are free to use or extend this file for
# educational purposes provided that (1) you retain this notice, and
# (2) you provide clear attribution to the University of Melbourne,
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# August 2021, derived from material created in January 2020 for
# the same subject


# %% [markdown]
# # Iterative Processing: Array

# %%
# We wrote this version in the live lecture. Below is a version that matches the one from the slides.

A = [3,7,4,2,8]   # len(A) = 5
#    0 1 2 3 4

def find1(A,x):
    # A is an array
    # j indexes A
    for j in range(0,len(A)):
        
        if A[j] == x:
            return j
    return -1

find1(A,2)


# %%
# The find function finds the value in the Array and returns corresponding index,
# returns -1 if not found
def find(A,x,n):
    # A is an array
    j = 0 # j indexes A
    while j < n:
        
        if A[j] == x:
            return j
        j = (j + 1)
    return -1

A = [6,9,2,3,7,5,8]
x = 7 # value to find
n = 7 # size of Array
find(A,x,n)

# %% [markdown]
# # Iterative Processing: List

# %%
class node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return "<a node whose val is %s>" % str(self.val)

# The find function finds the value in the LinkedList and returns corresponding pointer,
# returns None if not found
def find(head, value):
    # head is a linked list
    # p points into head
    p = head
    
    while p != None:
        if p.val == value:
            return p
        p = p.next
        
    return None

# Creation of Linked list
firstnode = node(2)
secondnode = node(3)
thirdnode = node(5)
forthnode = node(7)
firstnode.next = secondnode
secondnode.next = thirdnode
thirdnode.next = forthnode

a = find(firstnode,5)



# %% [markdown]
# # Recursive Processing: Array

# %%
# The find function finds the value in the Array and returns corresponding index,
# returns -1 if not found
def find(A,x,lo,hi):
    # A is an array
    # lo indexes A
    # hi indexes A
    
    if lo > hi:
        return -1
    elif A[lo] == x:
        return lo
    else:
        return find(A,x,lo+1,hi)

A = [6,9,2,3,7,5,8]
x = 7# value to find
n = 7 # size of Array

find(A,x,0,n-1)


# %% [markdown]
# # Recursive Processing: List

# %%
# The find function finds the value in the LinkedList and returns corresponding pointer,
# returns None if not found
def find(p,value):
    # p is a linked list
    
    if p == None:
        return p
    elif p.val == value:
        return p
    else:
        return find(p.next,value)

# Creation of the LinkedList
firstnode = node(2)
secondnode = node(3)
thirdnode = node(5)
forthnode = node(7)
firstnode.next = secondnode
secondnode.next = thirdnode
thirdnode.next = forthnode

a = find(firstnode,5)


# %% [markdown]
# # Stack Implementation: Array

# %%
# Push function adds the value 'x' at the top 't' of the Stack 'A' and returns the updated top 't'
def push(A,t,x):
    # A is an array
    # t indexes A
    A[t] = x
    t += 1
    
    return t

A = [6,9,2,3,7,-1,-1,-1] # Represents the stack
top = 5 # Represents the top of the stack

top = push(A,top,5) # Adding 5 at the top of stack
top = push(A,top,12) # Adding 12 at the top of stack

# %% [markdown]
# # Stack Implementation: Linked List

# %%
# Push function adds the value 'x' at the top 'st' of the Stack and returns the updated top 'st'
def push(st,x):
    # st is a linked list
    # elt is a linked list of single node
    elt = node(x)
    
    elt.next = st
    st = elt
    elt = None
    
    return st

# Creation of LinkedList, the LinkedList represents the stack,
# firstnode is the start 'st' or head of the linkedlist that works as the top of the stack
firstnode = node(2)
secondnode = node(3)
thirdnode = node(5)
forthnode = node(7)
firstnode.next = secondnode
secondnode.next = thirdnode
thirdnode.next = forthnode


firstnode = push(firstnode,5) # Adding 5 at the top of stack
firstnode = push(firstnode,9) # Adding 9 at the top of stack


