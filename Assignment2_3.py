#3. Write a program which accept one number from user and return its factorial.
#Input : 5    Output : 120

def Factorial(No):
    Fact = 1

    if(No < 0):
        No =(-No)

    while(No != 0):
        Fact = Fact * No
        No = No - 1

    return Fact


def main():
    num = 0

    print("Enter The Number : ")
    num = int(input())

    ret = Factorial(num)

    print("Factorial of given number is : ",ret)


if __name__ == '__main__':
    main()