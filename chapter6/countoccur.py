c = 0

def count():
    string = input("Please enter a word: ")
    char = input("Please enter a character: ")
    list(string)
    print(list(string))

    for bingo in list(string):
        if bingo == char:
            c + 1
        else:
            continue
count()
