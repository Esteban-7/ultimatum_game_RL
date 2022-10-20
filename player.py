import numpy as np



class player_1:
    def __init__(self, epsilon, alpha_learn_rate,actions, memory = False):
        # the actions argument an integer. It will be the endowment in the game, meaning that the player can offer any integer as an action
        #between 0 and the number of actions. 
        self.epsilon = epsilon
        self.alpha = alpha_learn_rate
        self.last_action = 0 
        self.memory = memory
        self.actions = actions
        

        #q_table: for player 1, when memory is activated, an additional row is added to the table. In normal conditions player 1 only has one state since he always does the first move.
        # when setting the memory to true, the two total rows represent the states for the player, where row is the state where player 2 rejected 
        if self.memory: 
            self.q_table = np.zeros(shape=(2,self.actions+1)) 
        else:
            self.q_table= np.zeros(shape=(1,self.actions+1))
        pass

    def move(self, state = 0): #state is 0 by default given that there is no memory by default
        #greedy action
        #First, given the q table for the player and the previous state (always 0 if there is no memory and either 0 or 1 when there is memory,
        # representing the action taken by player 2 in the prev. episode). In the q table, the row representing the state is used (row 0 or 1),
        # in that row the max value is found by the function max(), the index of this value is found with the index functio.
        # The new action is set to be the index of such action (given the structure defined, the index is equal to the offer made)
        
        strategy = np.random.random() #a random number is generated to be compared to the epsilon rate of greedy strategy

        if strategy > self.epsilon: # if the random number generated strategy is greater than epsilon then the greedy action is to be taken
            index_max_q = list(self.q_table[state]).index(max(self.q_table[state])) 
            action = index_max_q
        else: #if the strategy random number generated is not greater than epsilon, the exploring action is to be made
            action =   np.random.randint(low = 0, high = self.actions +1) #The randint integer will generate a random number between 0 and the endowment which will be the offer.  
        return action
        
    def update_qtable(self, action, reward,state):
        #Updates the qtable for the player one according to the action taken. State is set to 0 when no memory is kept, state changes according to the player 2 response on prev episode
        #find the element in the q table that needs to be updated
        if self.memory:
            state = state
        else:
            state = 0
        
        self.q_table[state][action] = self.q_table[state][action]*(1 - self.alpha) + reward*self.alpha #the new value in the table is the apha weighted reward
        pass


class player_2:

    def __init__(self, epsilon,alpha_learn_rate,states, actions = 2, memory = False):
        #States should be the endowment for the game, given that is all possible options that the player 1 can offer. 
        #Actions will be set to 2, player 2 has the option to accept (1) or reject (0) the offer by player 1
        self.epsilon = epsilon
        self.alpha = alpha_learn_rate
        self.last_action = 0
        self.actions = actions 
        self.states = states
        self.memory = memory
        

        #q_table: the q table is set to have N=states rows, representing the states that are the possible offers by player 1. Columns in the table are set to two,
        # given that the player 2 only has two options.
        #when memory is set to True, another dimension is created for the table, given that player 2 has to include its last action 
        if self.memory: 
            self.q_table = np.zeros(shape=(2,self.states+1,self.actions)) 
        else:
            self.q_table= np.zeros(shape=(self.states+1,self.actions))
        pass

    def move(self, state):
        #greedy action
        #Given the state, which in this case will be the offer made by the player 1, the player will decide according to an epsilon - greedy strategy
        strategy = np.random.random()

        if strategy > self.epsilon: # if the random number generated strategy is greater than epsilon then the greedy action is to be taken
            index_max_q = list(self.q_table[state]).index(max(self.q_table[state])) 
            action = index_max_q
        else: #if the strategy random number generated is not greater than epsilon, the exploring action is to be made
            action =   np.random.randint(low = 0, high = self.actions) #one is added giben that the randint function generates an open interval        
        return action

    def update_qtable(self, action, reward,state):
        #To update the qtable for each player 

        #find the element in the q table that needs to be updated
        self.q_table[state][action] = self.q_table[state][action]*(1 - self.alpha) + reward*self.alpha #the new value in the table is the apha weighted reward
        
        pass


    