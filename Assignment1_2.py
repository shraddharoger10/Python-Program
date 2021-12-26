#2. Write a program which contains one function named as ChkNum() which accept one
#parameter as number. If number is even then it should display “Even number” otherwise
#display “Odd number” on console.

#Input : 11  Output : Odd Number
#Input : 8   Output : Even Number

def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False


def main():
    value = 0

    print("Enter Number : ")
    Value = int(input())

    bRet = ChkNum(Value)
    if(bRet == True):
        print("The given number is Even")
    else:
        print("The given number is Odd")


if __name__ == '__main__':
       main()
