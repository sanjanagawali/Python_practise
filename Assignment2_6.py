print("==========Program to display pattern============")


def main():
    print("enter number")
    num = int(input())

    for i in range(num + 1, 0, -1):
        for j in range(0, i - 1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    main()

print("==============================================")

