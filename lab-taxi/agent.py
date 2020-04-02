import numpy as np
from collections import defaultdict
import random

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))

    def select_action(self, state, eps):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
#         return np.random.choice(self.nA)
        if random.random() > eps: # select greedy action with probability epsilon
            return np.argmax(self.Q[state])
        else:                     # otherwise, select an action randomly
            return random.choice(np.arange(self.nA))

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
#         self.Q[state][action] += 1
        old_Q = self.Q[state][action]
        Q_next_len = len(self.Q[next_state])
        Q_next = max(self.Q[next_state]) if next_state is not None else 0
        Q_next = Q_next/Q_next_len
        self.Q[state][action] = old_Q + (0.9*((reward + (1*Q_next)) - old_Q))
        return self.Q[state][action]
