#10. Write a program which accept name from user and display length of its name.
#Input : Marvellous  Output : 10

def Length(string):
    print(len(string))

def main():
    print("Enter Name : ")
    str = input()

    Length(str)

if __name__ == '__main__':
      main()