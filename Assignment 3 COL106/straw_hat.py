'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

def crewmate_comparator(crewmate1,crewmate2):
    return crewmate1.load_key<crewmate2.load_key
        

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        init_array=[crewmate.CrewMate() for _ in range(m)]
        
        self.heap=heap.Heap(crewmate_comparator,init_array)
        self.non_empty_crewmates=[]
            

    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        root_crewmate=self.heap.extract()
        if(not root_crewmate.treasure_list):#if treasure list of root crewmate is empty
            self.non_empty_crewmates.append(root_crewmate)#add it to non empty crewmates list
        root_crewmate.insert_treasure(treasure)
        self.heap.insert(root_crewmate)

    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        complete_list=[]
        for crewmember in self.non_empty_crewmates:
            complete_list.extend(crewmember.process_list())
        complete_list.sort(key= lambda x: x.id)
        return complete_list



            