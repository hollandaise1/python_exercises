## Week 1

# creates a file object
fileref = open("travel_plans.txt", "r")

# read the content - the content will be read as a one single string
contents = fileref.read()
print(contents[:100])
print(len(contents))

# readlines - it return a list insead of a single string, each line is a single string
lines = fileref.readlines()
print(len(lines))

for line in lines:
    """reiterate from the lines with stripping the extra line"""
    print(line.strip()) 
    
# close the file
fileref.close()
