print("==========Program to check odd and even number============")

def ChkNum(no):
    if ((no % 2) == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Please enter number :")
    no = int(input())
    
    ChkNum(no)

if __name__ == "__main__":
    main()

print("=======================================================")

