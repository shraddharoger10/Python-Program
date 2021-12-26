#5.Write a program which accept one number for user and check whether number is prime or not.
#Input : 5   Output : It is Prime Number

def ChkPrime(No):
      flag = False

      if No > 1:
       for i in range(2, (No//2)):
            if((No % i) == 0):
                  flag = True
                  break

def main():
      num = 0
      print("Enter the number : ")
      num = int(input())

      ret = ChkPrime(num)
      if(ret == True):
            print("Number is not Prime")
      else:
            print("Number is Prime")




if __name__ == '__main__':
      main()