from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        self.table_size=get_next_size()
        self.n=0
        if(self.collision_type=='Chain'):
            aux_table=[]
            for slot in self.table:
                if(slot):
                    aux_table.extend(slot)
        else:
            aux_table=[slot for slot in self.table if slot]

        self.table=[None]*self.table_size
        
        for slot in aux_table:
            self.insert(slot)
            
                    
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        self.table_size=get_next_size()
        self.n=0
        if(self.collision_type=='Chain'):
            aux_table=[]
            for slot in self.table:
                if(slot):
                    aux_table.extend(slot)
        else:
            aux_table=[slot for slot in self.table if slot]

        self.table=[None]*self.table_size
        
        for slot in aux_table:
            self.insert(slot)
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()