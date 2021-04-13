# A Python3 program to check if a binary tree is a binary search tree

# A binary tree node containing data field, 
# and left and right pointers
class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Returns true if given tree is BST
def isBST(root, l = None, r = None):
    # Base condition
    if (root == None):
        return True

    # if left node exists then check if it has correct data 
    # i.e. left node's data should be less than root's data
    if (l != None and root.data <= l.data):
        return False

    # if right node exists then check if it has correct data 
    # i.e. right node's data should be greater than root's data
    if (r != None and root.data >= r.data):
        return False
    
    # check recursively for every node
    return isBST(root.left, l, root) and \
        isBST(root.right, root, r)


# Driver Code 
if __name__ == '__main__':
    root = newNode(5) 
    root.left = newNode(2) 
    root.left.left = newNode(1)
    root.left.right = newNode(6)   # False 
   # root.left.right = newNode(4)   # True
    root.right = newNode(9) 
    root.right.left = newNode(8) 
    print(isBST(root, None, None))
    
