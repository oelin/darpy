# MIT License

# Copyright (c) 2023 Oelin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
