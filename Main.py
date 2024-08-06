from Console import *

while True:
    try: Menu()
    except Exception as err:
        print(err)
        input()