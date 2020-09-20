import sys

def get_filename():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        return filename
    else:
        print("papryka")
        return papryka
def main():
    filename = get_filename()
    if len(filename) == 0:
        return
    print(f"File to parse: {filename}")


if __name__ == "__main__":
    main()