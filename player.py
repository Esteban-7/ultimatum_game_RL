import numpy as np

##Defines the classes related to the different players in the ultimatum game. Two players are described, player_1 is the one to get the endowment and 
## makes an offer to the player 2. Player 2 is to accept or reject the offer by player 1. 

class player_1:
    def __init__(self, epsilon, alpha_learn_rate, actions):
        # The constructor of the class. 
        # epsilon represents the parameter for the epsilon greedy strategy. That means, with epsilon probability the agent will take a random action. 
        # alpha_learn_rate : represents the learning rate used to updated the qtable. 
        #  the actions argument an integer. It will be the endowment in the game, meaning that the player can offer any integer as an action
        #between 0 and the number of actions. 
        self.epsilon = epsilon
        self.alpha = alpha_learn_rate
        self.actions = actions
        
        #q_table: . Given the structure of the game, player 1 only has one state since he always does the first move and it doesn´t depend on player 2's actions.
        self.q_table= np.zeros(shape=(1,self.actions+1))
        pass

    def move(self, state = 0): #state is 0 by default given that there is only state for the player 1
        # This method defines the decision process done by player 1 following an epsilon-greedy strategy. 
        # Takes as argument the state in which the player is (always 0) and returns an integer, representing the offer to be made to player 2.

        # Greedy action
        #First, given the q table for the player, with only one row,in that row the max value is found by the function max(), 
        # the index of this value is found with the index function.
        # The new action is set to be the index of such action (given the structure defined, the index is equal to the offer made).
        
        strategy = np.random.random() #a random number is generated to be compared to the epsilon rate of greedy strategy

        # if the random number generated strategy is greater than epsilon then the greedy action is to be taken. That is, the greedy action will be taken with
        # 1 - epsilon probability. 
        if strategy > self.epsilon: 
            index_max_q = list(self.q_table[state]).index(max(self.q_table[state])) 
            action = index_max_q
        else: #if the strategy random number generated is not greater than epsilon, the exploring action is to be made
            action =   np.random.randint(low = 0, high = self.actions +1) #The randint integer will generate a random number between 0 and the endowment which will be the offer.  
        return action
        
    def update_qtable(self, action, reward,state = 0):
        # Updates the qtable for the player 1 according to the action taken. 
        # State is set to 0.
        # Finds the element in the q table that needs to be updated according to the action taken.

        self.q_table[state][action] = self.q_table[state][action]*(1 - self.alpha) + reward*self.alpha 
        #the new value in the table is the apha weighted reward
        pass


class player_2:

    def __init__(self, epsilon,alpha_learn_rate,states, actions = 2):
        # Constructor for the player 2 class.
        # epsilon represents the parameter for the epsilon greedy strategy. That means, with epsilon probability the agent will take a random action. 
        # alpha_learn_rate : represents the learning rate used to updated the qtable. 
        # States should be the endowment for the game, given that is all possible options that the player 1 can offer. 
        # Actions will be set to 2, player 2 has the option to accept (1) or reject (0) the offer by player 1.

        self.epsilon = epsilon
        self.alpha = alpha_learn_rate
        self.actions = actions 
        self.states = states
        

        #q_table: the q table is set to have N=states rows, representing the states that are the possible offers by player 1. Columns in the table are set to two,
        # given that the player 2 only has two options.
        self.q_table= np.zeros(shape=(self.states+1,self.actions))
        pass

    def move(self, state,*args,**kwargs):
        # This method defines the decision process done by player 2 following an epsilon-greedy strategy. 
        # Takes as argument the state in which the player is (the offer made by player 1) and returns an integer, 0 if rejects, 1 if accepts.
        
        #Greedy action
        #Given the state, which in this case will be the offer made by the player 1, the player will decide according to an epsilon - greedy strategy
        strategy = np.random.random()

        if strategy > self.epsilon: # if the random number generated strategy is greater than epsilon then the greedy action is to be taken
            index_max_q = list(self.q_table[state]).index(max(self.q_table[state])) 
            action = index_max_q
        else: #if the strategy random number generated is not greater than epsilon, the exploring action is to be made
            action =   np.random.randint(low = 0, high = self.actions) #one is added given that the randint function generates an open interval        
        return action

    def update_qtable(self, action, reward, state):
        # Updates the qtable for the player 2 according to the action taken.

        #find the element in the q table that needs to be updated
        self.q_table[state][action] = self.q_table[state][action]*(1 - self.alpha) + reward*self.alpha 
        #the new value in the table is the apha weighted reward
        
        pass


    