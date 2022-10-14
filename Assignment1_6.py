print("==========Program to display positive/negative number============")

def ChkNum(num):
    if (num > 0):
        print("Positive number")
    elif (num < 0):
        print("Negative number")
    else:
        print("Zero")

def main():
    print("Enter number:")
    num = int(input())

    ChkNum(num)


if __name__ == "__main__":
    main()

print("==============================================")

