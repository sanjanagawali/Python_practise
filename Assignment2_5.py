print("==========Program to check prime number============")


def prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            print("number is not prime")
            break
    else:
        print("number is prime")


def main():
    print("enter number")
    num = int(input())

    if num == 1:
        print("1 is not prime number ")
    elif num == 0:
        print("0 is nor prime neither composite")
    elif num < 0:
        print("please enter a valid whole number")
    else:
        if num > 1:
            prime(num)


if __name__ == "__main__":
    main()

print("==============================================")
