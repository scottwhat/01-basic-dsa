from collections import deque

def best_bridge(grid):
  
  #initial DFS to find first island 
  main_island = None
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      potential_island = traverse_island(grid, r, c, set())
      if potential_island:
        main_island = potential_island
  
  #seeded set with the main island pos, already in there so they dont get revisited 
  visited = set(main_island)
  queue = deque([ ])
  
  #simultaneous BFSabout to commence, all levels get processed
  #these fan out like a drop of ink in water
  #whole level 0 processed, all neighbors appended
  #next whole level processed, if valid it continues 
  
  for pos in main_island:
    r, c = pos
    queue.append((r, c, 0))
  
  
  #continue decipher 
  #bfs HERE 
  
  while queue:
    #typical BFS
    #BFS approach, what to do
    #get the info from the popped queue
    #if its the target return it, so if L and no in main_island 
    
    
    row, col, distance = queue.popleft()
    if grid[row][col] == 'L' and (row, col) not in main_island:    
      return distance - 1
    
    #use deltas for calculating position changes in matrix BFS
    #list out the nums, then loop over each 1 
    #get new row and colum calculated
    #make a new pos 
    #check if inbounds, pass in grid, new row + col and the current is not in visited: 
    #queue.append(row, col, distance )
    #visited.add(neighbor_pos)
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col
      neighbor_pos = (neighbor_row, neighbor_col)
      if inbounds(grid, neighbor_row, neighbor_col) and neighbor_pos not in visited:
        visited.add(neighbor_pos)
        queue.append((neighbor_row, neighbor_col, distance + 1))
  
def inbounds(grid, row, col):
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= col < len(grid[0])
  return row_inbounds and col_inbounds


#DFS - completed 
  
def traverse_island(grid, row, col, visited):
  if not inbounds(grid, row, col) or grid[row][col] == 'W':
    return visited
  
  pos = (row, col)
  if pos in visited:
    return visited
  
  visited.add(pos)
  
  traverse_island(grid, row - 1, col, visited)
  traverse_island(grid, row + 1, col, visited)
  traverse_island(grid, row, col - 1, visited)
  traverse_island(grid, row, col + 1, visited)
  return visited