from AoC.Days import Day1, Day2, Day3, Day4, Day5


class DayHandler:

    def __init__(self, day, part):
        self._day = day
        self._part = part

    @property
    def day(self):
        print("Getting day...")
        return self._day

    @day.setter
    def day(self, value):
        print("Setting day to: " + str(value))
        self._day = value

    @day.deleter
    def day(self):
        print("Deleting day")
        del self._day

    @property
    def part(self):
        print("Getting part...")
        return self._part

    @part.setter
    def part(self, value):
        print("Setting part to: " + str(value))
        self._part = value

    @part.deleter
    def part(self):
        print("Deleting part..")
        del self._part

    def display(self):
        print(str(self.day) + " " + str(self.part))

    def set(self, *args):
        self.day = args[0]
        self.part = args[1]

    def run(self):
        x, y = self._day, self._part
        print("Solution: " + str(eval("Day" + str(x) + ".Day" + str(x) + ".Day" + str(x) + "(" + str(y) + ")")))

    @staticmethod
    def exit():
        exit()
