import pandas as pd




class ultimatum:
    
    def __init__(self,episodes, player_1, player_2, endowment,policy):
        
        self.episodes = episodes
        self.player_1 = player_1
        self.player_2 = player_2
        self.endowment = endowment
        self.policy = policy
        
        self.player_1_actions = []
        self.player_2_actions = []
        self.player_1_rewards = []
        self.player_2_rewards = []
        self.player_1_payoff = []
        self.player_2_payoff = []

        
        pass


    def episode(self):
        
        player_1_action = self.player_1.move(state = self.player_2.last_action) #always last action of player 2 (initialized always at 0) is passed, but if memmory is not activated, the state is not used. 
        player_2_action = self.player_2.move(state = player_1_action, p = self.policy)
        
        if player_2_action == 0: #if player 2 rejects the offer 
            reward_player_1  = 0
            reward_player_2  = 0
        else:
            reward_player_1  = self.endowment - player_1_action
            reward_player_2 = player_1_action

        
        self.player_1.update_qtable(action = player_1_action, reward = reward_player_1,state = player_2_action)
        self.player_2.update_qtable(action = player_2_action, reward = reward_player_2, state = player_1_action)
        
        self.player_1.last_action = player_1_action
        self.player_2.last_action = player_2_action
        
        self.player_1_actions.append(player_1_action)
        self.player_2_actions.append(player_2_action)
        self.player_1_rewards.append(reward_player_1)
        self.player_2_rewards.append(reward_player_2)
        self.player_1_payoff.append(sum(self.player_1_rewards))
        self.player_2_payoff.append(sum(self.player_2_rewards))
        pass

    def play(self, dynamic = False):
        
        policy_values = {2000:0.35,5000:0.45,7000:0.6,10000:0.4}
        
        for i in range(self.episodes):
            if dynamic:
                if i in policy_values.keys():
                    self.policy = policy_values[i]
            self.episode()
        
        
        self.results = pd.DataFrame(list(zip(self.player_1_actions,self.player_2_actions, self.player_1_rewards,self.player_2_rewards,self.player_1_payoff,self.player_2_payoff)),
                        columns=["A's offer","B's action","A's reward","B's reward","A's payoffs","B's payoffs"])
        
        pass
