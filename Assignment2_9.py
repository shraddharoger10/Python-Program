#9. Write a program which accept number from user and return number of digits in that number.
#Input : 5187934   Output : 7

def CountDigit(No):
    Digit = 0
    Cnt = 0

    while(No != 0):
        Digit = No % 10
        print(Digit)
        Cnt = Cnt + 1
        No = (No // 10)

    return Cnt


def main():
    num = 0
    print("Enter the number : ")
    num = int(input())

    ret = CountDigit(num)

    print("Number of digits are : ",ret)



if __name__ == '__main__':
      main()