print("==========Program to check count of char============")

def countchar(word):
    i = 0
    for no in word:
        i = i + 1
    return i 


def main():
    print("enter word: ")
    word = input()
    ret = countchar(word)
    print(ret)

if __name__ == "__main__":
    main()

print("==============================================")

