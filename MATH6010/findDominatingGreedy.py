# python3 程序，使用贪心算法构造无向图的支配集
import numpy as np 
import random
import math

# E = 邻接矩阵, n = 节点的数量, delta = 每个顶点的最小邻居数目
def findDominatingGreedy(E, n, delta):

    U = []    # 用来存储已被选择进支配集的顶点，新的顶点加在尾部
    
    # 继续选择顶点进支配集直到所有顶点都已被支配
    while np.sum(E) != 0:
        uncovNB = np.sum(E, axis=1)   # 计算每个顶点还有多少邻居未被支配
        maxV = np.argmax(uncovNB)  # 查找拥有最多还未被支配邻居的顶点
        U.append(maxV)          # 把被选中的顶点加入支配集
        # 迭代找出被选中顶点所有尚未被支配的邻居
        for i in range(0, n, 1):
            if  E[maxV][i] == 1: 
                E[:,i] = 0      # 对该邻居的所有邻居单向删边
        E[maxV,:] = 0        # 把被选中顶点的所有边从图里移除
        E[:,maxV] = 0


    # 计算支配集中顶点数目的上界
    upperbound = n * (1 + math.log(delta + 1)) / (delta + 1)
    print("支配集顶点数目上界: ", upperbound)
    print("支配集中顶点数目: ", len(U))
    print("支配集: ", U)

# Driver Code 
if __name__ == '__main__':

    ###################### SAMPLE 1 #######################
    n = 100    # 顶点数目
    delta = 3    # 每个顶点的最小邻居数目
    E = np.zeros((n,n))  # 构造一个全0矩阵
    NB = np.zeros(n)   # 用以记录每个顶点目前有多少邻居
    # 为每一个顶点随机选择3个邻居，并且确保在邻接矩阵中自己为1
    for i in range(0, n, 1):
        while NB[i] < delta:
            r = random.randint(0, n-1)
            if r != i and E[i][r] != 1:
                E[i][r] = 1
                E[r][i] = 1
                NB[i] += 1
                NB[r] += 1
        E[i][i] = 1
    print("平均邻居数: ", np.average(NB))
    print("平均邻居数标准差: ", np.std(NB))
    findDominatingGreedy(E, n, delta)

    # ###################### SAMPLE 2 #######################
    # n = 200  
    # delta = 3  
    # E = np.random.randint(0, 2, size=(n,n))  # 随机构造一个0-1矩阵
    # E = (E + E.transpose())/2   # 因为是无向图，令该矩阵对称
    # E = np.around(E)    # 近似矩阵中的数目，因为前一步骤可能令某些数目变0.5
    # # 检查每个顶点是否有至少delta位邻居，如果没有，随机加邻居
    # # 并且确保在邻接矩阵中自己为1
    # for i in range(0, n, 1):
    #     E[i][i] = 1
    #     neighbor = np.sum(E, axis=1)[i]
    #     while neighbor < delta + 1:
    #         r = random.randint(0, n-1)
    #         if r != i and E[i][r] != 1:
    #             E[i][r] = 1
    #             E[r][i] = 1
    #             neighbor = neighbor + 1  
    # NB = np.sum(E,axis=1)-1
    # print("平均邻居数: ", np.average(NB))
    # print("平均邻居数标准差: ", np.std(NB))
    # findDominatingGreedy(E, n, delta)

    # ##################### SAMPLE 3 #######################
    # n = 6
    # delta = 1
    # E = np.array([[1,1,0,0,1,0], [1,1,1,0,1,0],[0,1,1,1,0,1],\
    #       [0,0,1,1,0,0],[1,1,0,0,1,1],[0,0,1,0,1,1]])
    # findDominatingGreedy(E, n, delta)

    # ##################### SAMPLE 4 #######################
    # n = 10
    # delta = 3
    # E = np.array([[1,0,1,1,0,1,0,0,0,0,],[0,1,0,1,1,0,1,0,0,0],\
    #               [1,0,1,0,1,0,0,1,0,0],[1,1,0,1,0,0,0,0,1,0],\
    #               [0,1,1,0,1,0,0,0,0,1],[1,0,0,0,0,1,1,0,0,1],\
    #               [0,1,0,0,0,1,1,1,0,0],[0,0,1,0,0,0,1,1,1,0,],\
    #               [0,0,0,1,0,0,0,1,1,1],[0,0,0,0,1,1,0,0,1,1]])
    # findDominatingGreedy(E, n, delta)
