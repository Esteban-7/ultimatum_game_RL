import pandas as pd
import numpy as np

## Defines the class for the ultimatum game. 


class ultimatum:
    
    def __init__(self,episodes, player_1, player_2, endowment,policy):
        # The constructor of the ultimatum class.
        # episodes is the number of episodes to be played. 
        # Takes 2 players that must be of the class player_1 and player_2 defined in the player module. 
        # The endowment is the amount of money that will be divided in the game. 
        # The policy argument defines the proportion of the endowment that player 2 will ask as a minimum to accept the offer in the case that the game is set to have fixed or dynamic rules.


        self.episodes = episodes
        self.player_1 = player_1
        self.player_2 = player_2
        self.endowment = endowment
        self.policy = policy
        
        # Empty lists for results, rewards and payoffs are created to save the results for every episode and later access to this information
        self.player_1_actions = []
        self.player_2_actions = []
        self.player_2_average_actions = []
        self.player_1_rewards = []
        self.player_2_rewards = []
        self.player_1_payoff = []
        self.player_2_payoff = []

        pass


    def episode(self):
        # Defines the steps taken in each episode of the game.
        # First player 1 makes a move, meaning that he makes an offer for player 2.
        # Player 2 then accepts the offer or rejects it. 
        # According to the action by player 2, the rewards are set.
        # The q values of the q tables are updated for both players according to the actions taken. 
        # Actions, rewards and payoffs are stored in the lists previously initialized to keep track of the game 
        
        player_1_action = self.player_1.move() 
        player_2_action = self.player_2.move(state = player_1_action, p = self.policy)
        
        if player_2_action == 0: #if player 2 rejects the offer 
            reward_player_1  = 0
            reward_player_2  = 0
        else:
            reward_player_1  = self.endowment - player_1_action
            reward_player_2 = player_1_action

        
        self.player_1.update_qtable(action = player_1_action, reward = reward_player_1)
        self.player_2.update_qtable(action = player_2_action, reward = reward_player_2, state = player_1_action)
        
        self.player_1_actions.append(player_1_action)
        self.player_2_actions.append(player_2_action)
        self.player_2_average_actions.append(np.mean(self.player_2_actions))
        self.player_1_rewards.append(reward_player_1)
        self.player_2_rewards.append(reward_player_2)
        self.player_1_payoff.append(sum(self.player_1_rewards))
        self.player_2_payoff.append(sum(self.player_2_rewards))
        pass

    def play(self, dynamic = False, policy_values = None):
        # Defines the behaviour for the game, that is, the repetitions of the episodes. 
        # If the policy is dynamic, that is, the policy for player_2 to accept (which is external) is shifting in time, the policy levels must be given as an argument.
        # For the number of episodes, an episode will be played, if the game has a dynamic policy, the value of p will be changed according to the information given. 
        # After all episodes are played, the attribute results is created by joining the lists of all results into a dataframe for easier comprehension.

        for i in range(self.episodes):
            if dynamic:
                if i in policy_values.keys():
                    self.policy = policy_values[i]
            self.episode()
        
        
        self.results = pd.DataFrame(list(zip(self.player_1_actions,self.player_2_actions,self.player_2_average_actions, self.player_1_rewards,self.player_2_rewards,self.player_1_payoff,self.player_2_payoff)),
                        columns=["A's offer","B's action","B's average actions","A's reward","B's reward","A's payoffs","B's payoffs"])
        
        pass
