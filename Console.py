from Progs import *
from CodeFeatures import *
import inquirer

@Func
def Menu():
    questions = [
        inquirer.List('choice',
                      message="Select menu item",
                      choices=['Comp Info', 'Get Weather', 'Get cat fact', 'Run audio file', 'Shorten the link', 'Wikipedia', 'FREE windows and office activators', 'Generate password', 'Exit'])
    ]

    choice = inquirer.prompt(questions)['choice']

    clearConsole()
    tprint('Progs.py')

    if choice == 'Comp Info': GetMyIP()
    elif choice == 'Get Weather': Weather()
    elif choice == 'Get cat fact': GetCatFact()
    elif choice == 'Run audio file':
        dir = input("Please enter audio file dir: (end=\"/ or \\\"): ")
        clearConsole()
        tprint('Progs.py')
        file = input("Please enter audio file name (and enter .file extension): ")
        clearConsole()
        tprint('Progs.py')

        RunAudioFile(dir, file)
    elif choice == 'Shorten the link': ShortenTheLink()
    elif choice == 'Wikipedia': Wikipedia()
    elif choice == 'Generate password': GeneratePassword()
    elif choice == 'FREE windows and office activators': WindowsAndOffice()
    elif choice == 'Exit': exit()