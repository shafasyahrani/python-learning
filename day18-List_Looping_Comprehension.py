#LOOP LIST
mylist = ["EXO","BTS","iKON","TXT"]
for x in mylist:
    print(x)

mylist = ["pisang","apel","mangga","leci"]
for x in  range (len(mylist)):  #loop dengan nomer index
    print(mylist[x])

mylist = ["soto","sop","gulai","opor"]
[print(x) for x in mylist]  #looping dengan list comprehension

#WHILE LOOP LIST
mylist = ["teknik","fisip","kedokteran","psikologi"]
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

#LIST COMPREHENSION
mylist = ["voli","basket","badminton","futsal"]
newlist = []

for x in mylist :
    if "a" in x:
        newlist.append(x)

print(newlist)

#newlist = [expression for item in iterable if condition == True]
#newlist = [x for x in fruits if "a" in x]

mylist = ["hijau","biru","ungu","merah"]
barulist = [x for x in mylist if "u" in x] #versi shortnya
print(barulist)
