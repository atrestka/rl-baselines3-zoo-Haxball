import gymnasium as gym
try:
    env = gym.make('highway_env')  # Adjust the ID as needed
    print("Environment created successfully.")
except gym.error.UnregisteredEnv:
    print("Environment is not registered.")