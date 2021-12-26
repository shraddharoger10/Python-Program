#3.Write a program which accept N numbers from user and store it into List. Return Minimum
#number from that List.

#Input : Number of elements : 4
#Input Elements : 13 5 45 7
#Output : 5


def Minimum(value):
    Min = value[0]

    for i in range(len(value)):
        if(value[i] < Min):
             Min = value[i]

    return Min


def main():
    size = 0
    i = 0
    Data = []

    print("How many element you want?")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        Data.append(int(input()))

    ret = Minimum(Data)
    print("Minimum number is : ",ret)

if __name__ == '__main__':
      main()
