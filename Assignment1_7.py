#7. Write a program which contains one function that accept one number from user and returns
#true if number is divisible by 5 otherwise return false.

#Input : 8    Output : False
#Input : 25   Output : True

def Divisible(No):
    if(No % 5 == 0):
        return  True
    else:
        return  False

def main():
    value = 0
    print("Enter The Number : ")
    value = int(input())

    bRet = False

    bRet = Divisible(value)
    if(bRet == True):
        print("Number is Divisible by 5")
    else:
        print("Number is not Divisible by 5")


if __name__ == '__main__':
      main()