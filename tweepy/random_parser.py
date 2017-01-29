file = open('twitterdata.txt','r')

counter = 0
totalcount = 0

for eachline in file:
     if eachline[0].isnumeric():
        print("Test")
        counter += 1
        totalcount += counter
     else:
        print("Not in code")
