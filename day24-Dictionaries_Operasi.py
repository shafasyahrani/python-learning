#change items

#Change values
thisdict = {
    "fruit":"pisang",
    "color":"kuning",
    "jumlah": 10
}
thisdict["jumlah"] = 15
print(thisdict)

#Adding Items
thisdict = {
    "buah":"anggur",
    "warna":"ungu",
    "jumlah": 5
}
thisdict["bentuk"] = "bulat"
print(thisdict)

#update() 
buahan = {
    "buah":"apel",
    "warna":"merah",
    "jumlah": 5
}
buahan.update({"jumlah":10})
print(buahan)

#Remove Items
#pop() menghapus item dengan speksifikasi kunci
thisdict ={
    "brand":"ford",
    "model":"mustang",
    "year": 1964 
}
thisdict.pop("model")
print(thisdict)

#popitem() menghapus item terakhir yang dimasukkan
thisdict ={
    "brand":"ford",
    "model":"mustang",
    "year": 1964 
}
thisdict.popitem()
print(thisdict)

#del menghapus dengan spesifikasi kunci item
thisdict ={
    "brand":"ford",
    "model":"mustang",
    "year": 1964 
}
del thisdict["model"]
print(thisdict)

#del dengan menghapus seluruh dictionary
thisdict ={
    "brand":"ford",
    "model":"mustang",
    "year": 1964 
}
del thisdict

#clear() mengosongkan dictionary
thisdict ={
    "brand":"ford",
    "model":"mustang",
    "year": 1964 
}
thisdict.clear()
print(thisdict)



