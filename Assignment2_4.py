print("==========Program to display addition of factors============")

def factors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            #print(i)
            sum = sum + i
    return sum

def main():
    print("enter number")
    num = int(input())

    ret = factors(num)
    print("addition of factors is", ret)


if __name__ == "__main__":
    main()

print("==============================================")
