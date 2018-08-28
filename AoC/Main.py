import AoC.Days.DayHandler as dh


class Console:

    @staticmethod
    def run():
        """Commands:
        display() : Displays currently set day and part.
        run()     : Executes currently set day and part.
        back      : Back to Main Menu.
        """

        while True:
            task = switch()

            if task == "1":
                exec("d.day = " + input("Give day: "))
                exec("d.part = " + input("Give part: "))
                continue
            elif task == "2":
                inside = True
                while inside:
                    answer = input("Waiting for input..\n")
                    try:
                        eval("d." + answer)
                    except Exception:
                        "No valid day or part given!"
                    if answer == "back":
                        break
                    if answer == "help":
                        print(Console.run.__doc__)


def switch():
    switcher = {
        1: 'Set day and part',
        2: 'Options'
    }
    return input(switcher)


d = dh.DayHandler(day=1, part=1)
Console.run()
