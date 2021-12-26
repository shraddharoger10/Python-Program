#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user.


from Arithmetic import *

def main():
    print("Enter First Number : ")
    value1 = int(input())

    print("Enter Second Number : ")
    value2 = int(input())

    ret = Add(value1,value2)
    print("Addition is : ",ret)

    ret = Sub(value1, value2)
    print("Subtraction is : ", ret)

    ret = Mult(value1, value2)
    print("Multiplication is : ", ret)

    ret = Div(value1, value2)
    print("Division is : ", ret)


if __name__ == '__main__':
      main()