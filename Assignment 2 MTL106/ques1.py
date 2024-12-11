def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    x=q/p
    if(x==1):
        return k/N
    else:
        return (1-x**k)/(1-x**N)

def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    x=q/p
    if(p>q):
        return (1-x**k)
    else:
        return 0

def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    x=q/p
    if(x==1):
        return k*(N-k)           
    return (N*(1-x**k)/(1-x**N)-k)/(p-q)