# A python3 program to find a dominating set of an undirected graph using greedy approach
import numpy as np 
import random
import math

# E = the adjacency matrix,   n = number of vertices
# delta = minimum number of neighbors for each vertex
def findDominatingGreedy(E, n, delta):
    # Create a list acting as dominating set storing the picked vertices
    U = []
    # Create an array to tell if the vertex is already covered. 
    # 1: covered, 0 otherwise, should be all 1 when done
    coveredV = np.zeros(n)
    # An array to store the number of uncovered neighbors for each vertex
    # should be all 0 when done
    uncovNB = np.sum(E, axis=1)

    # Keep picking vertex until all vertices are covered
    while sum(coveredV) != n:
        # find the vertex with the largest number of uncovered neighbors
        maxV = np.argmax(uncovNB)
        U.append(maxV)          # add the picked vertex into U
        E[maxV][maxV] = 0        # remove the self-edge for the picked vertex            
        if coveredV[maxV] != 1:    # if the picked vertex has never been covered before
            uncovNB[maxV] += -1    # minus the number of uncovered neighbor for this picked vertex
        # find all the uncovered neighbors for the picked vertex
        for i in range(0, n, 1):
            if  E[maxV][i] == 1:
                E[maxV][i] = 0     # remove the edge                 
                E[i][maxV] = 0     # remove the edge again, because of symmetry     
                if coveredV[maxV] != 1:    # if the picked vertex has never been covered before
                    uncovNB[i] += -1    # minus 1 from the number of uncovered neighbor for this neighbor
                if coveredV[i] != 1:    # if this neighbor has never been covered before
                    uncovNB[maxV] += -1    # minus 1 from the number of uncovered neighbor of the picked vertex
                    # iterate through all its uncovered neighbors 
                    for j in range(0, n, 1):
                        if E[i][j] == 1:
                            uncovNB[j] += -1
                            # if this pair of vertices are now both covered, break the edge between them
                            if coveredV[j] == 1:  
                                E[i][j] = 0                      
                                E[j][i] = 0
                coveredV[i] = 1   # mark this neighbor i as covered
        coveredV[maxV] = 1    # mark the picked vertex as covered

    # Calculate the upperbound for the number of vertices in the dominating set
    upperbound = n * (1 + math.log(delta + 1)) / (delta + 1)
    print("Upperbound: ", upperbound)
    print("Number of vertices in dominating set: ", len(U))
    print("Dominating set: ", U)


# Driver Code 
if __name__ == '__main__':

    ####################### SAMPLE 1 #######################
    n = 100  # number of vertices
    delta = 3  # minimum degree for each vertex
    # create a random nxn 0-1 matrix
    E = np.random.randint(0, 2, size=(n,n))
    # make the matrix symmetric, to represent an undirected graph
    E = (E + E.transpose())/2
    # round the matrix, since some elements may become 0.5 following the previous step
    E = np.around(E)
    # make sure the diagonal consists of all 1's and
    # check if each vertex has at least delta neighbors. If not, add neighbors
    for i in range(0, n, 1):
        E[i][i] = 1
        neighbor = np.sum(E, axis=1)[i]
        while neighbor < delta + 1:
            r = random.randint(0, n-1)
            if r != i and E[i][r] != 1:
                E[i][r] = 1
                E[r][i] = 1
                neighbor = neighbor + 1

    ####################### SAMPLE 2 #######################
    # n = 6
    # delta = 1
    # E = np.array([[1,1,0,0,1,0], [1,1,1,0,1,0],[0,1,1,1,0,1],[0,0,1,1,0,0],\
    #   [1,1,0,0,1,1],[0,0,1,0,1,1]])

    ######################## SAMPLE 3 #######################
    # n = 10
    # delta = 3
    # E = np.array([[1,0,1,1,0,1,0,0,0,0,],[0,1,0,1,1,0,1,0,0,0],[1,0,1,0,1,0,0,1,0,0],\
    #     [1,1,0,1,0,0,0,0,1,0],[0,1,1,0,1,0,0,0,0,1],[1,0,0,0,0,1,1,0,0,1],\
    #     [0,1,0,0,0,1,1,1,0,0],[0,0,1,0,0,0,1,1,1,0,],[0,0,0,1,0,0,0,1,1,1],\
    #     [0,0,0,0,1,1,0,0,1,1]])


    findDominatingGreedy(E, n, delta)

