import matplotlib.pyplot as plt

class GridWorld:
    def __init__(self, m, n, portals = {}):
        self.m, self.n = m, n

        self.portals = portals
        assert not (self.m - 1, self.n - 1) in self.portals.keys()

        # Actions
        self.transition = {
            'U' : (-1, 0),
            'D' : (1, 0),
            'L' : (0, -1),
            'R' : (0, 1)
        }

        self.action_space = list(self.transition.keys())

        self.agent_pos = (0, 0)
    
    def step(self, action):
        """
        Returns the new state, the reward and if the state is terminal
        Typically there's also a debug parameter return also
        """
        # Move
        self.agent_pos = ( 
            self.agent_pos[0] + self.transition[action][0], 
            self.agent_pos[1] + self.transition[action][1]
        )
        
        # Make sure we are within the boundaries
        self.agent_pos = (
            max(self.agent_pos[0], 0),
            max(self.agent_pos[1], 0)
        )

        self.agent_pos = (
            min(self.agent_pos[0], self.m - 1),
            min(self.agent_pos[1], self.n - 1)
        )

        self.agent_pos = self.portals.get(self.agent_pos, self.agent_pos)

        state_is_terminal = self.agent_pos[0] == self.m - 1 and self.agent_pos[1] == self.n - 1

        reward = 0 if state_is_terminal else -1

        return self.agent_pos, reward, state_is_terminal
    
    def render(self):
        pass

    def reset(self):
        self.agent_pos = (0, 0)

if __name__ == "__main__":
    from random import choice
    
    portals = {
        (1,1): (4,4)
    }

    env = GridWorld(5,5, portals)

    games = 10
    total_rewards = [0] * games

    for g in range(games):
        print(f"Game {g+1} starting...")
        done = False
        ret = 0
        obs = env.reset()

        while not done:        
            action = choice(env.action_space)

            obs, reward, done = env.step(action)

            ret += reward
            env.render(); input()

            #obs = obs_
        total_rewards[g] = ret
        print(f"Game {g+1} done...")


    plt.plot(total_rewards)
    plt.show()