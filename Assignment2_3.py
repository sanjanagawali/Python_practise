print("==========Program to display factorial============")

def factorial(num):
    factoria = 1
    for i in range(1, num+1):
        factoria = factoria * i
    return factoria

def main():
    print("enter number")
    num = int(input())

    if num < 0:
        print("Can't find factorial for negative numbers")
    elif num == 1:
        print("Factorial of 1 is 1")
    else:
        ret = factorial(num)
        print("Factorial is", ret)

if __name__ == "__main__":
    main()

print("==============================================")
