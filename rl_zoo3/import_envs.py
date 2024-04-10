from typing import Callable, Optional

import gymnasium as gym
from gymnasium.envs.registration import register

from rl_zoo3.wrappers import MaskVelocityWrapper

try:
    import pybullet_envs_gymnasium
except ImportError:
    pass

try:
    import highway_env
except ImportError:
    pass
else:
    # hotfix for highway_env
    import numpy as np

    np.float = np.float32  # type: ignore[attr-defined]

try:
    import custom_envs
except ImportError:
    pass

try:
    import gym_donkeycar
except ImportError:
    pass

try:
    import panda_gym
except ImportError:
    pass

try:
    import rocket_lander_gym
except ImportError:
    pass

try:
    import minigrid
except ImportError:
    pass


# Register no vel envs
def create_no_vel_env(env_id: str) -> Callable[[Optional[str]], gym.Env]:
    def make_env(render_mode: Optional[str] = None) -> gym.Env:
        env = gym.make(env_id, render_mode=render_mode)
        env = MaskVelocityWrapper(env)
        return env

    return make_env


for env_id in MaskVelocityWrapper.velocity_indices.keys():
    name, version = env_id.split("-v")
    register(
        id=f"{name}NoVel-v{version}",
        entry_point=create_no_vel_env(env_id),  # type: ignore[arg-type]
    )
# Attempt to import the SinglePlayerEnvironment class to ensure it exists
try:
    # This import is just to check if haxballgym is installed and SinglePlayerEnvironment is accessible
    from haxballgym import SinglePlayerEnvironment
    haxballgym_installed = True
except ImportError:
    print("haxballgym is not installed.")
    haxballgym_installed = False

if haxballgym_installed:
    print('Keep going brotha')
    # Register the environment using a string-based entry_point
    register(
        id='SinglePlayerHaxball-v0',  # Unique identifier for the environment
        entry_point='haxballgym:SinglePlayerEnvironment',  # Adjusted entry point
    )

    # Example on how to create and use the environment
    try:
        env = gym.make('SinglePlayerHaxball-v0')
        print("Environment created successfully. You can now use it!")
    except gym.error.UnregisteredEnv:
        print("Environment is not registered. Ensure registration code is executed.")