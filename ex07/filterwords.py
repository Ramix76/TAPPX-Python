import sys
import string

def filter_str():
        str = sys.argv[1]
        n = int(sys.argv[2])
        words = []
        punct = string.punctuation
        for c in punct:
            str = str.replace(c, "")
        for i in str.split(' '):
            if len(i) >= n:
                words.append(i)
        # print(words)

        print([word.replace(punct, "") for word in str.split(" ") if len(word) > n])


__name__ == '__main__'
if len(sys.argv) == 3:
    filter_str()
    exit()
print("\n    Error.Invalid number of arguments.\n")
