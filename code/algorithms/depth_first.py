import copy

class Depth_first:
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)

    def run(self):
        depth = 3
        stack = [""]

        while len(stack) > 0:
            state = stack.pop()
            print(state)

            if len(state) < depth:
                house_id = len(state)
                # (house_id, battery_id)
                # possible_states = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
                possible_states = list()

                for i in range(len(self.grid.batteries)):
                    possible_states.append((house_id, i))

                for i in possible_states:
                    child = copy.deepcopy(state)
                    child += i
                    stack.append(child)


# L - [(0, 0)]
# LL - [(0, 0), (1, 0)]
# LLL - [(0, 0), (1, 0), (2, 0)]
# LLR
# LR
# LRL
# LRR
# R
# RL
# RLL
# RLR
# RR
# RRL
# RRR
