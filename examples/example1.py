from darpy import *


problem = DARPProblem(
	map=DARPMap(rows=10, columns=10), 
	agents=[DARPCoordinate(x=1, y=1), DARPCoordinate(x=6, y=5)], 
	obstacles=[],
)


solved, solution = problem.solve()

print(f'solved: {solved}')
print(solution.astype(int))
