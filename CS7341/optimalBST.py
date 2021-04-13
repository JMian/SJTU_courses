# A python3 program to find the optimal average cost for a BST
import numpy as np

def optimalBST(p):
    n = len(p)
    C = np.zeros((n, n))
    W = np.zeros((n, n))
    for i in range(n):
        C[i][i] = p[i]
        W[i][i] = p[i]
    # fill in each diagonal
    for d in range(2, n+1):   
        # fill in entries in the diagonal, the cost for different d-elements subtrees
        for i in range(0, n-d+1):  
            # find the optimal cost for the subtree with keys i...j
            j = i + d - 1
            C[i][j] = float("inf")
            W[i][j] = W[i, j-1] + p[j]
            # try each node in i...j to see which acts as the root
            # for this subtree will result in lowest cost
            for r in range(i, j+1):
                c = 0
                if r > i:   # if there is left subtree available
                    c += C[i, r-1]
                if r < j:    # if there is right subtree available
                    c += C[r+1, j]
                if c < C[i][j]:    # if this key acting as root leads to lower cost
                    C[i][j] = c 
            C[i][j] += W[i][j] # add the probability/weight of the whole subtree
    optimalC = C[0][n-1]
    return optimalC

# Driver Code 
if __name__ == '__main__':
    p = [0.2, 0.3, 0.1, 0.4]
    print(optimalBST(p))
    
