class Day8:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day8(cls, part):
        path = 'Inputs/input8.txt'
        data = open(path, 'r')

        if part == 1:

            ls = [x.strip().split() for x in data.readlines()]
            operands = {'==': 'eq', '!=': 'ne', '<=': 'le', '>=': 'ge', '<': 'lt', '>': 'gt'}
            di = {}
            highest = 0

            for line in ls:
                var1 = line[0]
                var2 = line[4]
                plus_or_minus = line[1]
                amount = int(line[2])
                operand = line[5]
                value = int(line[6])

                if getattr(di.get(var2, 0), '__' + operands[operand] + '__')(value):
                    di[var1] = di.get(var1, 0) + (amount if plus_or_minus == 'inc' else -amount)
                    highest = max(highest, di[var1])

            return max(di.values()), highest
