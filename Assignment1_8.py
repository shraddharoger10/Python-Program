#8. Write a program which accept number from user and print that number of “*” on screen.
#Input : 5  Output : * * * * *

def Pattern(value):
    for i in range(0, value, 1):
        print("*",end=" ")


def main():
    print("Enter Number : ")
    No = int(input())

    Pattern(No)


if __name__ == '__main__':
      main()