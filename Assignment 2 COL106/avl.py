from node import Node

class AVLTree:
    def __init__(self,compare_function):
        self.root = None
        self.comparator = compare_function
        self.size=0

   
    def search(self,element):
        """Helper function to recursively search for a element."""
        node=self.root
        parent = None
        while node is not None:
            if (self.comparator(element,node.element)==0):
                return node  # Node found
            parent = node
            if (self.comparator(element, node.element)==-1):  # element < node.element
                node = node.left
            else:
                node = node.right
        return parent #returns node at bottom of path if node not found
    

    def search_return_none_if_not_found(self,element):
        """Helper function to recursively search for a element."""
        node=self.root
        while node is not None:
            if (self.comparator(element,node.element)==0):
                return node  # Node found
            if (self.comparator(element, node.element)==-1):  # element < node.element
                node = node.left
            else:
                node = node.right
        return node


    def relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)."""
        if make_left_child:  # make it a left child
            parent.left = child
        else:  # make it a right child
            parent.right = child
        if child is not None:  # make child point to parent
            child.parent = parent


    def rotate(self, x):
        """Rotate Position x above its parent."""
        
        y = x.parent  # we assume this exists
        z = y.parent  # grandparent (possibly None)
        
        if z is None:
            self.root = x  # x becomes root
            x.parent = None
        else:
            self.relink(z, x, y == z.left)  # x becomes a direct child of z
        
        # Now rotate x and y, including transfer of middle subtree
        if x == y.left:
            self.relink(y, x.right, True)  # x.right becomes left child of y
            self.relink(x, y, False)       # y becomes right child of x
        else:
            self.relink(y, x.left, False)  # x.left becomes right child of y
            self.relink(x, y, True)        # y becomes left child of x


    def restructure(self, x):
        """Perform trinode restructure of Position x with parent/grandparent."""
        y = x.parent
        z = y.parent
        
        if (x == y.right) == (y == z.right):  # matching alignments
            self.rotate(y)  # single rotation (of y)
            return y  # y is new subtree root
        else:  # opposite alignments
            self.rotate(x)  # double rotation (of x)
            self.rotate(x)
            return x

    def recompute_height(self, p):
        p.height = 1 + max(p.left_height(), p.right_height())


    def is_not_balanced(self, p):
        return abs(p.left_height() - p.right_height()) > 1


    def tall_child(self, p, favor_left=False):  # parameter controls tie breaker
        if p.left_height() + (1 if favor_left else 0) > p.right_height():
            return p.left
        else:
            return p.right


    def tall_grandchild(self, p):
        child = self.tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == p.left)
        return self.tall_child(child, alignment)


    def insert(self,element):
        self.size=1
        if(self.root==None) :   
            self.root=Node(element)
            return
        
        p=self.search(element)#p= node to which element should be inserted(will have max one child)
        if(self.comparator(element,p.element)==-1): #checking if element<p.element
            p.left=Node(element,parent=p)
        else:
            p.right=Node(element,parent=p)
        self.rebalance(p)


    def rebalance(self, p):
        while p is not None:
            old_height = p.height  # trivially 0 if new node
            if self.is_not_balanced(p):  # imbalance detected!
                # perform trinode restructuring, setting p to resulting root,
                # and recompute new local heights after the restructuring
                p = self.restructure(self.tall_grandchild(p))
                self.recompute_height(p.right)
                self.recompute_height(p.left)
                self.recompute_height(p)  # adjust for recent changes
            self.recompute_height(p)
            if p.height == old_height:  # has height changed?
                p = None  # no further changes needed
            else:
                p = p.parent  # repeat with parent


    def after(self, p):
        if p.right is not None:  # Successor is the leftmost position in p's right subtree
            walk = p.right
            while walk.left is not None:
                walk =walk.left
            return walk
        else:  # Successor is the nearest ancestor having p in its left subtree
            walk = p
            ancestor = walk.parent
            while ancestor is not None and walk == ancestor.right:
                walk = ancestor
                ancestor = walk.parent
            return ancestor
        
    def before(self, p):
        if p.left is not None:  # Successor is the leftmost position in p's right subtree
            walk = p.left
            while walk.right is not None:
                walk =walk.right
            return walk
        else:  # Successor is the nearest ancestor having p in its left subtree
            walk = p
            ancestor = walk.parent
            while ancestor is not None and walk == ancestor.left:
                walk = ancestor
                ancestor = walk.parent
            return ancestor
    
    
    def delete(self, element):
        """Remove item associated with element (raise elementError if not found)."""
        self.size=1
        p = self.search_return_none_if_not_found(element)
        if(p):
            y=p.element#save element so we can return it
        else:
            return None

        if p.left and p.right:  # p has two children
            x = self.before(p)#swap with the predecessor of p
            p.element=x.element 
        else:
            x = p #no swap needed here

        # Now x has at most one child
        child = x.left if x.left else x.right
        parent = x.parent

        if child:
            child.parent = parent

        if parent:
            if parent.left == x:
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child
        x.parent=x

        # Start rebalancing from the parent of the deleted node
        self.rebalance(parent)
        return y


