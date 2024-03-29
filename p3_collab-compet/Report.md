[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135623-e770e354-7d12-11e8-998d-29fc74429ca2.gif "Trained Agent"

# Project 3: Collaboration and Competition

### Project description:

For this project, you will work with the [Tennis](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#tennis) environment.

In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1.  If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01.  Thus, the goal of each agent is to keep the ball in play.

The observation space consists of 8 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation.  Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping.

The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents). Specifically,

- After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 2 (potentially different) scores. We then take the maximum of these 2 scores.
- This yields a single **score** for each episode.

The environment is considered solved, when the average (over 100 episodes) of those **scores** is at least +0.5.

### Implementation:

Neural Network Architecture:
-  DDPG reinforcement model with actors and critics built with feed forward  neural networks.

Reinforcement learning training parameters:

BUFFER_SIZE = int(1e6)
BATCH_SIZE = 1024        
GAMMA = 0.99            
TAU = 1e-3              
LR_ACTOR = 1e-4        
LR_CRITIC = 1e-3        
WEIGHT_DECAY = 0       

### Results:

The agent was able to solve the environment fairly quickly in only 979 episodes. The scores at each episode are graphed below

![results](images/result.jpg)

### Possible Future Additions:
- Tune Hyperparameters
- Improved Actor-Critic Models
- Improve replay buffer
