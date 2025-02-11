# Evaluation after training
num_test_episodes = 1000
wins, losses, draws = 0, 0, 0

for _ in range(num_test_episodes):
    state, _ = env.reset()
    done = False

    while not done:
        action = np.argmax(q_table[state]) if state in q_table else env.action_space.sample()
        state, reward, done, _, _ = env.step(action)

    if reward == 1:
        wins += 1
    elif reward == 0:
        draws += 1
    else:
        losses += 1

print(f"Win rate: {wins/num_test_episodes*100:.2f}%, Draw rate: {draws/num_test_episodes*100:.2f}%, Loss rate: {losses/num_test_episodes*100:.2f}%")


#Training complete! Learned Q-values for Blackjack.
#Win rate: 43.70%, Draw rate: 8.40%, Loss rate: 47.90% 
