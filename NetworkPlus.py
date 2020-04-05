from random import *

def main():
    
    choice = input("Just 'p'orts, 'i'p, 't'ransmisisson, 's'tandards, or study 'e'verything?")

    if choice.lower() == "p":
        flashcards = open("ports.txt", "r")
    elif choice.lower() == "i":
        flashcards = open("ip.txt")
    elif choice.lower() == "t":
        flashcards = open("transmission.txt")
    elif choice.lower() == "s":
        flashcards = open("standards.txt")
    else:
        flashcards = open("flashcards.txt", "r")

    flashDict = {}
    flashKeys = []
    wrongKeys = []
    done = False
    count = 0

    for card in flashcards:
        question, answer = card.split(",")
        answer = answer.strip("\n")
        flashDict[question] = answer.lower()

    for key in flashDict.keys():
        flashKeys.append(key)

    for i in range(len(flashKeys) - 1):
        num = randrange(0, (len(flashKeys) - 1))
        flashKeys[i], flashKeys[num] = flashKeys[num], flashKeys[i]

    for question in flashKeys:
        questionStr = question + ": "
        answer = input(questionStr)

        if answer.lower() in flashDict[question]:
            print("CORRECT!\n")
            count = count + 1
        else:
            print("Incorrect! Answer: ", flashDict[question], "\n")
            wrongKeys.append(question)
        
    print("You got: ", count, "correct out of ", len(flashDict))
    print("Work on: ")

    for key in wrongKeys:
        print(key)
    
main()
