#1.Write a program which accept N numbers from user and store it into List. Return addition of all
#elements from that List.

#Input : Number of elements : 6
#Input Elements : 13 5 45 7 4 56
#Output : 130


def Addition(value):
    sum = 0

    for i in range(len(value)):
        sum = sum + value[i]
    return sum


def main():
    size = 0
    i=0
    Data = []

    print("How many element you want?")
    size = int(input())

    print("Enter the elements : ")
    for i in range(size):
        Data.append(int(input()))

    print("Your entered data is : ",Data)

    ret = Addition(Data)
    print("Addition is : ",ret)


if __name__ == '__main__':
      main()