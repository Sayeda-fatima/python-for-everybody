#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
words_time=list()
words=list()
for line in handle:
    if line.startswith('From') and not line.startswith('From:'):
        #continue
    	line=line.split()
    	words_time.append(line[5])
for word in words_time:
    word=word.split(':')
    words.append(word[0])


count=dict()
for word in words:
    count[word]=count.get(word,0)+1

for k,v in sorted(count.items()):
    print(k,v)
