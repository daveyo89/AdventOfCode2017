class Day2:

    def __init__(self, part):
        self._part = part

    @classmethod
    def Day2(cls, part):

        path = 'Inputs/input2.txt'
        with open(path, "r") as file:
            file = file.read()
            total = 0

            if part == 1:

                line = file.replace("\t", " ").splitlines()
                for i in line:
                    row_numbers = i.split(" ")
                    row_numbers = list(map(int, row_numbers))
                    top = max(row_numbers)
                    low = min(row_numbers)
                    total += top - low

                return total

            elif part == 2:
                line = file.replace("\t", " ").splitlines()
                for i in line:
                    row_numbers = i.split(" ")
                    row_numbers = list(map(int, row_numbers))

                    for n in row_numbers:
                        for k in row_numbers:
                            if n % k == 0 and n is not k:
                                total += n / k

                return total
