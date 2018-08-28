class Day5:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day5(cls, part):
        path = 'Inputs/input5.txt'
        count = len(open(path).readlines())
        lines = open(path).readlines()

        step = 0
        position = 0
        lines = list(map(int, lines))

        if part == 1:
            while position < count:
                next_position = position + lines[position]
                lines[position] += 1
                position = next_position
                step += 1

            return step

        if part == 2:
            while position < count:
                next_position = position + lines[position]
                if lines[position] >= 3:
                    lines[position] -= 1
                else:
                    lines[position] += 1
                position = next_position
                step += 1

            return step
