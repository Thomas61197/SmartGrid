"""
1. Path Function
2. Search Function:
- Define start node. in our case, random house 
- Define movement in term of relative position: possibilities are left, right and ahead
- Look for the lowest cost grid-line. Check:
    -Not on the 'already visited' list
    -If battery --> stop if yes 
- Create the new node with the parent as the current node and update the position of the node.
"""

Class Node():
    