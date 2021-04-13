# A python3 program to count the number of inversions/ reverse pairs 
# within a given array

# A function taking input array and returning the number of inversions
def countInversion(A):
    n = len(A)
    B = [None]*n  # auxiliary array
    return mergeSortNCount(A, B, 0, n-1)

# A function to merge sort the given array while counting the inversions
def mergeSortNCount(A, B, low, high):
    inverseCount = 0
    if low < high:
        mid = (low + high) // 2  # floor division
        inverseCount += mergeSortNCount(A, B, low, mid)
        inverseCount += mergeSortNCount(A, B, mid+1, high)
        inverseCount += mergeNCount(A, B, low, mid, high)
    return inverseCount

# A function to sort two subarrays in non-decreasing order while counting
# inversions
def mergeNCount(A, B, low, mid, high):
    i = low   # Pointer in left subarray
    j = mid + 1   # Pointer in right subrray
    k = low   # Pointer for auxiliary array
    inverseCount = 0
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
            inverseCount += mid - i + 1
        k += 1
    while i <= mid:   # Copy the remaining elements 
        B[k] = A[i]
        i += 1
        k += 1
    while j <= high:   # Copy the remaining elements 
        B[k] = A[j]
        j += 1
        k += 1
    # Copy the sorted array into the original array
    for elements in range(low, high+1):
        A[elements] = B[elements]

    return inverseCount


# Driver Code
if __name__ =="__main__":
    A = [2, 3, 8, 6, 1]
    print(countInversion(A))
