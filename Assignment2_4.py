#4.Write a program which accept one number form user and return addition of its factors.
#Input : 15  Output : 16

def AddFactors(No):
    Sum = 0

    Cnt = 1
    while(Cnt <= (No/2)):
        if((No % Cnt) == 0):
            Sum = Sum + Cnt
        Cnt = Cnt + 1

    return Sum


def main():
    num = 0

    print("Enter the number : ")
    num = int(input())

    ret = AddFactors(num)

    print("Addition of Factors is : ",ret)


if __name__ == '__main__':
      main()