import AoC.Days.DayHandler as dh


class Console:

    @staticmethod
    def run():
        """Commands:
        display() : Displays currently set day and part.
        run()     : Executes currently set day and part.
        back      : Back to Main Menu.
        set(x,y)  : Set day and part without going back.
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

                    if answer == "back":
                        break
                    if answer == "help":
                        print(Console.run.__doc__)
                    else:
                        try:
                            eval("d." + answer)
                        except Exception:
                            print("Invalid command given, type \"help\" for list of commands.")


def switch():
    switcher = {
        1: 'Set day and part',
        2: 'Options'
    }
    return input(switcher)


d = dh.DayHandler(day=1, part=1)
Console.run()
