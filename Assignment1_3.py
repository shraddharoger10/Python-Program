#3. Write a program which contains one function named as Add() which accepts two numbers
#from user and return addition of that two numbers.

#Input : 11   5    Output : 16

def Addition(value1, value2):
    Ans = 0
    Ans = value1 + value2
    return Ans

def main():
    No1 = 0
    N02 = 0

    print("Enter First Number :")
    No1 = int(input())

    print("Enter Second Number : ")
    No2 = int(input())

    ret = Addition(No1, No2)

    print("Addition is : ",ret)


if __name__ == "__main__":
      main()