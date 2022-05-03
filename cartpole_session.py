import gym
import pygame


if __name__ == "__main__":
    e = gym.make("CartPole-v1")

    obs = e.reset() #reset the enviornment and obtain first observation (just 4 numbers)
    print(obs) #prints out the observation array

    print(e.action_space) #our actions are just 0 or 1, 0 means to left and 1 is to the right
    print(e.observation_space) #observation space of size four with values -inf to inf interval

    e.reset() #calls reset for next line that checks a step
    print(e.step(0)) #new observation with vector of 4 numbers, reward of 1, episode not over, empty extra info
    print(e.action_space.sample()) #returns random sample
    print(e.action_space.sample())
    print(e.observation_space.sample()) #random vector
