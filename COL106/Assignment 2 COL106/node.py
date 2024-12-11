class Node:
    def __init__(self,element,parent=None,left_child=None,right_child=None):
        self.element=element
        self.left=left_child
        self.right=right_child
        self.parent=parent
        self.height=0
    
    def left_height(self):
        if(self.left):
            return self.left.height
        else:
            return -1
    
    def right_height(self):
        if(self.right):
            return self.right.height
        else:
            return -1

    def __repr__(self, level=0, prefix="Root: "):
        ret = "|\t" * (level) + prefix + repr(self.element) + f" (H: {self.height})\n"
        if self.left:
            ret += self.left.__repr__(level + 1, prefix="L--- ")
        if self.right:
            ret += self.right.__repr__(level + 1, prefix="R--- ")
        return ret
        
    