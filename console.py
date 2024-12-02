class Console:
    GREETING = (
    "Welcome to\n"
    " ________  ___       ________ ________\n"
    "|\   __  \|\  \     |\  _____\\\   __  \ \n"
    "\ \  \|\  \ \  \    \ \  \__/\ \  \|\  \ \n"
    " \ \   __  \ \  \    \ \   __\\  \\   __  \ \n"
    "  \ \  \ \  \ \  \____\ \  \_| \ \  \ \  \ \n"
    "   \ \__\ \__\ \_______\ \__\   \ \__\ \__\ \n"
    "    \|__|\|__|\|_______|\|__|    \|__|\|__|\n"
    "\n"
    "Your no.1 task manager!\n"
    "What can I do for you?"
    "\n"
    )

    GOODBYE = "Bye! Hope to see you again soon!"
    LINE = "----------------------------------------------------------------"
    

    @staticmethod
    def greet():
        Console.line()
        print(Console.GREETING)
        Console.line()
        
    @staticmethod
    def line():
        print(Console.LINE)
        
    @staticmethod
    def bye():
        print(Console.GOODBYE)
        Console.line()
