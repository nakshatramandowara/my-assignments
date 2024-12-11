
'''
Python Code to implement a heap with general comparison function
'''
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.comparator=comparison_function
        self.heap_array=init_array
        self.build_heap()#makes heap_array an actual heap
        
    
    def MIN_downheap(self,i):
        l=2*i+1
        r=2*i+2
        smallest=i
        length=len(self.heap_array)
        if(l<length and (self.comparator(self.heap_array[l],self.heap_array[smallest]))): #A[l]<A[smallest]
            smallest=l
        if(r<length and (self.comparator(self.heap_array[r],self.heap_array[smallest]))):#A[r]<A[smallest]
            smallest=r
        if(smallest!=i):
            self.heap_array[i],self.heap_array[smallest]=self.heap_array[smallest],self.heap_array[i]# swap A[i] with the smallest of the 3
            self.MIN_downheap(smallest)
            
        
    def build_heap(self):
        n=len(self.heap_array)
        for i in range((n-1)//2,-1,-1):
            self.MIN_downheap(i)
            
    def MIN_upheap(self,i):
        if(i<=0):
            return
        parent=(i-1)//2
       
        if(self.comparator(self.heap_array[i],self.heap_array[parent])):#A[i]<A[parent]
            self.heap_array[i],self.heap_array[parent]=self.heap_array[parent],self.heap_array[i]#swap upwards
            self.MIN_upheap(parent) #recursive call
        else:
            return #do nothing
    
    
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.heap_array.append(value)
        # print(self.heap_array)
        self.MIN_upheap(len(self.heap_array)-1)
        
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        
        self.heap_array[0],self.heap_array[-1]=self.heap_array[-1],self.heap_array[0]#swap root and last element
        root=self.heap_array.pop()
        self.MIN_downheap(0)
        return root
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        # Write your code here
        if(self.heap_array):
            return self.heap_array[0]
        else:
            return None
        
        
    def __repr__(self, index=0, level=0, prefix="Root: "):
        if index >= len(self.heap_array):
            return ""

        ret = "|\t" * level + prefix + repr(self.heap_array[index].load_key) + "\n"

        left_index = 2*index+1
        right_index = 2*index+2

        if left_index < len(self.heap_array):
            ret += self.__repr__(left_index, level + 1, prefix="L--- ")
        if right_index < len(self.heap_array):
            ret += self.__repr__(right_index, level + 1, prefix="R--- ")

        return ret
    # You can add more functions if you want to
def simple_comparator(val1,val2):
    if(val1<val2):
        return True
    else:
        return False
# X=[4,3,2,16,9,10,14,8,7]
# myheap=Heap(simple_comparator,X)

# print(myheap.heap_array)
# myheap.insert(1)
# print(myheap)
# print(myheap.extract())
# print(myheap)