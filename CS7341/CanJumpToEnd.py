# A Python3 program to check if the end of an array is reachable 
# starting from a defined position a

def CanJumpToEnd(nums, a):
    
    # Considering Python indexs from 0 
    n = len(nums) - 1

    # If end of array is within reach from starting position
    if nums[a] >= n - a:
        return True
 
    # To keep track of position
    currentPosition = a
    
    while True:
        # Initiate a new list to store the furthest reachable 
        # position from each current reachable position 
        availablePosition = []

        # Determine if the furthest position within reach from  
        # current position is determined by current position  
        # element or the end of array
        end = min(currentPosition + nums[currentPosition] + 1, n)

        # Iterate through every element within reach
        for i in range(currentPosition + 1, end, 1):
            # For each element within reach, add to the list 
            # their furthest reachable position in the next move 
            availablePosition.append(i+nums[i])
        # Find the furthest reachable position in the next move
        maxPosition = max(availablePosition)
        # If the furthest reachable position in the next move 
        # exceeds n, end of array is reachable
        if maxPosition >= n:
            return True
        else:
            # Get the index of position which will have
            # furthest reachable position in the next move
            maxIndex = availablePosition.index(maxPosition)
            # Move to the position having furthest reachable 
            # position in the next move
            currentPosition = currentPosition + maxIndex + 1
            # If in the next move the furthest reachable position
            # has a value of 0 in its position, we are stuck and 
            # end of array can never be reached
            if nums[currentPosition] == 0:
                return False


# Driver Code 
if __name__ == '__main__':
    nums = [2,3,1,1,4]   # True
    nums2 = [3,2,1,0,4]   # False 
    nums3 = [3, 6, 5, 7, 1, 1, 1, 1, 1, 3, 2, 7, 7]   # True
    nums4 = [3, 6, 5, 7, 1, 1, 1, 1, 1, 1, 0, 3, 2, 7, 7] # False
    nums5 = [3, 1, 2, 3, 1, 1, 3, 1, 1, 0, 1, 0, 6, 7]   # False
    nums6 = [3, 2, 3, 4, 1, 4, 1, 0, 1, 1, 3, 2, 7, 7]   # True
    nums7 = [1, 7, 3, 1, 0, 1, 0, 0, 0, 1, 2, 2, 0, 1, 5] # False
    nums8 = [1, 7, 3, 1, 0, 1, 0, 0, 3, 1, 2, 2, 0, 1, 5]  # True
    print(CanJumpToEnd(nums,0))
    print(CanJumpToEnd(nums2,0))
    print(CanJumpToEnd(nums3,0))
    print(CanJumpToEnd(nums4,0))
    print(CanJumpToEnd(nums5,0))
    print(CanJumpToEnd(nums6,0))
    print(CanJumpToEnd(nums7,0))
    print(CanJumpToEnd(nums8,0))
