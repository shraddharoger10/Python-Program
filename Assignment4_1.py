#1.Write a program which contains one lambda function which accepts one parameter and return power of two.

#Input : 4  Output : 16
#Input : 6  Output : 64

Power = lambda no : 2 ** (no)

def main():
    print("Enter the number")
    value = int(input())

    ret =Power(value)

    print("Power is : ",ret)


if __name__ == '__main__':
      main()

