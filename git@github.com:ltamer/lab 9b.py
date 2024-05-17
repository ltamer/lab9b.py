import random

#note: update out_path to point to somewhere on your computer
params = {'world_size':(20,20),
          'num_agents':380,
          'same_pref' :0.4,
          'max_iter'  :100,
          'out_path'  :r'/Users/laratamer/Documents/GitHub/simple_abm/lab9b.py/git@github.com/ltamer/lab 9b.py'}

class Agent:
    def __init__(self, world):
        self.world = world
        self.location = None

    def find_empty_patch(self):
        # Get all empty locations
        empty_locations = [loc for loc, occupant in self.world.grid.items() if occupant is None]
        if empty_locations:
            return random.choice(empty_locations)
        return None

    def move_to_empty_patch(self):
        new_location = self.find_empty_patch()
        if new_location:
            # Move to new location
            self.world.grid[self.location] = None
            self.world.grid[new_location] = self
            self.location = new_location

class World:
    def __init__(self, params):
        size = params['world_size']
        self.grid = {(i, j): None for i in range(size[0]) for j in range(size[1])}
        self.agents = [Agent(self) for _ in range(params['num_agents'])]
        self.initialize_agents()

    def initialize_agents(self):
        # Randomly place agents in the world
        locations = list(self.grid.keys())
        random.shuffle(locations)
        for agent in self.agents:
            location = locations.pop()
            self.grid[location] = agent
            agent.location = location

    def run_simulation(self):
        for _ in range(params['max_iter']):
            for agent in self.agents:
                agent.move_to_empty_patch()

# Initialize the world with parameters
world = World(params)
world.run_simulation()

# Print final agent locations
for location, agent in world.grid.items():
    if agent is not None:
        print(f"Agent at location {location}")
