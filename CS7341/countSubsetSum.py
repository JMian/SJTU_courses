# A python3 program to count within an array the number of subsets whose elements 
# sum to a given value k
import numpy as np

def countSubsetSum(A, k):
    n = len(A)
    S = np.zeros((n+1, k+1))
    for i in range(0, n+1):
        S[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            S[i][j] = S[i-1][j]
            if j >= A[i-1]:
                S[i][j] += S[i-1][j-A[i-1]]
    return S

# Driver Code 
if __name__ == '__main__':
    A = [3,5,1,8,4,2]
    k = 5
    print(countSubsetSum(A,k))
