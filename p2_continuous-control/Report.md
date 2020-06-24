[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/43851024-320ba930-9aff-11e8-8493-ee547c6af349.gif "Trained Agent"

# Project 2: Continuous Control

### Project description:

For this project, you will train an agent to interact in the Reacher environment.  

![Trained Agent][image1]

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.


### Implementation:

Neural Network Architecture:
-  Convolutional neural network with multiple 'RELU' activation layers and an included BatchNorm1d layer.

Reinforcement learning training parameters:
- BUFFER_SIZE = int(1e6)
- BATCH_SIZE = 1024
- GAMMA = 0.99
- TAU = 1e-3
- LR_ACTOR = 1e-4
- LR_CRITIC = 3e-4
- LEAKINESS = 0.01
-  WEIGHT_DECAY = 0.0001

### Results:

I ran this program many times and the Udacity workspace always would disconnect. In the included solution, the agent was about to solve the environment but Udacity disconnected.

The agents likely would have solved the environment in less than 300 episodes.

### Possible Future Additions:
- Tune Hyperparameters
- Improved Actor-Critic Models
- Improve replay buffer
