# making a class node to be used in the tree traversal for code and making heap
class Node:
    
    # constructor takes the symbol and its probability
    def __init__(self, symbol, prob):

        self.left = None
        self.right = None
        self.symbol = symbol
        self.prob = prob

    # function used to override the heapq compare function 
    def __lt__(self, other):
        return self.prob < other.prob
    
    # Inorder traversal
    # takes the root of the tree, the code untill that node and a dictionary
    # to put the symbol with its code
    def inorderTraversal(self, root, currentCode, codes, inverseCode):
        if root:
            self.inorderTraversal(root.left, currentCode + '0', codes, inverseCode)
            self.inorderTraversal(root.right, currentCode+ '1', codes, inverseCode)
            if not root.symbol is None:
                codes[root.symbol] = currentCode
                inverseCode[currentCode] = root.symbol
        return



