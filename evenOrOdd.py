value = 0
inputvalue = 0
while (int(inputvalue) != -1):
    inputvalue = int(input("please enter a number: "))
    if inputvalue != -1:
        print(f"Value Inputed is: {inputvalue}")
        if (int(inputvalue) % 2) != 0:
            print("Odd")
        else:
            print("even")
