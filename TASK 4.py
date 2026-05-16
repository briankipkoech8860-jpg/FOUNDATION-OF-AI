#kipkoech brian
#CIT-227-126/124
from collections import deque
# Define a well-labelled graph map
# A network of nodes and their connected neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_path(graph, start, goal):
    """
    Performs Breadth-First Search to find the shortest path.
    Uses a FIFO Queue.
    """
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            return path
            
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

def dfs_path(graph, start, goal):
    """
    Performs Depth-First Search to find a traversal path.
    Uses a LIFO Stack.
    """
    stack = [[start]]
    visited = set()
    
    while stack:
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            return path
            
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    return None

# --- Program Execution and Annotation ---
start_node = 'A'
goal_node = 'F'

print("--- AI SEARCH ALGORITHMS PATHS ---")
print(f"Starting Node: {start_node} | Goal Node: {goal_node}\n")

# Run BFS
bfs_result = bfs_path(graph, start_node, goal_node)
print(f"(i) Breadth-First Search (BFS) Path: {bfs_result}")

# Run DFS
dfs_result = dfs_path(graph, start_node, goal_node)
print(f"(ii) Depth-First Search (DFS) Path: {dfs_result}")
