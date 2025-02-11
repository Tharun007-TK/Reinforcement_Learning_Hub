# Evaluation after training
num_test_episodes = 1000
wins, losses, draws = 0, 0, 0

def greedy_policy(state):
    """Returns the best action based on learned Q-values."""
    return np.argmax(q_table[state]) if state in q_table else env.action_space.sample()

for _ in range(num_test_episodes):
    state, _ = env.reset()
    done = False

    while not done:
        action = greedy_policy(state)  # Use the learned policy (greedy selection)
        next_state, reward, done, _, _ = env.step(action)
        state = next_state  # Move to the next state

    # Track performance
    if reward == 1:
        wins += 1
    elif reward == 0:
        draws += 1
    else:
        losses += 1

# Display performance results
print(f"Win rate: {wins/num_test_episodes*100:.2f}%, Draw rate: {draws/num_test_episodes*100:.2f}%, Loss rate: {losses/num_test_episodes*100:.2f}%")

#Training complete! Learned Q-values for Blackjack.
#Win rate: 37.10%, Draw rate: 4.70%, Loss rate: 58.20%
