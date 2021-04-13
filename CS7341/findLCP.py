# A python3 program to find the longest common prefix

# A utility function to find the longest common prefix 
# between two strings
def findLCP(str1, str2):
    result = ""
    n1 = len(str1)
    n2 = len(str2)
    i = 0
    j = 0
    while i < n1 and j < n2:
        if str1[i] != str2[j]:
            break
        result = result + str1[i]
        i += 1
        j += 1
    return result

# A function that returns the longest common prefix 
# from a set of strings; -1 if not exists
def LCP(S):
    prefix = S[0]
    n = len(S)
    for i in range(1, n, 1):
        prefix = findLCP(prefix, S[i])
    return prefix

# Driver Code
if __name__ =="__main__":
    S = ["flower", "flow", "flight"]
    print(LCP(S))
