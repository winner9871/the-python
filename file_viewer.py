import os.path

def main():
    fname = input("Enter The Name Of File:")
    while not os.path.exists(fname):
        print(fname, "Doesn't Exists, Kindly Enter a valid file name")
        fname = input("Enter The Name Of File:")

    with open(fname, "rt") as fobj:
        lines = fobj.readlines()
    
    numOfLines = len(lines)
    
    print(f"There are {numOfLines} lines in {fname}")
    print("Enter Line Number You Want To See")
    print("Anytime Enter 0 to exit")

    while True:
        lineNum = int(input("Enter The Line Number :\t"))
        if lineNum == 0:
            break
        elif lineNum > numOfLines:
            print(f"Sorry But there are only {numOfLines} lines in {fname}")
        else:
            print(f"{lineNum:4d} {lines[lineNum - 1]}")


    

if __name__ == "__main__":
    main()

