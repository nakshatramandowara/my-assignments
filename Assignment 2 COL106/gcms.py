from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException


def comp_binID(binID1,binID2):
    if(binID1[0]<binID2[0]):
        return -1
    elif(binID1[0]==binID2[0]):
        return 0
    else:
        return 1

def comp_objectID(objID1,objID2):
    if(objID1[0]<objID2[0]):
        return -1
    elif(objID1[0]==objID2[0]):
        return 0
    else:
        return 1

def comp_BLUEGREEN(bin1,bin2):
    if(bin1.capacity<bin2.capacity):
        return -1
    elif(bin1.capacity==bin2.capacity and bin1.id<bin2.id):
        return -1
    elif(bin1.capacity==bin2.capacity and bin1.id==bin2.id):
        return 0
    else:
        return 1

def comp_YELLOWRED(bin1,bin2):
    if(bin1.capacity<bin2.capacity):
        return -1
    elif(bin1.capacity==bin2.capacity and bin1.id>bin2.id):
        return -1
    elif(bin1.capacity==bin2.capacity and bin1.id==bin2.id):
        return 0
    else:
        return 1


    
class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.BinID_Tree=AVLTree(comp_binID)
        self.ObjectID_Tree=AVLTree(comp_objectID)
        self.BlueGreenTree=AVLTree(comp_BLUEGREEN)
        self.YellowRedTree=AVLTree(comp_YELLOWRED)


    def add_bin(self, bin_id, capacity):
        new_bin=Bin(bin_id,capacity)
        self.BinID_Tree.insert((bin_id,new_bin))
        self.BlueGreenTree.insert(new_bin)
        self.YellowRedTree.insert(new_bin)

    def add_object(self, object_id, size, color):
       
        my_object=Object(object_id,size,color)
        
        if(my_object.colour==1): #Blue- compact fit,least ID
            found_bin=self.compactfit(my_object,self.BlueGreenTree)
        elif(my_object.colour==2):#Yellow- compact fit,greatest ID
            found_bin=self.compactfit(my_object,self.YellowRedTree)
        elif(my_object.colour==3):#Red- largest fit,greatest ID
            found_bin=self.largestfit(my_object,self.YellowRedTree)
        else:#Green- largest fit,greatest ID
            found_bin=self.largestfit(my_object,self.BlueGreenTree)

        if(found_bin==None):
            raise NoBinFoundException
        else:
            x=found_bin.element
            self.YellowRedTree.delete(x)
            self.BlueGreenTree.delete(x)#delete and insert the bin again
            x.add_object(my_object)
            self.YellowRedTree.insert(x)
            self.BlueGreenTree.insert(x)
            self.ObjectID_Tree.insert((object_id,x))
            
        
    def compactfit(self,myobject:Object,tree):
        
        parent=None
        current=tree.root
       
        while(current):
            if(myobject.size<=current.element.capacity):
                parent=current
                current=current.left
            else:
                current=current.right
        return parent # returns None if no valid bin is found


    def largestfit(self, myobject:Object,tree):
        
       
        current=tree.root
        while(current.right):
            current=current.right
        
        if(current and myobject.size<=current.element.capacity):
            return current
        else:
            return None


    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        X=self.ObjectID_Tree.delete((object_id,None))
        if(not X):
            return
        object_bin=X[1]
        self.YellowRedTree.delete(object_bin)
        self.BlueGreenTree.delete(object_bin)
        object_bin.remove_object(object_id)
        self.YellowRedTree.insert(object_bin)
        self.BlueGreenTree.insert(object_bin)
         

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        X=self.BinID_Tree.search_return_none_if_not_found((bin_id,None))
        if(X):
            return (X.element[1].capacity,X.element[1].return_list_of_objectIDs())
        else:
            return None


    def object_info(self, object_id):
        # returns the bin_id in which thes object is stored
        X=self.ObjectID_Tree.search_return_none_if_not_found((object_id,None))
        if(X):
            object_bin=X.element[1]
            return object_bin.id
        else:
            return None
    
    
