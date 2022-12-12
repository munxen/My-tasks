# Write a function that takes the file name as input and counts the number of lines, 
#of words and letters in the specified file.
def name_file():
    file_search = input ("Enter the file name(name.txt ): ")
    filename = ("C:/Users/") + file_search
    lines = 0
    words = 0
    chars = 0
    with open (filename, 'r') as file:
        for line in file:
            lines += 1
            words += len((line.split()))
            chars += len(line.strip('\n'))
        print ("Number of rows: " + str(lines))
        print ("Number of words: " + str(words))
        print ("Number of letters: " + str(chars))
name_file()