#Loop Dictionaries

thisdict = {
    "nama":"Jenny",
    "nim":12345,
    "jurusan":"psikologi"
}

#print semua nama kunci (keys)
for x in thisdict:
    print(x)

for x in thisdict.keys():   #menggunakan keys()
    print(x)

print("="*5)

#print semua nilai (values)
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():     #menggunakan values()
    print(x)

print("="*5)

#print semua item dalam dictionary
for x, y in thisdict.items():
    print(x,y)