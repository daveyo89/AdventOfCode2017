class Day1:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day1(cls, part):

        path = "Inputs/input1.txt"
        i = 0
        total = 0
        with open(path, 'r') as file:
            if part == 1:
                for row in file:
                    while i < len(row) - 1:
                        if row[i] is row[i + 1]:
                            total += int(row[i])
                        i += 1
                    if (row[-1]) is row[0]:
                        total += int(row[0])
                return total, i

            elif part == 2:
                file = file.read()
                step = int(file.__len__() / 2)
                for i in range(file.__len__()):
                    if file[i] is file[(i + step) % (file.__len__())]:
                        total += int(file[i])
                return total
