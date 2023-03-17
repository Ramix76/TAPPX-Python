import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
elif len(sys.argv) == 1:
    print("AssertionError: more arguments needed")
elif not sys.argv[1].isdigit():
    print("AssertionError: argument is not an integer") 
elif int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
elif int(sys.argv[1]) == 0:
    print("I'm Zero.")
else:
    print("I'm Odd.")