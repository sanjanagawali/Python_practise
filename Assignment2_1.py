print("==========Program to perform mathematical functions ============")

def Addition():
    print("Addition function")
    print("enter first number")
    num1 = int(input())
    print("enter second number")
    num2 = int(input())
    sum = num1 + num2
    print("Addition of numbers is", sum)

def Substraction():
    print("Substraction function")
    print("enter first number")
    num1 = int(input())
    print("enter second number")
    num2 = int(input())
    if num1 > num2:
        sum = num1 - num2
    else:
        sum = num2 - num1
    print("Substraction of numbers is", sum)

def Multiplication():
    print("Multiplication function")
    print("enter first number")
    num1 = int(input())
    print("enter second number")
    num2 = int(input())
    sum = (num1 * num2)
    print("Multiplication of numbers is", sum)

def Division():
    print("Division function")
    print("enter first number")
    num1 = int(input())
    print("enter second number")
    num2 = int(input())
    sum = num1 / num2
    print("Division of numbers is", sum)

def display():
    print("Please enter input as below for functions: \n 1-Addition \n 2-Substraction \n 3-Multipication\n 4-Division")

def main():
    display()

    print("Enter you input between 1 to 4")
    choice = int(input())

    if(choice == 1):
        Addition()
    elif(choice == 2):
        Substraction()
    elif(choice == 3):
        Multiplication()
    elif(choice == 4):
        Division()
    else:
        print("enter valid input")

if __name__ == "__main__":
    main()

print("==============================================")


#output:

#==========Program to perform mathematical functions ============
#Please enter input as below for functions:
#1-Addition
#2-Substraction
#3-Multipication
#4-Division
#Enter you input between 1 to 4
#1
#Addition function
#enter first number
#12
#enter second number
#23
#Addition of numbers is 35
#==============================================

