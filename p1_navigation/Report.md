[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

# Project 1: Navigation

### Introduction

For this project, you will train an agent to navigate (and collect bananas!) in a large, square world.  

![Trained Agent][image1]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

### Implementation

Neural Network Architecture:
-  2 fully connected 'RELU' activation layers

Reinforcement learning training parameters:
- BUFFER_SIZE = int(1e5)
- BATCH_SIZE = 64        
- GAMMA = 0.99         
- TAU = 1e-3            
- Learning Rate = 5e-4    
- Maximum episodes = 2000
- Maximum steps per episode = 1000
- eps_start = 1.0
- eps_end = 0.01
- eps_decay = 0.925

### Results

![Graph of results](images/navigation_results_graphs.png)

![Navigation Results](images/navigation_results.png)

As shown above, the agent solved the environment in 498 episodes.

### Instructions
