#6. Write a program which accept one number and display below pattern.
#Input : 5
#Output : * * * * *
#         * * * *
#         * * *
#         * *
#         *


def Pattern(num):
    for i in range(num + 1,0,-1):
        for j in range(0,i-1):
            print("*",end="  ")
        print(" ")

def main():
    rows = 0
    print("Enter the number of rows : ")
    rows = int(input())

    Pattern(rows)

if __name__ == '__main__':
     main()