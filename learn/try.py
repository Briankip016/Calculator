try:
    file = open("learn/test.txt", "r")
    data = file.read()
    print("The data is: ", data)
except FileNotFoundError:
    print("Sorry,Please check the file name and path")
finally:
    print("Thankyou for using the program")