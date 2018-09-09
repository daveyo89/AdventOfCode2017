class Day6:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day6(cls, part):
        path = 'Inputs/input6.txt'
        data = list(map(int, open(path, 'r').read().split()))
        length = len(data)
        s = set()
        if part == 1:
            while tuple(data) not in s:
                s.add(tuple(data))
                top = max(data)
                index = data.index(top)
                data[index] = 0
                for i in range(top):
                    data[(index + i + 1) % length] += 1
            return len(s)

        if part == 2:
            r = set()
            for _ in ['-'] * 2:
                s = set()
                while tuple(data) not in s:
                    s.add(tuple(data))
                    top = max(data)
                    index = data.index(top)
                    data[index] = 0
                    for j in range(top):
                        data[(index + j + 1) % length] += 1
                r.add(len(s))
            return r
