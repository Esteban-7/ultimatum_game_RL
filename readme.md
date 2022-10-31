# Ultimatum Game - Reinforcement Learning. 

Run simulations with artificial agents playing the ultimatum game. 
Following the design patterns for games with set rules by 
Zhong, F., O. Kimbrough, S., & Wu, D. (2002). Cooperative Agent Systems: Artificial Agents Play the Ultimatum Game. Group Decision and Negotiation, 433-447. 


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Getting-started ">Getting started</a></li>
    <li><a href="#Players">Players</a></li>
    <li><a href="#Ultimatum">Ultimatum</a></li>
    <li><a href="#Game (notebook)">Game</a></li>
  </ol>
</details>



## Getting Started

The ultimatum game is proposed in game theory, in this game, an agent A is given an endowmente and it musts split it with an agent B. Agent A makes the decision of how much of the endowment offer to agent B. Agent B makes choices to accept or reject the offer. If agent B accepts the offer, agent A keeps the endowment minus the offer made, agent B keeps the amount of the offer made by agent A. If agent B rejects the offer, both agents end up with a reward of 0. In the theory, the outcome of the game is that agent A proposes the minimum possible and agent B will accept any offer, like this both amgents maximize their utility. This project aims at simulate the ultimatum game with artificial agents using python. The bheavior of the agents is not modelled but they learning using the q-algorithm (reinforcement learning).
For this project, 2 main modules are created and called from the Game notebook. In the players module the agents are defined as separate clases, in the ultumatum module the game is defined as a class. 

The required packages can be found in the txt file in the repository.



## Players 

Both players are defined as a separate class. Both players share some attributes and methods. However the q-table and its update is different according to each player. 


## Ultimatum 
 
The class ultimatum is defined. The attributes difine the number of episodes per simulation, the policy that agent B might follow and the dataframe to keep the record of results of each episode.

## Game (notebook)

Using the players and ultimatum classes defined above, several simulations of the game are run. Important focus is set on the optimal values for epsilon and alpha values in the methods of the artifitial agents. 
 