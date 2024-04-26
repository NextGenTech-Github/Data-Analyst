while True:
    try:
        data=int(input("Enter a Number: "))
        print ("You entered: ", data)
        break;
    except ValueError:
        print ("Invalid input")