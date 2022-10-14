print("==========Program to display pattern============")

def main():
    print("enter number")
    num = int(input())

    for i in range(0, num+1):
        for j in range(0,i):
            print(j+1, end =" ")
        print()

if __name__ == "__main__":
    main()

print("==============================================")

