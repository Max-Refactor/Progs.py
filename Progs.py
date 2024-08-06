from CodeFeatures import *
from Pages import *
from Weather import get_weather
from prettytable import PrettyTable
import socket, pyglet, pyshorteners, wikipedia, os, random, requests


@Func
def GetMyIP():
    try:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        data = PrettyTable()
        data.field_names = ["hostname", "ip"]
        data.add_row([hostname, IPAddr])
        print(data)
    except Exception as err:
        print(err)
    input()

@Func
def RunAudioFile(dir: str = "", file: str = ""):
    try:
        if dir == "": dir = "./music/"
        if file == "": file = "music.mp3"

        player = pyglet.media.Player()

        source = pyglet.media.load(dir + file)

        player.queue(source)
        player.play()

        print("To stop music press ENTER", end="")
    except Exception as err:
        print(err)
    input()

@Func
def ShortenTheLink(url: str = ""):
    if url == "":
        url = input("Enter your url for shorten: ")

    try:
        shorteners = pyshorteners.Shortener()
        print("Short LINK - ", shorteners.tinyurl.short(url))
    except Exception as err:
        print(err)
    input()

@Func
def Wikipedia(search: str = ""):
    if search == "":
        search = input("Enter your query on Wikipedia (Title): ")

    try:
        questions = [
            List('choice',
                 message="Select Language",
                 choices=['Ukraine', 'Russian', 'English']
                 )
        ]
        answers = prompt(questions)
        choice = answers['choice']

        if choice == 'Ukraine':
            lang = 'uk'
        elif choice == 'Russian':
            lang = 'ru'
        else:
            lang = 'en'

        wikipedia.set_lang(lang)
        print(wikipedia.summary(search))

    except Exception as err:
        print(err)
    input()

@Func
def WindowsAndOffice():
    file = __file__.replace('Progs.py', '.cmd/MAS_AIO-CRC32_31F7FD1E.cmd')
    os.startfile(file, 'runas')

@Func
def Weather():
    questions = [
        List('choice',
             message="Select Language",
             choices=['Ukraine', 'Russian', 'English']
             )
    ]
    answers = prompt(questions)
    choice = answers['choice']

    if choice == 'Ukraine':
        lang = 'ua'
    elif choice == 'Russian':
        lang = 'ru'
    else:
        lang = 'en'

    clearConsole()
    tprint('Progs.py')

    get_weather(lang)
    input()

@Func
def GeneratePassword(Number_of_characters_in_the_password: int = 0):
    if Number_of_characters_in_the_password == 0: Number_of_characters_in_the_password = int(input("How many characters should be in the password?\n>"))
    clearConsole()
    symvols_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r' 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symvols_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    smvols_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symvols_ = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '/', ':', ';', '?', '[', ']', '{', '}']
    all_symvols = symvols_upper + symvols_lower + smvols_number + symvols_

    password = ''
    for i in range(Number_of_characters_in_the_password):
        password = password + random.choice(all_symvols)

    print(f'Your password is \"{password}\"')
    input()

@Func
def GetCatFact():
    clearConsole()
    tprint('Progs.py')

    try:
        fact = requests.get('https://cat-fact.herokuapp.com/facts').json()[0]['text']
        print(fact)
    except Exception as err:
        print(err)
    input()

if __name__ == '__main__':
    GetMyIP()