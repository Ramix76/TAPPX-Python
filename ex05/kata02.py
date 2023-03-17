import numbers


kata = (2019, 9, 25, 3, 30)

for i in kata:
    if i < 0:
        print("Error.Please inserta positive number")
        exit()

__name__ == '__main__'
print(f"{kata[1]:02}/{kata[2]:02}/{kata[0]:04} {kata[3]:02}:{kata[4]:02}")