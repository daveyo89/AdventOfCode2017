class Day7:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day7(cls, part):
        import re, numpy as np

        path = 'Inputs/input7.txt'
        data = open(path, 'r').read().splitlines()
        bad_chars = '-()\>,'
        rgx = re.compile('[%s]' % bad_chars)
        numbers = []
        names = []
        backtrack = []

        if part == 1:
            for line in data:
                line = rgx.sub('', line).split()
                names += [line]

            aa = np.array(names)

            for i in range(len(aa)):
                numbers.append(aa[i][1])
            high = max(list(map(int, numbers)))

            for i in range(len(aa)):
                if str(high) in aa[i]:
                    backtrack = aa[i][0]
                    for j in range(len(aa)):
                        if backtrack in aa[j] and int(aa[j][1]) < high:
                            result = aa[j][0]
                            return result

        if part == 2:

            table = dict((m[0], (int(m[1]), m[3].split(', ') if m[3] else []))
                         for m in [re.match('(\w+) \((\d+)\)( -> ((\w+, )*\w+))?', line).groups() for line in data])

            n = (set(table) - set(c for n in table for c in table[n][1])).pop()

            def sorting(table):
                w = lambda n: table[n][0] + sum(w(c) for c in table[n][1])
                b = lambda n: len({w(c) for c in table[n][1]}) == 1
                a = lambda n: sum(w(c) for c in table[n][1]) / len(table[n][1])

                return w, b, a

            w, b, a = sorting(table)

            while not b(n):
                c = sorted(table[n][1], key=lambda c: -abs(w(c) - a(n)))
                n = ([c for c in table[n][1] if not b(c)] + c)[0]

            return table[c[0]][0] + w(c[1]) - w(c[0])
