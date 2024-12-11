"""
Use the following function to convert the decimal fraction of k/N into it's binary representation
using k_prec number of bits after the decimal point. You may assume that the expansion of 
k/N terminates before k_prec bits after the decimal point.
"""
def decimalToBinary(num, k_prec) : 
  
    binary = ""  
    Integral = int(num)    
    fractional = num - Integral 
   
    while (Integral) :       
        rem = Integral % 2
        binary += str(rem);  
        Integral //= 2

    binary = binary[ : : -1]  
    binary += '.'

    while (k_prec) : 
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) :  
            fractional -= fract_bit  
            binary += '1'       
        else : 
            binary += '0'
        k_prec -= 1
        
    return binary 

def win_probability(p, q, k, N):
    """
    Return the probability of winning while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    total_probability=0
    x=decimalToBinary(k/N,100)
    multiplier=1.0
    for char in x:
        if(char=='1'):
            total_probability+=p*multiplier
            multiplier=multiplier*q
        elif(char=='0'):
            multiplier*=p
    return total_probability
            

        

def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined while gambling aggressively.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    total_expectation=0
    x=decimalToBinary(k/N,100)[1:]#remove point

    trailing_zeroes=0
    for char in x[::-1]:
        if(char=='0'):
            trailing_zeroes+=1
        else:
            break
    if(trailing_zeroes>0):
        x=x[:-trailing_zeroes]
    
    multiplier=1.0
    for char in x:
        if(char=='1'):
            total_expectation+=1*multiplier
            multiplier*=q
        elif(char=='0'):
            total_expectation+=1*multiplier
            multiplier*=p
    return total_expectation


