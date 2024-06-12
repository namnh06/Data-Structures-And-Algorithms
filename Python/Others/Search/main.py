from abc import ABC, abstractmethod
import heapq
from typing import List, Tuple, Dict, Optional

# Strategy Design Pattern
class Strategy(ABC):
    @abstractmethod
    def search(self, maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        pass

class DepthFirstSearch(Strategy):
    def search(self, maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        # Validate input to ensure start and goal positions are within the maze boundaries and not blocked
        if not is_valid_input(maze, start, goal):
            return None
        
        # Initialize a stack to manage the cells to explore, starting with the start position
        stack: Stack = Stack()
        stack.push(start)
        
        # Dictionary to keep track of the predecessors of each cell for path reconstruction
        predecessors: Dict[Tuple[int, int], Tuple[int, int]] = {start: None}

        # Continue exploring while there are cells in the stack
        while not stack.is_empty():
            current_cell: Tuple[int, int] = stack.pop()
            
            # If the goal is reached, reconstruct and return the path
            if current_cell == goal:
                return get_path(predecessors, start, goal)
            
            # Explore the neighboring cells in a clockwise direction
            for direction in directions:
                row_offset, col_offset = direction
                neighbour: Tuple[int, int] = (current_cell[0] + row_offset, current_cell[1] + col_offset)
                
                # If the neighboring cell is valid and not visited, add it to the stack
                if is_valid_pos(maze, neighbour) and neighbour not in predecessors:
                    stack.push(neighbour)
                    predecessors[neighbour] = current_cell
        
        # Return None if no path is found
        return None

class BreadthFirstSearch(Strategy):
    def search(self, maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        # Validate input to ensure start and goal positions are within the maze boundaries and not blocked
        if not is_valid_input(maze, start, goal):
            return None
        
        # Initialize a queue to manage the cells to explore, starting with the start position
        queue: Queue = Queue()
        queue.enqueue(start)
        
        # Dictionary to keep track of the predecessors of each cell for path reconstruction
        predecessors: Dict[Tuple[int, int], Tuple[int, int]] = {start: None}

        # Continue exploring while there are cells in the queue
        while not queue.is_empty():
            current_cell: Tuple[int, int] = queue.dequeue()
            
            # If the goal is reached, reconstruct and return the path
            if current_cell == goal:
                return get_path(predecessors, start, goal)
            
            # Explore the neighboring cells in a clockwise direction
            for direction in directions:
                row_offset, col_offset = direction
                neighbour: Tuple[int, int] = (current_cell[0] + row_offset, current_cell[1] + col_offset)
                
                # If the neighboring cell is valid and not visited, add it to the queue
                if is_valid_pos(maze, neighbour) and neighbour not in predecessors:
                    queue.enqueue(neighbour)
                    predecessors[neighbour] = current_cell
        
        # Return None if no path is found
        return None

class AStarSearch(Strategy):
    def search(self, maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        # Validate input to ensure start and goal positions are within the maze boundaries and not blocked
        if not is_valid_input(maze, start, goal):
            return None
        
        # Initialize a priority queue to manage the cells to explore, starting with the start position
        pq: PriorityQueue = PriorityQueue()
        pq.put(start, 0)
        
        # Dictionary to keep track of the predecessors of each cell for path reconstruction
        predecessors: Dict[Tuple[int, int], Tuple[int, int]] = {start: None}
        
        # Dictionary to store the cost from the start to each cell
        g_values: Dict[Tuple[int, int], int] = {start: 0}

        # Continue exploring while there are cells in the priority queue
        while not pq.is_empty():
            current_cell: Tuple[int, int] = pq.get()
            
            # If the goal is reached, reconstruct and return the path
            if current_cell == goal:
                return get_path(predecessors, start, goal)
            
            # Explore the neighboring cells in a clockwise direction
            for direction in directions:
                row_offset, col_offset = direction
                neighbour: Tuple[int, int] = (current_cell[0] + row_offset, current_cell[1] + col_offset)
                
                # If the neighboring cell is valid, calculate the cost and update the priority queue
                if is_valid_pos(maze, neighbour):
                    new_cost: int = g_values[current_cell] + 1
                    if neighbour not in g_values or new_cost < g_values[neighbour]:
                        g_values[neighbour] = new_cost
                        f_value: int = new_cost + heuristic(goal, neighbour)
                        pq.put(neighbour, f_value)
                        predecessors[neighbour] = current_cell
        
        # Return None if no path is found
        return None

# Stack (LIFO) class for Depth-First Search (DFS)
class Stack:
    def __init__(self) -> None:
        self.items: List[Tuple[int, int]] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: Tuple[int, int]) -> None:
        self.items.append(item)

    def pop(self) -> Tuple[int, int]:
        return self.items.pop()

# Queue (FIFO) class for Breadth-First Search (BFS)
class Queue:
    def __init__(self) -> None:
        self.items: List[Tuple[int, int]] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item: Tuple[int, int]) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> Tuple[int, int]:
        return self.items.pop()

# PriorityQueue class for A* Search
class PriorityQueue:
    def __init__(self) -> None:
        self.elements: List[Tuple[int, Tuple[int, int]]] = []

    def is_empty(self) -> bool:
        return not self.elements

    def put(self, item: Tuple[int, int], priority: int) -> None:
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Tuple[int, int]:
        return heapq.heappop(self.elements)[1]

# Direction offsets for movement
directions: List[Tuple[int, int]] = [
    (-1, 0), # move up
    (0, 1),  # move right
    (1, 0),  # move down
    (0, -1)  # move left
]

# Function to check if the position is within the columns of the maze
def is_in_columns(num_cols: int, j: int) -> bool:
    return 0 <= j < num_cols

# Function to check if the position is within the rows of the maze
def is_in_rows(num_rows: int, i: int) -> bool:
    return 0 <= i < num_rows

# Function to check if the position is not a block
def is_block(maze: List[List[int]], i: int, j: int) -> bool:
    return maze[i][j] != "*"

# Heuristic function for A* search
# Calculate the Manhattan distance between two points goal and neighbour
def heuristic(goal: Tuple[int, int], neighbour: Tuple[int, int]) -> int:
    x1, y1 = goal
    x2, y2 = neighbour
    return abs(x1 - x2) + abs(y1 - y2)

# Function to check if the input (start and goal) is valid within the maze
def is_valid_input(maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> bool:
    return is_valid_pos(maze, start) and is_valid_pos(maze, goal)

# Function to check if the position is valid within the maze
def is_valid_pos(maze: List[List[int]], pos: Tuple[int, int]) -> bool:
    i, j = pos
    num_rows: int = len(maze)
    num_cols: int = len(maze[0])
    return is_in_rows(num_rows, i) and is_in_columns(num_cols, j) and is_block(maze, i, j)

# Function to reconstruct the path from start to goal using predecessors
def get_path(predecessors: Dict[Tuple[int, int], Tuple[int, int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    # Start from the goal and initialize an empty path
    current: Tuple[int, int] = goal
    path: List[Tuple[int, int]] = []
    
    # Trace back from the goal to the start using the predecessors dictionary
    while current != start:
        path.append(current)
        current = predecessors[current]
        
    path.append(start)
    # Reverse the path to get it from start to goal
    path.reverse()
    return path

# Function to create a test maze
def create_maze(size: int) -> List[List[int]]:
    if size < 2:
        raise ValueError("Maze size must be at least 2x2")
    return [[0] * size for _ in range(size)]

# Context class to use different strategies
class MazeSolver:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def solve(self, maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        return self._strategy.search(maze, start, goal)

if __name__ == "__main__":
    
    # Test for is_in_columns
    assert is_in_columns(3, 2) == True
    assert is_in_columns(3, -1) == False

    # Test for is_in_rows
    assert is_in_rows(3, 2) == True
    assert is_in_rows(3, -1) == False

    # Test for is_block
    assert is_block([[0, 0, 0], [0, '*', 0], [0, 0, 0]], 1, 1) == False
    assert is_block([[0, 0, 0], [0, '*', 0], [0, 0, 0]], 0, 0) == True

    # Test for heuristic
    assert heuristic((0, 0), (1, 1)) == 2
    assert heuristic((1, 1), (4, 5)) == 7

    maze = create_maze(3)
    """
    | A | B | C |
    | D | E | F |
    | G | H | I |
    """
    # Test for is_valid_input
    assert is_valid_input(maze, (0, 0), (2, 2)) == True
    assert is_valid_input(maze, (3, 3), (2, 2)) == False
    assert is_valid_input(maze, (0, 0), (-1, 0)) == False
    
    # Test for is_valid_pos
    assert is_valid_pos(maze, (0, 0)) == True
    assert is_valid_pos(maze, (-1, 0)) == False
    
    # Test for get_path
    predecessors: Dict[Tuple[int, int], Tuple[int, int]] = {
        (2, 2): (2, 1),
        (2, 1): (2, 0),
        (2, 0): (1, 0),
        (1, 0): (0, 0)
    }
    start = (0, 0)
    goal = (2, 2)
    assert get_path(predecessors, start, goal) == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test for DepthFirstSearch
    dfs = DepthFirstSearch()
    solver = MazeSolver(dfs)
    path_dfs = solver.solve(maze, start, goal)
    print(f'DFS Path: {path_dfs}')
    assert path_dfs == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

    # Test for BreadthFirstSearch
    bfs = BreadthFirstSearch()
    solver.set_strategy(bfs)
    path_bfs = solver.solve(maze, start, goal)
    print(f'BFS Path: {path_bfs}')
    assert path_bfs == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test for AStarSearch
    astar = AStarSearch()
    solver.set_strategy(astar)
    path_astar = solver.solve(maze, start, goal)
    print(f'A* Path: {path_astar}')
    assert path_astar == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    
    # Add obstacles to the maze
    maze_with_block = create_maze(3)
    maze_with_block[1][0] = '*'
    """
    | A | B | C |
    | * | E | F |
    | G | H | I |
    """
    
    # Test for DepthFirstSearch with a block
    dfs = DepthFirstSearch()
    solver = MazeSolver(dfs)
    path_dfs = solver.solve(maze_with_block, start, goal)
    print(f'DFS Path: {path_dfs}')
    assert path_dfs == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    
    # Test for BreadthFirstSearch with blocks
    maze_with_block[0][2] = '*'
    """
    | A | B | * |
    | * | E | F |
    | G | H | I |
    """
    bfs = BreadthFirstSearch()
    solver.set_strategy(bfs)
    path_bfs = solver.solve(maze_with_block, start, goal)
    print(f'BFS Path: {path_bfs}')
    assert path_bfs == [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]

    # Test for AStarSearch with a block
    maze_with_block[0][2] = 0
    maze_with_block[1][0] = 0
    maze_with_block[1][2] = '*'
    """
    | A | B | C |
    | D | E | * |
    | G | H | I |
    """
    astar = AStarSearch()
    solver.set_strategy(astar)
    path_astar = solver.solve(maze_with_block, start, goal)
    print(f'A* Path: {path_astar}')
    assert path_astar == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]