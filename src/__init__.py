if __package__:
    from pluGET.utils.consoleoutput import consoleTitle, clearConsole, printMainMenu
    from pluGET.utils.utilities import check_requirements
    from pluGET.handlers.handle_input import createInputLists, getInput
    from pluGET.handlers.handle_config import checkConfig
else:
    from utils.consoleoutput import consoleTitle, clearConsole, printMainMenu
    from utils.utilities import check_requirements
    from handlers.handle_input import createInputLists, getInput
    from handlers.handle_config import checkConfig


def mainFunction():
    consoleTitle()
    clearConsole()
    checkConfig()
    check_requirements()
    createInputLists()
    printMainMenu()
    getInput()

mainFunction()
