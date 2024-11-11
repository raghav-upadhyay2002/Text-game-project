import random
from textworld_express import TextWorldExpressEnv

env = TextWorldExpressEnv(envStepLimit=100)


env.load(gameName="cookingworld", gameParams="numIngredients=3,numLocations=2,includeDoors=1,limitInventorySize=5")

# Test run: Generate and play 10 episodes
for episode_id in range(10):
    obs, infos = env.reset(seed=episode_id, gameFold="train", generateGoldPath=True)
    print(f"Episode {episode_id + 1} start:")
    print(obs)

    for step_id in range(50):
        # Select a random valid action
        validActions = sorted(infos['validActions'])
        if validActions:
            randomAction = random.choice(validActions)
            obs, reward, done, infos = env.step(randomAction)
            print(">", randomAction)
            print(obs)
            if done:
                print("Task complete!")
                break
        else:
            print("No valid actions available.")
            break
    print("-" * 30)