# when the value of i becomes equal to ‘k‘, 
# the pass statement did nothing and hence the letter ‘k‘ is also printed. 
# Whereas in the case of continue statement, the continue statement transfers 
# the control to the begining of the loop, hence the letter k is not printed.

s = "geeks"
for i in s:
    if i == 'k':
        continue
        print('Continue executed')
    print(i)

# >> g
# >> e
# >> e
# >> s


s = "geeks"
for i in s:
    if i == 'k':
        pass
        print('Pass executed')
    print(i)
 
# >> g
# >> e
# >> e
# >> Pass executed
# >> k
# >> s


s = "geeks"
for i in s:
    if i == 'k':
        break
    print(i)
    
# >> g
# >> e
# >> e
