class Day3:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day3(cls, part):

        path = 'Inputs/input3.txt'
        val = int(open(path, 'r').read())
        if part == 1:
            east = 0
            north = 1
            west = 2
            south = 3

            direction = 0

            max_steps = 1
            steps = 0
            direction_changes = 0

            x, y = 0, 0

            for i in range(1, val):
                if direction == east:
                    x = x + 1
                if direction == north:
                    y = y + 1
                if direction == west:
                    x = x - 1
                if direction == south:
                    y = y - 1

                steps += 1

                if steps == max_steps:
                    direction_changes = direction_changes + 1
                    direction = (direction + 1) % 4
                    steps = 0
                    if direction_changes % 2 == 0:
                        max_steps += 1

            return str(abs(x) + abs(y))
        if part == 2:

            import numpy as np
            import matplotlib.pyplot as plt

            east = 0
            north = 1
            west = 2
            south = 3

            direction = 0
            max_steps = 1
            steps = 0
            direction_changes = 0
            n = 12

            spiral = np.zeros((n, n), int)

            y = int(n / 2)
            x = int(n / 2) + 1
            spiral[y][x - 1] = 1

            while x <= n and y <= n:
                spiral[y][x] += (spiral[y - 1][x - 1] if y > 0 and x > 0 else 0) + (
                    spiral[y - 1][x] if y > 0 else 0) + (
                                    spiral[y - 1][x + 1] if y > 0 and x < n else 0)
                spiral[y][x] += (spiral[y][x - 1] if x > 0 else 0) + (spiral[y][x + 1] if x < n else 0)
                spiral[y][x] += (spiral[y + 1][x - 1] if y < n and x > 0 else 0) + (
                    spiral[y + 1][x] if y < n else 0) + (
                                    spiral[y + 1][x + 1] if y < n and x < n else 0)

                if spiral[y][x] > val:
                    print(spiral[y][x])
                    break

                steps = steps + 1
                if steps == max_steps:
                    direction_changes = direction_changes + 1
                    direction = (direction + 1) % 4
                    steps = 0
                    if direction_changes % 2 == 0:
                        max_steps += 1
                if direction == east:
                    x = x + 1
                if direction == north:
                    y = y + 1
                if direction == west:
                    x = x - 1
                if direction == south:
                    y = y - 1

            matrix = np.matrix(spiral)
            plt.imshow(matrix, interpolation='gaussian', cmap=plt.cm.viridis,
                       extent=(0.5, np.shape(matrix)[0] + 0.5, 0.5, np.shape(matrix)[1] + 0.5))
            plt.colorbar()
            plt.show()

            return matrix
