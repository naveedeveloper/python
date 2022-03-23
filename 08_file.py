"""
File Modes : 
-> w = write
-> r = read
-> a = append
-> r+ = both read and write
-> w+ = both read and write, if file does not exits it will create a file and if file exits it will overwrite it.

How to create File?
-> use open() function

open() Exp :
-> open("path and file name", "File mode")
e.g
-> open("c:\\D\\abc.txt","r+")

file realted functions :
-> open()
-> write()
-> read()
-> close()

Special Case:
-> if we open file like 
    with open("c:\\python\\abc.txt","r") as f
-> In above case, we don't need to close the file b/c (with) will close it. 
-> closed = this is used to detect neith file is close or not.
e.g
print(f.closed)
"""

from os import read


f = open("F:\\python\\file.txt", "w")
f.write("My name is Tayyub Naveed.\nThis is the first file writing . . .")
f.close()


with open("F:\\python\\file.txt", "w") as f:
    f.write("My name is Tayyub Naveed.\nOverwriting File. . .")

print("To check weither file is closed or not  : ", f.closed)
# Above both method are the same. . . 

f = open("F:\\python\\file.txt", "r")
print(f.read())
f.close()

# Q : Calculate the number of words in file.
# split() function will return the list of strings by using the given parameter.
# len() function is use to convert that list into numeric value.

f = open("F:\\python\\file.txt", "r")
numberOfLetters = 0
for line in f:
    wrd = line.split(" ")
    print("List : ", wrd)    
    numberOfLetters += len(wrd)

f.close()
print("Total Number of letters : ", numberOfLetters)

# Q : Calculate the number of lines in file.

fileName = "F:\\python\\file.txt"
fileMode = "r"

f = open(fileName, fileMode)
numberOfLines = 0

for line in f:   
    numberOfLines += 1

f.close()
print("Total Number of Lines : ", numberOfLines)

# Q: Calculate the number of charactors in file

f = open(fileName, fileMode)
data = f.read()
print("Number of charactors in file : ", len(data))
f.close()

# Shortcut to find the number of charactors, number of words and number of line in file.
print("Shortcut. . . . . !!!!")
f = open(fileName, fileMode)
data = f.read()
print("Number of charactors in file : ", len(data))
print("Number of Words in file : ", len(data.split()))
print("Number of lines in file : ", len(data.splitlines()))
f.close()

