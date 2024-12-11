'''
    Python file to implement the class CrewMate
'''
from treasure import Treasure
from heap import Heap

def processing_comparator(t1:Treasure,t2:Treasure):
    if(t1.arrival_time+t1.size<t2.arrival_time+t2.size):
        return True
    elif(t1.arrival_time+t1.size==t2.arrival_time + t2.size and t1.id<t2.id):
        return True
    return False

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        # Write your code here
        self.treasure_list=[]
        self.load_key=0
    
    def insert_treasure(self,treasure: Treasure):
        self.treasure_list.append(treasure)
        if(self.load_key<treasure.arrival_time):
            self.load_key=treasure.arrival_time+treasure.size
        else:
            self.load_key+=treasure.size

    def process_list(self):
        processing_treasure_heap=Heap(processing_comparator,[])
        return_list=[]
        for i in range(len(self.treasure_list)):
            item=self.treasure_list[i]
        
            current_time=self.treasure_list[i].arrival_time
            last_time=self.treasure_list[i-1].arrival_time

            time_passed=current_time-last_time
            # k=1
            while(time_passed>0 and processing_treasure_heap.heap_array):#time_passes is >0 and heap is non empty
                # print(k)
                # k+=1
                root=processing_treasure_heap.extract()#treasure that is being processed currently
                
                if(time_passed<root.size):
                    root.size-=time_passed
                    processing_treasure_heap.insert(root)
                    time_passed=0
                else:
                    time_passed-=root.size
                    root.completion_time=current_time-time_passed
                    return_list.append(root)
            processing_treasure_heap.insert(item.deepcopy())

        last_insertion_time=self.treasure_list[-1].arrival_time
        
        while(processing_treasure_heap.heap_array):

            root=processing_treasure_heap.extract()
            last_insertion_time+=root.size
            root.completion_time=last_insertion_time
            return_list.append(root)
        
        return return_list

        

            



        

    
    # Add more methods if required