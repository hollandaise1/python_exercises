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

# prob 1: The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
# Find the total number of characters in the file and save to the variable num.
# creates a file object
fileref = open("travel_plans.txt", "r")

# read the content - the content will be read as a one single string
contents = fileref.read()
num = len(contents)
print(num)

# prob 2: We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
# Find the total number of words in the file and assign this value to the variable num_words.
fname = "emotion_words.txt"
num_words = 0

with open(fname, 'r') as fileref:
    lines = fileref.readlines()
    for lin in lines:
        num_words += len(lin.split()) #split it will give us 48, if using strip it returns 373
    print(num_words)

    
# prob 3: Assign to the variable num_lines the number of lines in the file school_prompt.txt.
fname = "school_prompt.txt"

with open(fname, 'r') as fileref:
    lines = fileref.readlines()
    num_lines = len(lines)
    print(num_lines)


# prob 4: Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.
fileref = open('school_prompt.txt','r')
beginning_chars = fileref.read()[:30]
print(beginning_chars)


# prob 5: Using the file school_prompt.txt, assign the third word of every line to a list called three.
fname = "school_prompt.txt"

with open(fname, 'r') as fileref:
    three = [line.split()[2] for line in fileref]
    print(three) 

    
# prob 6: Create a list called emotions that contains the first word of every line in emotion_words.txt.
fname = 'emotion_words.txt'

with open(fname, 'r') as file:
    lines = file.readlines()
    emotions = []
    for lin in lines:
        emotions.append(lin.split()[0])
    print(emotions)

    
# prob 7: Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.
fname = 'travel_plans.txt'

with open(fname, 'r') as file:
    first_chars = file.read(33) # parethesis is to read the first characters
    print(first_chars)
    
    
# prob 8: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
fname = 'school_prompt.txt'

with open(fname, 'r') as fname:
    p_words = []
    words = fname.read().split() # split is able to split by , or \n etc
    p_words = [word for word in words if "p" in word]
    print(p_words)

# bonus: Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices 
# as well as some other financial indicators, including the “Long Term Interest Rate”, which is interest rate paid on 10-year U.S. government bonds.
# Write a program that computes the average closing price (the second column, labeled SP500) and the highest long-term interest rate. 
# Both should be computed only for the period from June 2016 through May 2017. Save the results in the variables mean_SP and max_interest.
begin_date = "6/1/2016"
end_date = "5/1/2017"
SP = 'SP500'
Rate = 'Long Interest Rate'

with open('SP500.txt','r') as f:
    h = f.readline()
    line = f.readlines()
hlist = h.split(',')
sums = []
lst =[]
in_date = 0
for l in line:
    lina = l.split(',')
    now_date = lina[hlist.index('Date')]
    if (now_date == begin_date) or (in_date == 1):
        sums.append(float(lina[hlist.index(SP)]))
        lst.append(float(lina[hlist.index(Rate)]))
        in_date = (0 if (now_date == end_date) else 1)
mean_SP = sum(sums) / len(sums)
max_interest =  max(lst)

# 0.5, 2.49
