# A python3 program to find the path and largest number of coins 
# that can be collected on an N x M board, starting from [0,0] and ending 
# at [N-1,M-1], only 1 step to the right or down is allowed at each move.
import numpy as np

# A is matrix of gold coins;  k is the number of runs
def CoinCollection(A, k):
    N = len(A)
    M = len(A[0])
    # the maximum number of coins accumulated up until F[i][j]
    F = np.zeros((N, M))   
    # a matrix of path taken. If [i][j] is part of the path, 
    # marked as 1; 0 otherwise
    P = np.zeros((N, M))  
    path = []   # a list of path taken, ordered from left to right

    F[0][0] = A[0][0]

    # Find the number maximum number of coins accumulated up until F[i][j]
    for j in range(1, M):
        F[0][j] = F[0][j-1] + A[0][j]
    for i in range(1, N):
        F[i][0] = F[i-1][0] + A[i][0]
        for j in range(1, M):
            F[i][j] = max(F[i-1][j], F[i][j-1]) + A[i][j]
    maxCoin = F[N-1][M-1]  # maximum number of coins collected in this run

    # find the path taken, backtracking from [N-1][M-1]
    P[0][0] = 1
    P[N-1][M-1] = 1
    r = N-1
    c = M-1
    path.insert(0, '[%d,%d]' % (r,c))
    A[r][c] = 0  # 第2小题
    while (r > 0 or c > 0):
        if r > 0 and (c == 0 or F[r-1][c] > F[r][c-1]):
            P[r-1][c] = 1
            r += -1
        else:
            P[r][c-1] = 1
            c += -1
        if F[r][c] < 0:   # 第3小题
            return "error"     # 第3小题
        path.insert(0, '(%d,%d)' % (r,c))
        A[r][c] = 0  # 第2小题

    # 如果运行超过1次
    if k > 1:
        path_k, maxCoin_k = CoinCollection(A, k-1)
        path.append('path for %d time: ' % (k) + str(path_k))
        maxCoin += maxCoin_k

    return path, maxCoin


# Driver Code 
if __name__ == '__main__':
    A = [\
        [2,2,7,2,1,1],\
        [1,3,8,1,5,6],\
        [1,4,3,1,9,1],\
        [3,1,1,1,2,1],\
        [7,2,2,1,1,2]]  # 39coins
    # A2 = [\
    #     [0,0,0,2,1,1],\
    #     [1,3,0,0,0,6],\
    #     [1,4,3,1,0,1],\
    #     [3,1,1,1,0,1],\
    #     [7,2,2,1,0,0]]   #上面的A第二次行走，17coins
    # A3 = [\
    #     [ 2,-3, 0, 1, 0, 0],\
    #     [ 2, 1, 0,-8, 1, 0],\
    #     [ 0, 1, 0,-6, 7, 0],\
    #     [ 0, 3,-10, 1, 3,-2],\
    #     [-1,-2,-7, 0, 1, 0]]  #第3小题，error
    
    print(CoinCollection(A, 2))

  #  print(CoinCollection(B))
        # A = [\
    #     [0,0,0,0,1,0],\
    #     [0,1,0,1,0,0],\
    #     [0,0,0,1,0,1],\
    #     [0,0,1,0,0,1],\
    #     [1,0,0,0,1,0]]
    # F = [
    #     [0 0 0 0 1 1]
    #     [0 1 1 2 2 2]
    #     [0 1 1 3 3 4]
    #     [0 1 2 3 3 5]
    #     [1 1 2 3 4 5]]
    # A = [\  
    #     [0,7,0,0,0,4],\
    #     [0,0,5,3,0,0],\
    #     [0,8,0,0,0,2],\
    #     [4,0,6,0,1,0],\
    #     [9,0,0,5,0,0],\
    #     [0,3,0,0,7,0]] #33
