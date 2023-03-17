import sys

def math(data):
    if (data is None):
        data = input("Please introduce arguments: ").split()
    print(f"The sum is: { int(data[0]) + int(data[1])}")
    print(f"The difference is: { int(data[0]) - int(data[1])}")
    print(f"The product is: { int(data[0]) * int(data[1])}")
    try:
        print(f"The quotient is: { int(data[0]) / int(data[1])}")
        print(f"The remainder is: { int(data[0]) % int(data[1])}")
    except:
        print("Operation not possible.")
        print("Operation not possible.")
    
if __name__== "__main__":
    if ((len(sys.argv) > 3 or len(sys.argv) < 3) and (len(sys.argv) > 1)):
        print("ERROR:Invalid number of arguments.")
    elif (len(sys.argv) == 1):
        math(None)
    elif not (sys.argv[1].isdigit()):
        print("The arguments are not integers.") 
    elif not (sys.argv[2].isdigit()):
        print("The arguments are not integers.") 
    elif (len(sys.argv) == 3):
        data = sys.argv[1], sys.argv[2]
        math(data)
    