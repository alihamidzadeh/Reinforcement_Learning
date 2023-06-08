import gym
import time

env = gym.make("FrozenLake-v1", render_mode="human", is_slippery=False)
env.reset()

# print(env.render())
# time.sleep(5)
# print(env.observation_space)
# print(env.P)

# 0: LEFT
# 1: DOWN
# 2: RIGHT
# 3: UP

while True:
    # action = env.action_space.sample()
    action = int(input("Enter: "))
    next_state, reward, done, trunc, info = env.step(action)
    env.render()
    print(next_state, reward, done, trunc, info)
    if done:
        env.reset()
