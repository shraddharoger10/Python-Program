#2.Write a program which accept N numbers from user and store it into List. Return Maximum
#number from that List.

#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56


def Maximum(value):
    Max = 0

    for i in range(len(value)):
        if(value[i] > Max):
             Max = value[i]

    return Max


def main():
    size = 0
    i = 0
    Data = []

    print("How many element you want?")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        Data.append(int(input()))

    ret = Maximum(Data)
    print("Maximum number is : ",ret)

if __name__ == '__main__':
      main()
