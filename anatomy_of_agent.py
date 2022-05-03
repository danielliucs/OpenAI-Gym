#Purpose of code listed in description of this commit

import random as r #random rewards for a limited number of steps regardless of agent's actions


class Environment: #Defined environment
    def __init__(self): 
        self.steps_left = 10 #Initialize internal state, counter that limits the number of steps agent can take to interact with environment

    def get_observation(self): #return the current environment's observation to the agent
        return [0.0, 0.0, 0.0]

    def get_actions(self): #what agent queries for set of actions it can execute, only two in this case encoded in 0 and 1
        return [0, 1]

    def is_done(self): #ends the episode (observation of state) to the agent
        return self.steps_left == 0

    def action(self, action): #central piece of environment functionality, handles agent's actions and returns reward for action
        if self.is_done():
            raise Exception("Game is over") #refuse to continue episodes that are over
        self.steps_left -= 1 #updating number of steps, self.steps_left = self.steps_left-1
        return r.random() #generate random number


class Agent: #Defined Agent
    def __init__(self): #constructor with a counter that keeps total award accumulated
        self.total_reward = 0.0

    def step(self, env): #accepts environment instance and performs one step in environment
        current_obs = env.get_observation() #get observations from environement (ignores observations)
        actions = env.get_actions() #holds action list (vector) returned, make decision about action to take based on observations (random since observations is 0)
        reward = env.action(r.choice(actions)) #select random choice returned list (vector), submit action to environment 
        self.total_reward += reward #accumulate total award


#creates two objects of their respective classes, runs one episode
if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)
