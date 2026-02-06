#SETS
#tidak berurut, tidak dapat dirubah, unindex, dan item dalam set tidak dapat sama

myset = {"Kore","Indonesia","Japan"}
print(myset)

set1 = {"apel","pisang","anggur"}
set2 = {1,2,3,4}
set3 = {False, True}
set4 = {"apel",20,True}

#nilai 0 dan False adalah sama dan dianggap nilai duplikat dalam set
#nilai 1 dan True adalah sama dan dianggap nilai duplikat dalam set

myset = {"Shana",1,True}
print(myset)       #yang dihasilkan hanya angka 1 dan "Shana" saja

#menambahkan item dalam set
myset = {"hijau","ungu","kuning"}
myset.add("merah")
print(myset)

myset = {"Shana","Sheila","Shania"}
thisset = {20,22,25}
myset.update(thisset)
print(myset)

#sets dapat menghapus item dalam sets
#remove(), discard(), clear(), del

#for loop -> sets tidak berurutan maka jika sets loop akan menghasilkan nilai yang random tidak sesuai urutan

#join sets
#union() atau | ,update()  ->  menggabungkan 2 sets
set1 = {"brian","yuta","adrian"}
set2 = {"putri","paula","sheila"}
set3 = set1.union(set2)
print(set3)

set1 = {"apel","mangga","jeruk"}
set2 = {"pisang","anggur","jambu"}
set1.update(set2)
print(set1)

#intersection()  atau & -> hanya menghasilkan item yg sama dalam 2 sets
set1 = {"apel","mangga","anggur"}
set2 = {"anggur","jeruk","mangga"}
set3 = set1.intersection(set2)
print(set3)




