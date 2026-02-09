#Acces Item Dictionaries
thisdict = {
    "nama":"sheila",
    "umur": 21,
    "jurusan":"ilmu komputer"
}
x = thisdict["nama"]
print(x)

#get() ini akan mengeluarkan nilainya sesuai dengan kuncinya
x = thisdict.get("nama")
print(x)

#keys()    ini akan mengeluarkan kunci item
x = thisdict.keys()
print(x)

data = {
    "nama":"jenny",
    "nim" : 12345,
    "jurusan":"piskologi"
}

x = data.keys()
print(x)

data["fakultas"] = "psikologi"  #menambahkan item 
print(x)

#values()   untuk mengeluarkan nilai item
murid = {
    "nama":"salsa",
    "kelas" : 10,
    "jenis kelamin": "perempuan"
}

x = murid.values()
print(x)

murid["kelas"] = 11     #merubah nilai item
print(x)

#items() akan menampilkan setiap item dalam dictionary
x = murid.items()
print(x)