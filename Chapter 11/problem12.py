import re
name = input("Enter file:")
if len(name) < 1:
    name = "regular-expression.txt"
handle = open(name)
sum=0
number=list()
for line in handle:
    #line=line.rstrip()
    numbers=re.findall('[0-9]+', line)
    #print(y)
    if not numbers: continue
    for number in numbers:
        sum+=int(number)

print(sum)
