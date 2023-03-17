from json.tool import main
import sys
import string

def text_analyzer(count = None):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if (count is None):
        count = input()
    upper = sum(1 for elem in count if elem.isupper())
    lower = sum(1 for elem in count if elem.islower())
    punctuation = sum(1 for elem in count if (elem in string.punctuation))
    space = sum(1 for elem in count if elem.isspace())
    print("There are " + str(lower) + " lowercases letters")
    print("There are " + str(upper) + " uppercases letters")
    print("There are " + str(punctuation) + " punctuation characters")
    print("There are " + str(space) + " spaces")

if __name__== "__main__":
    if len(sys.argv) > 2:
        print("Error number of argument")
        exit(1)
    elif len(sys.argv) == 1:
        text_analyzer()
    else:
        text_analyzer(sys.argv[1])