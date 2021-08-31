import print_tree

#Create a node class to store data in a parse tree
#Node should have reference links to left, right and parent 
class Node:
    def __init__ (self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent

root = Node("")

#Create a function to build a parse tree from a fully parenthesized mathematical expression in infix notation.
def buildParseTree(exp):
    explist = exp.split()
    currentNode = root
    
    print('root: ', root.val)
    
    for expression in explist:

        #left parentheses, right parentheses, operators, and operands.
        if expression == '(':
            
            #print('expression: ', expression)
            
            # create a node and make it the left of the currentNode
            node = Node(expression)
            currentNode.left = node
            #newNode.left = currentNode.left
            
            #print('newNode: ', newNode.val)
            
            # then descent to that left child (ie: currentNode equal to left child)
            currentNode = node
            
            #print('currentNode: ', currentNode.val)
            
        elif expression == ')':
            # go up to the parent of the currentNode
            currentNode = currentNode.parent

        elif expression in '+-*/':
            
            #print('expression: ', expression)
            
            # set value of the currentNode to that operator
            currentNode.val = expression
            
            # create a node and make it the right child of the currentNode
            #newNode = Node(expression)
            node = Node(expression)
            currentNode.right = node
   
            #print('newNode: ', newNode.val)

            # then descend to that right child
            currentNode = node
            
            #print('currentNode: ', currentNode.val)

        #elif expression not in '+-*/':
            # expression is a number
            # set value of the currentNode to that number
            currentNode.val = expression
            
            # go back up to our parent
            #currentNode = root
            
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
        
#Create a function to traverse and print the parse tree in pre-order. You will need to use recursion.
def inPreOrder(node):
    # - Recursively do a preorder traversal of the left subtree
    # - Visit root node first
    # - Recursively do a preorder traversal of the right subtree
    if node:
        inPreOrder(node.left)
        print(node.val)
        inPreOrder(node.right)
    
#Create a function to traverse and print the parse tree in post-order. You will need to use recursion.
def inPostOrder(node):
    # - Recursively do a postorder traversal of the left subtree
    # - Visit root node first
    # - Recursively do a postorder traversal of the right subtree
    if node:
        inPostOrder(node.left)
        print(node.val)
        inPostOrder(node.right)
    
#buildParseTree("( ( 11 * 2 ) + ( 10 - 2 ) )")
buildParseTree("( 11 * 2 )")

print_tree.print_tree(root)

#inOrder(root)

#inPreOrder(root)

#inPostOrder(root)