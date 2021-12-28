#2.Write a program which contains one lambda function which accepts two parameters and return
#its multiplication.

#Input : 4  3   Output : 12
#Input : 6  3   Output : 18

Multiplication = lambda no1,no2 : no1 * no2

def main():
    print("Enter first number")
    No1 = int(input())

    print("Enter second number")
    No2 = int(input())

    ret = Multiplication(No1, No2)

    print("Multiplication is : ",ret)


if __name__ == '__main__':
      main()