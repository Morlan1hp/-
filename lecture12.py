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
# # TreeNode

# %%
from queue import Queue

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Height(T):
    if T is None:
        return -1
    else:
        return max(Height(T.left), Height(T.right)) + 1


T = Node(17)
T.left = Node(33)
T.left.left = Node(19)
T.left.right = Node(16)
T.left.right.left = Node(38)
T.left.right.right = Node(31)
T.right = Node(48)
T.right.left = Node(11)
T.right.right = Node(14)

# %% [markdown]
# ## Preorder Traverse

# %%
def PreorderTraverse(T):
    # T is a tree
    if T is not None:
        # node is currently being traversed
        node = T.val
        
        PreorderTraverse(T.left)
        
        PreorderTraverse(T.right)
        


PreorderTraverse(T)

# %% [markdown]
# ## Inorder Traverse

# %%
def InorderTraverse(T):
    if T is not None:
        InorderTraverse(T.left)
        node = T.val
        
        InorderTraverse(T.right)


PreorderTraverse(T)

# %% [markdown]
# ## Postorder Traverse

# %%
def PostorderTraverse(T):
    if T is not None:
        PostorderTraverse(T.left)
        PostorderTraverse(T.right)
        node = T.val
        


PreorderTraverse(T)

# %% [markdown]
# ## Levelorder Traverse

# %%
def LevelorderTraverse(T):
    Q = Queue()
    Q.put(T)
    while not Q.empty():
        # X is a tree
        X = Q.get()
        # node is currently being traversed
        node = X.val
        
        if X.left is not None:
            Q.put(X.left)
        if X.right is not None:
            Q.put(X.right)


PreorderTraverse(T)


