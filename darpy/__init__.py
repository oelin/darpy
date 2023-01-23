from typing import List
from dataclasses import dataclass
import numpy as np

from . import darp


@dataclass
class DARPMap:

    rows: int = 10
    columns: int = 10


@dataclass
class DARPCoordinate:

    x: int = 0
    y: int = 0


    def to_index(self, map: DARPMap):
        return self.y * map.rows + self.x


@dataclass
class DARPProblem:

    map: DARPMap
    agents: List[DARPCoordinate]
    obstacles: List[DARPCoordinate]


    def solve(self, iterations: int = 5000):

        # Compute agent and obstacle indices...

        agent_indices = [agent.to_index(self.map) for agent in self.agents]
        obstacle_indices = [obstacle.to_index(self.map) for obstacle in self.obstacles]


        # Compute even portions...

        portions = np.ones(len(self.agents)) / len(self.agents)


        # Solve the problem...

        solver = darp.DARP(
                nx=self.map.columns,
                ny=self.map.rows,
                notEqualPortions=False,
                given_initial_positions=agent_indices,
                given_portions=portions,
                obstacles_positions=obstacle_indices,
                visualization=False,
                MaxIter=iterations,
        )
        
        try:
            self.solved,_ = solver.divideRegions()
            self.solution = solver.BinaryRobotRegions
            
            return self.solved, self.solution
        
        except:
            return False, None
