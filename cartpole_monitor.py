import gym

#Run in no env

if __name__ == "__main__":
    env = gym.make("CartPole-v1")
    #env = gym.wrappers.Monitor(env, "recording")

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        env.render() #plays a video of cartpole falling/being balanced
        if done:
            break
            
    print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))
    env.close()
    env.env.close()
