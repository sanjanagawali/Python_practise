print("==========Program for addition of two numbers============")

def Add(num1, num2):
    sum = num1 + num2
    return sum

def main():
    print("Enter first number")
    num1 = int(input())
    print("Enter second number")
    num2 = int(input())
    sum = Add(num1,num2)

    print("Addition of two numbers is: ",sum)


if __name__ == "__main__":
    main()

print("==============================================")

