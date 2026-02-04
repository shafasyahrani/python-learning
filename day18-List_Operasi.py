#Operasi Pada List

#ADD LIST ITEMS
#append() menambahkan item di akhir list

thislist = ["Yonsei","NUS","NTU"]
thislist.append("SNU")
print(thislist)

#insert() menambahkan item dengan spesifikasi index
thislist = ["Korea","USA","Singapore"]
thislist.insert(1,"Indonesia")
print(thislist)

#extend() menambahkan list baru di suatu list
#extend juga bisa menambahkan jenis list lain seperti tuple, sets, dictionaries, dll.
thislist = ["hijau","merah","pink"]
mylist = ["kuning","purple","blue"]
thislist.extend(mylist)
print(thislist)

thislist = ["makan","tidur","belajar"]
todolist = ("nyuci","olahraga")
thislist.extend(todolist)
print(thislist)

#REMOVE ITEMS LIST
#remove() mengapus spesifik item dalam list menggunakan value 
thislist = ["apel","jambu","melon","anggur"]
thislist.remove("jambu")
print(thislist)

#jika terdapat 2 item yang sama dan di remove() maka yang terhapus adalah item urutan awal di list
thislist = ["pisang","duku","alpukat","pisang"]
thislist.remove("pisang")
print(thislist)

#pop() mengapus item dengan spesifikasi index
thislist = ["Jenny","Rose","Jisoo","Lisa","Nana"]
thislist.pop(4)
print(thislist)

thislist = ["Reid","Morgan","Hotch","Elle","Jane"]
thislist.pop()  #menghapus item terakhir 
print(thislist)

#del() menghapus item berdasarkan spesifikasi index 
thislist = ["Python","Java","C++","HTML"]
del thislist[3]
print(thislist)

thislist = ["Python","Java","C++"]
del thislist  #menghapus seluruh list

#clear() menghapus isi list, list masih ada namun isinya kosong
thislist = ["eyes","nose","mouth","ear"]
thislist.clear()
print(thislist)

#sort() mengurutkan item list
mylist = ["blue","green","pink","black"]
mylist.sort()
print(mylist)

#reverse() mengurutkan item list dari terbesar ke terkecil
mylist = [1, 5, 4, 6]
mylist.sort(reverse=True)
print(mylist)

