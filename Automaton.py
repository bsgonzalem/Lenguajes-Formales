def zerone(string, i):
    
    if i >= len(string):
        return False

    if string[i] == 'a':
        return twofour(string, i + 1)

    if string[i] == 'b':
        return eight(string, i + 1)

    return False


def twofour(string, i):
    if i >= len(string):
        return True

    if string[i] == 'a':
        return seven(string, i + 1)

    if string[i] == 'b':
        return fiftyeight(string, i + 1)

    return False


def seven(string, i):
    if i >= len(string):
        return False

    if string[i] == 'a':
        return seven(string, i + 1)

    if string[i] == 'b':
        return eight(string, i + 1)

    return False


def eight(string, i):
    
    if i >= len(string):
        return True

    if string[i] == 'a':
        return eight(string, i + 1)

    if string[i] == 'b':
        return eight(string, i + 1)

    return False


def sixtyeight(string, i):
    
    if i >= len(string):
        return True

    if string[i] == 'a':
        return sixtyeight(string, i + 1)

    if string[i] == 'b':
        return eight(string, i + 1)

    return False


def fiftyeight(string, i):

    if i >= len(string):
        return True

    if string[i] == 'a':
        return fiftyeight(string, i + 1)

    if string[i] == 'b':
        return sixtyeight(string, i + 1)

    return False



string = input("insert the string for the automaton: ")
accepted = zerone(string, 0)

if accepted:
    print("This string was accepted by the automaton")
else:
    print("this string isnt allowed for the automaton")