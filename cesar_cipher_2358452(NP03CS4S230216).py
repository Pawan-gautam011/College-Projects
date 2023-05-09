#Defining welcome() function
def welcome():
    print("Welcome to the Ceaser Cipher \nThis program encrypts and decrypts text with the Ceaser Cipher")
    #Print displays the message whereas \n starts a new line

#Defining enter_message() function
def enter_message():
    while True:   # Using while loop to remain in loop until a condition is fulfilled
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        mode = mode.lower()   # Converting to lowercase to accept the Uppercase prompts also
        if mode == "e" or mode == "d":
            break # Condition satifies and ends the loop
        else:
            print("Invalid Mode") # Displays the message and returns to the start of the loop

    while True:
        if mode == "e":
            message = input("What message would you like to encrypt: ").upper() # Converting message to uppercase
            if message:
                break
        else: # Only two modes are possible, so elif is not needed
            message = input("What message would you like to decrypt: ").upper() #Converting message to uppercase
            if message:
                break

    while True:
        try:
            shift = int(input("What is the shift number: "))
            break
        except ValueError: #Shows value error if invalid number is entered, only numbers convertible to integer are accepted
            print("Invalid Shift")

    return (mode, message, shift) #returns mode, message and shift as a tuple after calling enter_message() function

#Defining encrypt() function
def encrypt(message, shift):
    result = "" #Assigning an empty string to result
    for char in message:
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65) #Adding encrypted char to result if char is an alphabet
            #ord changes the alphabets to a value called ascii value(a number) and chr changes it back to alphabets after adding a number
            #Ascii value of uppercase alphabets starts from 65, so substracting 65 to start the values from 0 and getting the modulus to get remainder ranging from 0-25
        else:
            result += char  #Equivalent to result = result + char
                                                                            
    return result  #Returns the result

#Defining decrypt() function
def decrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            result += chr((ord(char) - 65 - shift) % 26 + 65) 
            #Subtracting the shift otherwise same as for encrypt() function
        else:
            result += char
    return result

#File handling
def process_file(filename, mode):  #defining process_file which takes two parameter
    messages = []  #empty list assigned to messages
    with open(filename) as file:
        for line in file:
            message = line.upper()
            if mode == "e":
                messages.append(encrypt(message, shift))  #appending encrypted message to the empty list
            else:
                messages.append(decrypt(message, shift)) #appending decryped message to the empty list
    return messages #returns the appended list

def write_message(messages): #defining write_message() to add to file results.txt
    with open("results.txt", "w") as file:
        for message in messages:
            file.write(message + "\n")

def is_file(filename):    #defining is_file() to return true or false if the file name is valid or not
    try:
        with open(filename):
            return True
    except FileNotFoundError:
        return False

def message_or_file():
    while True:   # Using while loop to remain in loop until a condition is fulfilled
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        mode = mode.lower()   # Converting to lowercase to accept the Uppercase prompts also
        if mode == "e" or mode == "d":
            break # Condition satifies and ends the loop
        else:
            print("Invalid Mode") # Displays the message and returns to the start of the loop

    while True:
        read = input("Would you like to read from a file (f) or the console (c)? ")
        if read == "f":
            while True:
                filename = input("Enter a filename: ") #if user enters f ask the filename.
                if not is_file(filename):
                    print("Invalid Filename")
                    continue
                    
                else:
                    while True:
                        try:
                            global shift
                            shift = int(input("What is the shift number: "))#Ask user for shift number in integers
                            break
                        except ValueError:  #if input cannot be converted into integers, loop continues until valid input is given
                            pass
                    return mode, None, filename
        elif read == "c":
            while True:
                if mode == "e":
                    message = input("What message would you like to encrypt: ").upper() # Converting message to uppercase
                    if message:
                        return mode, message, None
                else: # Only two modes are possible, so elif is not needed
                    message = input("What message would you like to decrypt: ").upper() #Converting message to uppercase
                    if message:
                        return mode, message, None

        else:
            continue
def main():  #main function
    welcome()
    while True:
        mode, message, filename = message_or_file()  #assigning values to mode message and filename which is returned from message_or_file() function 
        if message:
            while True:
                try:
                    shift = int(input("What is the shift number: "))  #Ask user for shift number in integers
                    break
                except ValueError:  #if input cannot be converted into integers, loop continues until valid input is given
                    continue
            if mode == "e":
                result = encrypt(message, shift) #calling encrypt function     
                print(result)
            else:
                result = decrypt(message, shift) #callimg decrypt function
                print(result)
        else:
            messages = process_file(filename, mode)
            write_message(messages)
            print("Messages written to results.txt")
        while True:
            again = input("Would you like to encrypt or decrypt another message? (y/n): ") #ask user for yes or no to continue program
            if again != "y" and again != "n":  #if user is not equal to "y" or "n" loop continues
                continue
            else:
                break
        if again == "n":
            print("Thanks for using the program, Goodbye!!")#if again loop ends and print goodbye
            break
        else:
            continue #if again==y loop continues and asks user desired prompt
            
main() #calling main function
