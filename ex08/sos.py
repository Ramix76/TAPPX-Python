import sys
from unicodedata import name

equivalences = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "−.−.−−",
    " ": "/"
}

def check_text(char):
    char = char.upper()
    if char in equivalences:
        return equivalences[char]

def morse_encoding(text):
    morse = ""
    for char in text:
        encoded_char = check_text(char)
        morse += encoded_char + " "
    return morse

__name__ == '__main__'
if len(sys.argv) < 2:
    print("\n    Error.Invalid number of arguments.\n")
    exit()
elif len(sys.argv) == 2:
    string = sys.argv[1]
else:
    string =  ' '.join(sys.argv[1:]) 
print(morse_encoding(string))    