#10. Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934   Output : 37


def CountDigit(No):
    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        print(Digit)
        Sum = Sum + Digit
        No = (No // 10)

    return Sum


def main():
    num = 0
    print("Enter the number : ")
    num = int(input())

    ret = CountDigit(num)

    print("Addition of digits are : ",ret)



if __name__ == '__main__':
        main()