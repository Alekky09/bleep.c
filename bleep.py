from cs50 import get_string
from sys import argv


def main():

    if len(argv) != 2:
        exit("Usage: python bleep.py dictionary")

    dictionary = open(argv[1], "r")

    file = {line.strip() for line in dictionary}
    print(file)

    message = get_string("What message would you like to censor?\n")
    message_list = message.split()

    for word in message_list:

        if word in file:
            for char in word:
                print("*", end = "")
        else:
            print(word, end = "")
        print(" ", end = "")
    print("")

if __name__ == "__main__":
    main()
