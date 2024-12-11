"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M +M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

def mod_inverse(a, m):
        def egcd(a, b):
            if a == 0:
                return (b, 0, 1)
            else:
                g, y, x = egcd(b % a, a)
                return (g, x - (b // a) * y, y)

        g, x, _ = egcd(a, m)
        return x % m
# Problem 1a
def calc_helper(a,b,dp):
        if(dp[a-1][b-1]!=None):
             return dp[a-1][b-1]
        if(a==1):
                p=mod_multiply(calc_helper(a,b-1,dp)[0],a)
                q=mod_multiply(calc_helper(a,b-1,dp)[1],a+b-1)
                
        elif(b==1):
                p=mod_multiply(calc_helper(a-1,b,dp)[0],b)
                q=mod_multiply(calc_helper(a-1,b,dp)[1],a+b-1)
        else:
                p=mod_add(mod_multiply(calc_helper(a-1,b,dp)[0],b),mod_multiply(calc_helper(a,b-1,dp)[0],a))
                q=mod_multiply(calc_helper(a-1,b,dp)[1],a+b-1)
        dp[a-1][b-1]=(p,q)
        return (p,q)

def calc_prob(alice_wins, bob_wins):
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    dp=[[None]*bob_wins for _ in range(alice_wins)]
    dp[0][0]=(1,1)#n_A=1,n_B=1 case
    
    p,q=calc_helper(alice_wins,bob_wins,dp)

    return (p* mod_inverse(q,M))%M

# Problem 1b (Expectation) 
# 
# 

def helper2(t,dp,square=False):
        sum=(0,1)# sum = p/q, stored as tuple(p,q)
        for i in range(1,t):
            p,q=calc_helper(i,t-i,dp)
            
            p=p*(2*i-t)
            if(square):#use of additional input square to calculate E(Z^2) similarly to E(Z)
                #basically clever reuse of code
                p*=(2*i-t)
            a,b=sum
            sum=(mod_add(mod_multiply(p,b),mod_multiply(a,q)),mod_multiply(b,q))
        return sum

def calc_expectation(t):
    """
    Returns:
        The expected value of um_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    dp=[[None]*t for _ in range(t)]
    dp[0][0]=(1,1)#n_A=1,n_B=1 case
    
    p,q=helper2(t,dp)
    return (p* mod_inverse(q,M) )%M


# Problem 1b (Variance)
def calc_variance(t):
    """
    Returns:
        The variance of um_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

        for some reason the answer is of type t/3 always
    """
    dp=[[None]*t for _ in range(t)]
    dp[0][0]=(1,1)
    p,q=helper2(t,dp,True)#E(Z^2)
    a,b=helper2(t,dp)#E(Z)
    a,b=mod_multiply(a,a),mod_multiply(b,b)#(E(Z))^2
    p=mod_add(mod_multiply(p,b),-mod_multiply(a,q))#E(Z^2)-(E(Z))^2
    q=mod_multiply(b,q)
    return (p* mod_inverse(q,M) )%M

print(calc_expectation(10))


    
