filePath = 'test.txt'

# Open
with open(filePath, 'r') as myFile:
    print(myFile.read())

# Append
with open(filePath, 'a') as myFile:
     myFile.write('\nFourth Line')

# Write
with open(filePath, 'w') as myFile:
    myFile.write('New line')