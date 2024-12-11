import numpy as np

def stationary_distribution(p, q, r, N):
    P = np.zeros((N+1, N+1))
    
    for i in range(N+1):
        if i > 0:
            P[i,i-1] = q[i]
        P[i,i] = r[i]
        if i < N:
            P[i,i+1] = p[i]

   # Solve π * P = π with sum(π) = 1
    # This is equivalent to solving (P.T - I)π = 0 with sum(π) = 1

    A = P.T - np.eye(N+1)
    
    A[0] = 1
    b = np.zeros(N+1)
    b[0] = 1
    
    return np.linalg.solve(A, b)

def expected_wealth(p, q, r, N):
    pi = stationary_distribution(p, q, r, N)
    return sum(i * pi[i] for i in range(N+1))

def expected_time(p, q, r, N, a,b):
    A = np.zeros((N+1, N+1))
    B = np.ones(N+1)
    
    for i in range(N+1):
        if i == b:
            A[i,i] = 1
            B[i] = 0
        else:
            if i > 0:
                A[i,i-1] = -q[i]
            A[i,i] = 1 - r[i]
            if i < N:
                A[i,i+1] = -p[i]
    
    times = np.linalg.solve(A, B)
    return times[a]

