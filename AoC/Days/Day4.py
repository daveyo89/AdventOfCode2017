class Day4:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day4(cls, part):

        path = 'Inputs/input4.txt'
        val = open(path, 'r').read()

        if part == 1:
            lines = val.splitlines()
            max_lines = len(lines)
            in_valid = 0

            for line in lines:
                line = line.split()
                for word in line:
                    if line.count(word) > 1:
                        in_valid += 1
                        break

            return max_lines - in_valid

        if part == 2:
            lines = val.splitlines()
            max_lines = len(lines)
            in_valid = 0

            for line in lines:
                line = line.split()
                temp_line = []
                for i in range(len(line)):
                    temp_line.append([''.join(sorted(line[i]))])

                for word in temp_line:
                    if temp_line.count(word) > 1:
                        in_valid += 1
                        break

            return max_lines - in_valid
