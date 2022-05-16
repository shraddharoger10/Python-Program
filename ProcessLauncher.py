import subprocess
from sys import *
import subprocess

def Find(string):
    process = ".exe"

def ProcessLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            process = Find(line)
            print(process)
            for program in process:
                subprocess.Popen([program])

def main():
    print("___________________ Process Launcher_______________________")
    print("Script name : ",argv[0])
    print("Number of arguments accepted : ",len(argv) - 1)

    if(len(argv) < 1):
        print("Invalid number of arguments")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Script is used to open the process ")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : Name_of_Script First_Argument")
        exit()


if __name__ == '__main__':
    main()

