def calc_score(nA, nB, totalrounds, payoffmatrix, dp):
    payoffmatrix[0][0]=(nB/(nA+nB),0,nA/(nA+nB)) #update payoffmatrix[0][0]
    if nA + nB == totalrounds: #game is over
        return 0
    
    if dp[int(2*nA)][int(2*nB)][totalrounds] != None: #multiply by 2 to handle non int indexes
        return dp[int(2*nA)][int(2*nB)][totalrounds]
    
    max_s = 0
    for i in range(3):
        s = sum(payoffmatrix[i][j][k] * ((2-k)/2 + calc_score(
                nA + (2-k)/2, nB + k/2, totalrounds, payoffmatrix, dp))
            for j in range(3)
            for k in range(3)
        )
        s=s/3
        max_s = max(max_s, s) #find best output out of all three strategies (0,0,1),(1,0,0),(0,1,0)
    
    dp[int(2*nA)][int(2*nB)][totalrounds] = max_s
    return max_s

def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice to maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).
    
    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive
    """
    best_s = 0
    best_i = None
    dp = [[[None for i in range(tot_rounds + 1)] for j in range(2*tot_rounds + 1)] for k in range(2*tot_rounds + 1)]
    payoffmatrix = [
        [(0.5, 0, 0.5), (0.7, 0, 0.3), (5/11, 0, 6/11)],
        [(0.3, 0, 0.7), (1/3, 1/3, 1/3), (0.3, 0.5, 0.2)],
        [(6/11, 0, 5/11), (0.2, 0.5, 0.3), (0.1, 0.8, 0.1)]
    ]
    for i in range(3):
        s = sum(payoffmatrix[i][j][k] * ((2-k)/2 + calc_score(
                na + (2-k)/2, nb + k/2, tot_rounds,payoffmatrix,dp
            ))
            for j in range(3)
            for k in range(3)
        ) 

        if s > best_s:
            best_s = s
            best_i = i

    probs = [0, 0, 0]
    probs[best_i] = 1
    return probs

def expected_points(tot_rounds):
    """
    Given the total number of rounds(tot_rounds), calculate the expected points that Alice can score after the tot_rounds,
    assuming that Alice plays optimally.

    Return : The expected points that Alice can score after the tot_rounds.
    """
    payoffmatrix = [
        [(0.5, 0, 0.5), (0.7, 0, 0.3), (5/11, 0, 6/11)],
        [(0.3, 0, 0.7), (1/3, 1/3, 1/3), (0.3, 0.5, 0.2)],
        [(6/11, 0, 5/11), (0.2, 0.5, 0.3), (0.1, 0.8, 0.1)]
    ]
    if((tot_rounds+1)*(2*tot_rounds+1)*(2*tot_rounds+1)>10**5):
        return None
    dp = [[[None for i in range(tot_rounds + 1)] for j in range(2*tot_rounds + 1)] for k in range(2*tot_rounds + 1)]
    return 1 + calc_score(1, 1, tot_rounds, payoffmatrix, dp)

print(expected_points(6))