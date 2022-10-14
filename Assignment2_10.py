print("==========Program to return addition of digits in number============")

def main():
    print("enter number")
    num = input()

    sum = 0
    for i in str(num):
        sum = sum + int(i)
    print(sum) #/

if __name__ == "__main__":
    main()

print("==============================================")

