#2. Write a program which accept one number and display below pattern.
#Input : 5
#Output : * * * * *
#         * * * * *
#         * * * * *
#         * * * * *
#         * * * * *

def Pattern():
    for i in range(1,5):
        for j in range(1,5):
            print("*",end="   ")
        print(" ")

def main():
    Pattern()

if __name__ == '__main__':
     main()