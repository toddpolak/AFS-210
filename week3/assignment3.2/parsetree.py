import print_tree

class Node:
    def __init__ (self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent

root = Node("")

def buildParseTree(exp):
    explist = exp.split()
    currentNode = root

    for expression in explist:
        print(expression)

        #left parentheses, right parentheses, operators, and operands.
        if expression == '(':
            # create a node and make it the left of the currentNode
            
            node = Node(expression)
            currentNode.left = node
            
            # then descent to that left child (ie: currentNode equal to left child)  

        #elif expression == ')':
            # go up to the parent of the currentNode
            
        #elif expression in '+-*/':
            # set value of the currentNode to that operator
            # create a node and make it the right child of the currentNode
            # then descend to that right child

        #elif expression not in '+-*/':
            # expression is a number
            # set value of the currentNode to that number
            # go back up to our parent
                
        #else:
            #raise ValueError("Unknown Operator: " + expression)

#Create a function to traverse and print the parse tree in order .  You will need to use recursion.
def inOrder(node):
    # - Recursively do a inorder traversal of the left subtree
    # - Visit root node first
    # - Recursively do a inorder traversal of the right subtree
    if node:
        inOrder(node.left)
        print(node.val)
        inOrder(node.right)
        
def inPreOrder(node):
    # - Recursively do a preorder traversal of the left subtree
    # - Visit root node first
    # - Recursively do a preorder traversal of the right subtree
    if node:
        inPreOrder(node.left)
        print(node.val)
        inPreOrder(node.right)
    
def inPostOrder(node):
    # - Recursively do a postorder traversal of the left subtree
    # - Visit root node first
    # - Recursively do a postorder traversal of the right subtree
    if node:
        inPostOrder(node.left)
        print(node.val)
        inPostOrder(node.right)
    
buildParseTree("( ( 11 * 2 ) + ( 10 - 2 ) )")

print_tree.print_tree(root)

inOrder(root)

inPreOrder(root)

inPostOrder(root)