#The purpose of this program is to intervene with the stream of actions sent by agent
#and insert a probability of 10% of replacing current action with a random one to explore the 
#environement more


import gym
import random as r


class RandomActionWrapper(gym.ActionWrapper):
    
    def __init__(self, env, epsilon = 0.1):
        super(RandomActionWrapper, self). __init__(env) #Uses parent's init method
        self.epsilon = epsilon #saves a probability of random action

    #Override parent's class method to tweak action to accept a random action   
    def action(self, action):
        if r.random() < self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
        return action

if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v1"))

    #Applying wrapper by creating normal CartPole environemnt and pass to wrapper constructor

    obs = env.reset()
    total_reward = 0.0

    while True:
        obs, reward, done, extra_info = env.step(0) #uses action of wrapper wehn calling step()
        total_reward += reward 
        if done:
            break
    
    print("Reward got: %.2f" %total_reward)

