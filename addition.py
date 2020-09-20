import sys

def main():
    sum = 0
    for i in sys.argv:
        if i.isdigit() == False:
            continue
        sum+=int(i)
    print(sum)
if __name__ == "__main__":
    main()

