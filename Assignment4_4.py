#4.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which are even. Map function will calculate its square.
#Reduce will return addition of all that numbers.

#Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#List after filter = [2, 4, 4, 2, 8, 10]
#List after map = [4, 16, 16, 4, 64, 100]
#Output of reduce = 204

from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Square = lambda No : No ** 2

Addition = lambda a,b : a + b

def main():
    size = 0
    List = []

    print("How many elements you want to enter?")
    size = int(input())

    print("Enter the elements")
    for i in range(size):
        List.append(int(input()))

    print("Original List is : ",List)

    NewList = list(filter(CheckEven,List))
    print("Even list is : ",NewList)

    List1 = list(map(Square,NewList))
    print("Square of elements is : ",List1)

    AddList = reduce(Addition,List1)
    print("Addition is : ",AddList)



if __name__ == '__main__':
     main()