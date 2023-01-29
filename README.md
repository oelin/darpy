# darpy

A bug-fixed, refactored and repackaged version of [alice-st/DARP](https://github.com/oldworship/DARP-python). This is a user-friendly implementation of the DARP algorithm for multi-agent coverage path planning (MCPP).

```sh
pip install git+https://github.com/oelin/darpy
```


## Improved API

```py
from darpy import DARPCoordinate, DARPMap, DARPProblem


problem = DARPProblem(
	map = DARPMap(
		rows = 10,
		columns = 10,
	),
	agents = [
		DARPCoordinate(3, 3),
		DARPCoordinate(6, 0),
	],
	obstacles = [
		DARPCoordinate(6, 4),
		DARPCoordinate(5, 5),
		DARPCoordinate(5, 6),
		DARPCoordinate(5, 4),
	],
)


solved, solution = problem.solve()
```
