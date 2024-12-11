import hash_table as ht


def normal_comparator(x,y,handle_equality=False):
    if(handle_equality and x==y):
       return '='
    return x<y

def key_comparator(x,y,handle_equality=False):
    if(handle_equality and x[0]==y[0]):
        return '='
    return x[0]<y[0]

def merge(a,b,comparator):
    n=len(a)
    m=len(b)
    merged_array=[]
    i,j=0,0
    while(i<n and j<m): 
        if(comparator(a[i],b[j])):
            merged_array.append(a[i])
            i+=1
        else:
            merged_array.append(b[j])
            j+=1

    merged_array.extend(a[i:])
    merged_array.extend(b[j:])
    return merged_array

def merge_Sort(A ,comparator):#input array and comparator
    if(len(A)<=1):
        return A
    mid=(len(A)-1)//2
    a=merge_Sort(A[:mid+1],comparator)
    b=merge_Sort(A[mid+1:],comparator)
    
    return merge(a,b,comparator)

def binary_search(x,A,comparator,L=0,R=None):
    if(R==None):
        R=len(A)-1
    if(L>R):
        return None
    mid=(L+R)//2
    if(comparator(x,A[mid],True)==True):#handle equality =True
        return binary_search(x,A,comparator,L,mid-1)
    elif(comparator(x,A[mid],True)=='='):
        return mid
    else:
        return binary_search(x,A,comparator,mid+1,R)

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        texts=[merge_Sort(text,normal_comparator) for text in texts]#sort each text
        for text in texts:#remove duplicate words in each text 
            duplicate_free_text = [text[i] for i in range(len(text)-1) if not text[i]==text[i+1]]
            duplicate_free_text.append(text[-1])#append last element as it was left out
            text[:]=duplicate_free_text#modify in place
           
        self.my_library = list(zip(book_titles,texts))
        self.my_library=merge_Sort(self.my_library,key_comparator)#sort by book titles
        
        
    
    def distinct_words(self, book_title):
        index=binary_search((book_title,None),self.my_library,key_comparator)
        return self.my_library[index][1]
        
    
    def count_distinct_words(self, book_title):
        return len(self.distinct_words(book_title))
    
    def search_keyword(self, keyword):
        return [book_title for book_title,text in self.my_library if binary_search(keyword,text,normal_comparator)!=None]

    
    def print_books(self):
        for book_title,text in self.my_library:
            print(book_title+': ',end='')
            print(" | ".join(text))
            

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        if(name=="Jobs"):
            self.name="Chain"
        elif(name=="Gates"):
            self.name="Linear"
        else:
            self.name="Double"
        self.params=params
        self.Map=ht.HashMap(self.name,self.params)

    
    def add_book(self, book_title, text):#complexity O(W+table_size)
        textset=ht.HashSet(self.name,self.params)#O(table_size)
        
        for word in text:#O(W)
            textset.insert(word)
        self.Map.insert((book_title,textset))

    
    def distinct_words(self, book_title):
        textset=self.Map.find(book_title)
        if(self.name!='Chain'):
            return [word for word in textset.table if word]
        else:
            x=[]
            for slot in textset.table:
                if(slot):
                    x.extend(slot)
            # print(x)
            return x


    
    def count_distinct_words(self, book_title):
        textset=self.Map.find(book_title)
        return textset.n
        
    
    def search_keyword(self, keyword):
        required_books=[]
        for slot in self.Map.table:
            if(slot):
                if(self.name!='Chain'):
                    book_title,textset=slot
                    if(textset.find(keyword)):
                        required_books.append(book_title)
                else:#chaining case
                    for item in slot:
                        book_title,textset=item
                        if(textset.find(keyword)):
                            required_books.append(book_title)
        return required_books
    
    def print_books(self):
        for slot in self.Map.table:
            if(slot):
                if(self.name!='Chain'):
                    book_title,textset=slot
                    print(book_title+': ',end='')
                    print(textset)
                else:
                    for item in slot:
                        book_title,textset=item
                        print(book_title+': ',end='')
                        print(textset)
                        


