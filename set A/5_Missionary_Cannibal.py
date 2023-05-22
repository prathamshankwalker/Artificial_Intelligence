# implement missionaries and cannibals problem using dfs# Write a program to implement Missionary & Cannibal problem using DFS

class State:
    def __init__(self,missionary,cannibal,boat,parent=None):
        self.missionary = missionary     # Number of missionaries on the left bank
        self.cannibal = cannibal         # Number of cannibals on the left bank
        self.boat = boat                 # 0 if boat is on left bank, 1 if boat is on right bank
        self.parent = parent             # Parent state

    def is_valid(self):
        # Check if the number of missionaries is greater than or equal to the number of cannibals on either bank
        if self.missionary < self.cannibal and self.missionary > 0:
            return False
        
        # Check if the number of missionaries is greater than or equal to zero
        if self.missionary < 0 or self.missionary > 3:
            return False
        
        # Check if the number of cannibals is greater than or equal to zero
        if self.cannibal < 0 or self.cannibal > 3:
            return False
        return True

    def is_goal(self):
        return self.missionary == 0 and self.cannibal == 0 and self.boat == 1
    
    def __eq__(self, other):
        return self.missionary == other.missionary and self.cannibal == other.cannibal and self.boat == other.boat
    
    def __hash__(self):
        return hash((self.missionary, self.cannibal, self.boat))
    
    def __str__(self):
        return f"({self.missionary}, {self.cannibal}, {self.boat})"
    

def successors(state):
    children = set()
    if state.boat == 0:
        # Boat is on left bank
        for i in range(3):
            for j in range(3):
                if i + j >= 1 and i + j <= 2:
                    new_state = State(state.missionary - i, state.cannibal - j, 1, state)
                    if new_state.is_valid():
                        children.add(new_state)
    else:
        # Boat is on right bank
        for i in range(3):
            for j in range(3):
                if i + j >= 1 and i + j <= 2:
                    new_state = State(state.missionary + i, state.cannibal + j, 0, state)
                    if new_state.is_valid():
                        children.add(new_state)
    return children


def dfs(initial_state):
    stack = [initial_state]
    visited = set()
    while stack:
        state = stack.pop()
        if state.is_goal():
            path = []
            while state.parent:
                path.append(state)
                state = state.parent
            path.append(state)
            return list(reversed(path))
        visited.add(state)
        for child in successors(state):
            if child not in visited:
                stack.append(child)
    return None

def RHSside(state):
    return f"({3 - state.missionary}, {3 - state.cannibal}, {state.boat})"

initial_state = State(3, 3, 0)
path = dfs(initial_state)
if path:
    print("   LHS         ||           RHS      ")
    print("_____________________________________")
    for i, state in enumerate(path):
        print(f"{state}      ||        {RHSside(state)}")
    print("_____________________________________")
else:
    print("No solution found.")