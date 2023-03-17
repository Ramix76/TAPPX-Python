kata = "The right format"

if len(kata) > 42:
    print("Error,too long")
    exit()

__name__ == '__main__'

print(kata.rjust(42,"-"), end="")
