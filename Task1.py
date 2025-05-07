try:
    file1=open('sample.txt', 'r')
    readingfile=file1.read()
    print('Reading file content:')
    file1.close()
    print(readingfile)
except FileNotFoundError:
    print("Error: The file sample.txt not found.")
