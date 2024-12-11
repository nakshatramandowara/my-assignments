from prime_generator import get_next_size

def polynomial_calculator(s,z,c):
    p=[ord(char)+26-65 if ord(char)<=90 else ord(char)-97 for char in s]
    sum=0
    multiplier=1
    for i in range(len(p)):
        sum+=multiplier*p[i]
        multiplier*=z
        sum%=c
    return sum



class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type=collision_type

        if(self.collision_type=="Double"):
            self.z1,self.z2,self.c2,self.table_size=params
        else:
            self.z,self.table_size=params
        self.n=0  #no. of elements in the table
        self.table=[None]*self.table_size
    

     
    def h2(self,key):
        return self.c2- polynomial_calculator(key,self.z2,self.c2)

    def insert(self, x, map_or_set):
        if(map_or_set=='map'):
            key=x[0]
        else:
            key=x
        index=self.get_slot(key)
        if(self.collision_type=='Chain'):
            if(self.table[index]==None):
                self.table[index]=[]
            if(x not in self.table[index]):#check if already present
                self.table[index].append(x)
                self.n+=1

            return
        step_size=self.h2(key) if self.collision_type=='Double' else 1
        for j in range(0,self.table_size):
                next_slot=(index+j*step_size) %self.table_size
                if(self.table[next_slot]==x):#already present
                    return
                elif(self.table[next_slot]==None): #found empty slot
                    self.table[next_slot]=x
                    self.n+=1
                    return
                
        raise Exception("Table is full")
        

    def find(self, key):
        pass
        
    
    def get_slot(self, key):
        if(self.collision_type=='Double'):
            return polynomial_calculator(key,self.z1,self.table_size) 
        else:
            return polynomial_calculator(key,self.z,self.table_size) 

    
    def get_load(self):
        return self.n/self.table_size
    
    
    def __str__(self):
        pass
        
                        

    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
    
    def insert(self, key):
        super().insert(key,'set')    
                
    
    def find(self, key):
        index=self.get_slot(key)
        slot=self.table[index]
        if(slot==None):
                return False
        if(self.collision_type=='Chain'):
            for ele in slot:
                if(ele==key):
                    return True

        step_size= self.h2(key) if self.collision_type=='Double' else 1

        for j in range(0,self.table_size):
                next_slot=(index+j*step_size) %self.table_size
                if(self.table[next_slot]==None):
                    return False
                elif(self.table[next_slot]==key):
                    return True

        return False
    
    def __str__(self):
        output=[]
        if(self.collision_type=='Chain'):
            for slot in self.table:
                if(slot==None):
                    output.append('<EMPTY>')
                else:
                    output.append(" ; ".join(slot))
                
        else:
            for slot in self.table:
                if(slot==None):
                    output.append('<EMPTY>')
                else:
                    output.append(slot)
        return " | ".join(output)
    
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
    
    def insert(self, x):
        # x = (key, value)
        super().insert(x,'map')
    
    def find(self, key):
        index=self.get_slot(key)
        slot=self.table[index]
        if(slot==None):
                return None
        if(self.collision_type=='Chain'):
            for ele in slot:
                if(ele[0]==key):
                    return ele[1]
        step_size= self.h2(key) if self.collision_type=='Double' else 1

        for j in range(0,self.table_size):
                next_slot=(index+j*step_size) %self.table_size
                if(self.table[next_slot]==None):
                    return None
                elif(self.table[next_slot][0]==key):
                    return self.table[next_slot][1]

        return None
    
    def format_entry(self, entry):
        """Helper method to format individual entries based on their type using f-strings."""
        return f"({entry[0]}, {entry[1]})"
    
    def __str__(self):
        output=[]
        if(self.collision_type=='Chain'):
            for slot in self.table:
                if(slot==None):
                    output.append('<EMPTY>')
                else:
                    output.append(" ; ".join(map(self.format_entry, slot)))   
        else:
            for slot in self.table:
                if(slot==None):
                    output.append('<EMPTY>')
                else:
                    output.append(self.format_entry(slot))
        return " | ".join(output)
    


