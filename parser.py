import sys

def get_filename():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        return filename
    else:
        print("papryka")
def main():
    filename = get_filename()
    if len(filename) == 0:
        return
    print(f"File to parse: {filename}")


if __name__ == "__main__":
    main()

def read_from_file_to_list(filename):
    with open("input.txt","r") as file_to_read:
        print(file_to_read.readlines())