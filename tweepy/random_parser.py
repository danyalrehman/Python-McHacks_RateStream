from termcolor import colored

file = open('twitterdata.txt','r')

counter = 0
totalcount = 0

for eachline in file:
     if eachline[0].isnumeric():
        print(eachline)
        counter += 1
        totalcount += float(eachline)
     else:
        print("Not in code")

print("This is the Total Count: ", totalcount)
print("This is the Total Number of Posts: ", counter)
ratio = totalcount/counter

if ratio > 0:
   print("Normalized Ratio: ", colored(ratio, 'green'))
else:
   print("Normalized Ratio: ", colored(ratio, 'red'))

print("\n")
