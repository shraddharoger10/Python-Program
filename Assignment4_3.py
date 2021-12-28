#3.Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user.
#Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90.
#Map function will increase each number by 10. Reduce will return product of all that numbers.

#Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#List after filter = [76, 89, 86, 90, 70]
#List after map = [86, 99, 96, 100, 80]
#Output of reduce = 6538752000

from functools import reduce

Range = lambda no : (no>=70) & (no<=90)

Increment = lambda no : no + 10

Product = lambda a,b : a * b

def main():
    size = 0
    Data = []

    print("How many elements you want?")
    size = int(input())

    print("Enter The elements")
    for i in range(size):
        Data.append(int(input()))

    print("Original data is : ",Data)

    newdata = list(filter(Range,Data))
    print("Filtered data is : ",newdata)

    AddData = list(map(Increment,newdata))
    print("Incremented data is : ",AddData)

    ret = reduce(Product,AddData)
    print("Product of numbers is : ",ret)


if __name__ == '__main__':
      main()