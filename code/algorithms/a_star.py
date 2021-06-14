"""
1. Path Function
2. Search Function:
- Define start node. in our case, random house 
- Define movement in term of relative position: possibilities are left, right and ahead
- Look for the lowest cost grid-line. Check:
    -Not on the 'already visited' list
    -If battery --> stop if yes 
- Create the new node with the parent as the current node and update the position of the node.
f(n): lowest cost in neighbouring node n
g(n): exact cost of the path from the starting node to any other no n
h(n): heuristic: estimated lowest cost from node n to goal node 
For every transition to another node, A* should calculate min(f(n) = g(n) + h(n)) 
"""

class Node():
#parent Node
#current position
#cost values
