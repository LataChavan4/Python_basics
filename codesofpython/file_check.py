def readFiles(filename):
    try:
        with open (filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")



readFiles('1.txt')
readFiles('2.txt')
readFiles('3.txt')