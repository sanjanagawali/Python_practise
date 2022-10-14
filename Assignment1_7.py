print("==========Program to check divisible by 5 ============")

def Div(num):
    if (num % 5 == 0):
        return True
    else:
        return False

def main():
    print("Enter number")
    num = int(input())

    ret = Div(num)
    print(ret)

if __name__ == "__main__":
    main()

print("==============================================")

