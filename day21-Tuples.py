#TUPLES
#tupless adalah kumpulan yang terurut dan tidak dapat diubah

mytuples = ("makan","tidur","belajar")
print(mytuples)

mytuples = ("apel","mangga","pisang","apel") #item dalam tuples boleh sama
print(mytuples)

mytuples = ("hijau",)   #jika ingin mebuat satu item tuple gunakan ,
print(mytuples)

tuple1 = ("hijau","merah","kuning")
tuple2 = (7,4,5,3)
tuple3 = (True,False,True)
tuple4 = ("olahraga",22,True)

thistuples = ("apel","pisang","mangga")
print(thistuples[2])    #indexing

#tuples TIDAK dapat dirubah (ditambahkan, dihapus)
# thistuples[2] = ("jambu") -> tidak bisa dilakukan
# print(thistuples)

#alternatif menambahkan item pada tuples
#mengubah tuples menjadi list
print("="*5)

thistuples = ("Reid","Morgan","Hotchner")
thislist = list(thistuples)     #merubah tuple menjadi list
print(thistuples)
print(thislist)

thislist.append("Parentiss")    #menambahkan item pada list
print(thislist)

thistuples = tuple(thislist)    #merubah list menjadi tuple lagi
print(thistuples)


