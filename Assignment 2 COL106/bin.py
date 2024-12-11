from avl import AVLTree
from object import Object,Color

def comp_id(object1,object2):
    if(object1.id < object2.id):
        return -1
    elif(object1.id>object2.id):
        return 1
    else:
        return 0

class Bin:
    def __init__(self, bin_id, capacity):
        self.id=bin_id
        self.capacity=capacity
        self.BinTree=AVLTree(comp_id)

    def add_object(self, object):
        self.BinTree.insert(object)
        self.capacity-=object.size
        # Implement logic to add an object to this bin
        

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        
        a=self.BinTree.delete(Object(object_id,0,Color.BLUE))
        self.capacity+=a.size
        return a

    def return_list_of_objectIDs(self):
        a=[]
        def helper(node):
            if(node!=None):
                helper(node.left)
                a.append(node.element.id)
                helper(node.right)
            else:
                return
        helper(self.BinTree.root)
        return a

        

        
    def __repr__(self):
        if self.BinTree.root is None:
            return "Empty Bin"
        return self._tree_repr(self.BinTree.root)

    def _tree_repr(self, node, level=0, prefix="Root: "):
        ret = "|\t" * level + prefix + repr(node.element.id) + f" (H: {node.height} size:{node.element.size} color:{node.element.colour})\n"
        if node.left:
            ret += self._tree_repr(node.left, level + 1, prefix="L--- ")
        if node.right:
            ret += self._tree_repr(node.right, level + 1, prefix="R--- ")
        return ret

        
# bin1 = Bin(2341, 6)
# bin1.add_object(Object(5, 4, Color.RED))
# bin1.add_object(Object(3, 2, Color.GREEN))
# bin1.add_object(Object(7, 1000, Color.RED))
# print(bin1.remove_object(3).colour)

# print(bin1)
