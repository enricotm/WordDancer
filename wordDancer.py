import time
import random as rd

init_word = input("Palavra: ")
spaces = 40

def printWord(crt_word):
    print(' '*(90-spaces-round(len(init_word)/2))+crt_word)
    time.sleep(.02)

def snake(repeat):
    word = init_word
    for _ in range(repeat):
        for _ in range(spaces):
            word = " "+word
            printWord(word)
        for _ in range(spaces):
            word = word[1:]
            printWord(word)

def wrapAroundRight(repeat):
    word = init_word+" "*spaces
    for _ in range(len(word)*repeat):
        word = word[-1]+word[:-1]
        printWord(word)

def wrapAroundLeft(repeat):
    word = init_word+" "*spaces
    for _ in range(len(word)*repeat):
        word = word[1:]+word[0]
        printWord(word)

def splitHalf(repeat):
    word = init_word
    for _ in range(int(spaces/2)):
        word = " "+word+" "
        printWord(word)
    for _ in range(repeat):
        for _ in range(int(spaces/2)):
            word = word[1:round(len(word)/2)]+"  "+word[round(len(word)/2):-1]
            printWord(word)
        for _ in range(int(spaces/2)):
            word = " "+word[:round(len(word)/2)-1]+word[round(len(word)/2)+1:]+" "
            printWord(word)
    for _ in range(int(spaces/2)):
        word = word[1:-1]
        printWord(word)

printWord(init_word)
while True:
    repeat = rd.randint(1,4)
    move = rd.randint(1,4)
    if move == 1:
        snake(repeat)
    elif move == 2:
        wrapAroundRight(repeat)
    elif move == 3:
        wrapAroundLeft(repeat)
    elif move == 4:
        splitHalf(repeat)