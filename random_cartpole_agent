import gym


if __name__ == "__main__":
    env = gym.make("CartPole-v1") #creates environment
    #counters for number of steps and awards
    total_reward = 0.0 
    total_steps = 0
    #always have to reset on first observation, not used since agent is stochastic
    obs = env.reset()

    while True:
        action = env.action_space.sample() #sample random item from action space
        obs, reward, done, extra_info = env.step(action) #returned next observation, local reward, episode done flag, and extra_info abt env
        total_reward += reward #accumulate total award
        total_steps += 1 #count number if steps
        if done: #if end of episode
            break
    
    print("Episode done in %d steps, total reward is %.2f" % (total_steps, total_reward))
