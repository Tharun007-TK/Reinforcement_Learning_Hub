import gymnasium as gym
import numpy as np

# Create the FrozenLake environment
env = gym.make("FrozenLake-v1", is_slippery=False, render_mode="human")

# Define parameters
num_states = env.observation_space.n
num_actions = env.action_space.n
q_table = np.zeros((num_states, num_actions))

# Hyperparameters
alpha = 0.1
gamma = 0.9
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 2000  # Increased number of episodes

# Training loop
for episode in range(episodes):
    state, _ = env.reset()
    done = False

    while not done:
        # Choose action using epsilon-greedy policy
        if np.random.rand() < epsilon:
            action = env.action_space.sample()  # Explore
        else:
            action = np.argmax(q_table[state, :])  # Exploit

        # Take action, observe reward and next state
        next_state, reward, done, _, _ = env.step(action)

        # Reward shaping: Encourage shorter paths, but don't modify goal rewards
        if not done and reward == 0:
            reward = -0.01  # Small penalty for taking extra steps

        # Q-learning update formula
        q_table[state, action] += alpha * (
            reward + gamma * np.max(q_table[next_state, :]) - q_table[state, action]
        )

        # Move to next state
        state = next_state

    # Decay epsilon (reduce exploration)
    epsilon = max(min_epsilon, epsilon * epsilon_decay)

print("Training finished!")

# Testing the trained agent
state, _ = env.reset()
done = False

print("\nAgent's test run:")

while not done:
    action = np.argmax(q_table[state, :])  # Select best learned action
    next_state, reward, done, _, _ = env.step(action)

    env.render()  # Render environment
    state = next_state

env.close()
