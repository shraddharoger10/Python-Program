#4.Write a program which accept N numbers from user and store it into List. Accept one another
#number from user and return frequency of that number from List.

#Input : Number of elements : 11
#Input Elements : 13 5 45 7 4 56 5 34 2 5 65
#Element to search : 5
#Output : 3


def Frequency(value, No):
    Cnt = 0
    for i in range(len(value)):
        if(No == value[i]):
            Cnt = Cnt + 1

    return Cnt


def main():
    size = 0
    num = 0
    Data = []

    print("How many element you want?")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        Data.append(int(input()))

    print("Enter number to search : ")
    num = int(input())

    ret = Frequency(Data,num)
    print("Frequency is : ",ret)


if __name__ == '__main__':
      main()