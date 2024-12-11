import numpy as np
import random
class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. If you think there is no better strategy than 2a,
        then implement the same strategy here. Else implement that non greedy strategy here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        x = self.results[-1]
        if x == 1:#choosing between Attack v/s defense when Bob is attacking
            if 11 * self.points < 5 * len(self.results):
                return 0
            else:
                return 2
        if x == 0:
           
            return 1
        else:  # draw case (x == 0.5)
            return 0
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
       

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_style, bob_style = alice.play_move(), bob.play_move()
    p1, p2, p3 = payoff_matrix[alice_style][bob_style]
    
    q=p1+p2+p3
    x = random.randint(1, q)#used only ints, no floats for better accuracy and lower runtime
    if x <= p1:
        result = 1
    elif x <= p1 + p2:
        result = 0.5
    else:
        result = 0
    alice.observe_result(alice_style, bob_style, result)
    bob.observe_result(bob_style, alice_style, 1 - result)
    # Update payoff_matrix[0][0]
    payoff_matrix[0][0] = (int(bob.points*2) ,0 ,int(alice.points*2))
    #multiply by 2 to make points integer(score can be x.5)
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    payoff_matrix = [#using integers only,no floats, by taking lcm and only storing numerators
        [(1, 0, 1), (7, 0, 3), (5, 0, 6)],
        [(3, 0, 7), (1, 1, 1), (3, 5, 2)],
        [(6, 0, 5), (2, 5, 3), (1, 8, 1)]
    ]
    alice = Alice()
    bob = Bob()
    for _ in range(num_rounds):
        simulate_round(alice, bob, payoff_matrix)

    # print(alice.results)
    # print(bob.results)
    return alice.points
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10^5)