#6.Write a program which accept number from user and check whether that number is positive or negative or zero.

#Input : 11   Output : Positive Number
#Input : -8   Output : Negative Number
#Input : 0    Output : Zero

def ChkNumber(No):
    if(No < 0):
        print("Number is negative")
    elif(No > 0):
        print("Number is Positive")
    else:
        print("Number is zero")

def main():
    Value = 0
    print("Enter the Number : ")
    Value = int(input())

    ChkNumber(Value)


if __name__ == '__main__':
     main()