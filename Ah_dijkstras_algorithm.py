import sys

nodes = [[1, 1, 0, 0],
            [1, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 0]]
edges =  [[0, 6, 9, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 5],
          [0, 0, 0, 0]]

num = len(nodes[0])

visited_plus_cost = [[0, 0]]
for _ in range(num-1):
  visited_plus_cost.append([0, sys.maxsize])

for _ in range(num):
  node = -1
  for x in range(num):
    if visited_plus_cost[x][0] == 0 and (node < 0 or visited_plus_cost[x][1] <= visited_plus_cost[node][1]):
        node = x
  next_visit = node
  for y in range(num):
    if nodes[next_visit][y] == 1 and visited_plus_cost[y][0] == 0:
      changed_cost = visited_plus_cost[next_visit][1] + edges[next_visit][y]
      if visited_plus_cost[y][1] > changed_cost:
        visited_plus_cost[y][1] = changed_cost
    visited_plus_cost[next_visit][0] = 1

vertices = ['A', 'B', 'C', 'D']
print("Shortest Paths:")
for x, cost in enumerate(visited_plus_cost):
  print(f"\tFrom A to {vertices[x]}: ",cost[1])
