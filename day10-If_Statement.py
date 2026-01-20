# If Statement

#urutan if statement
# if kondisi : aksi

#1. if
#2. kondisi (contoh a > b)
#3. aksi (contoh : print("yes"))

#Example
nama = "Thomas"
if nama=="Thomas" :
    print("Congratulations Thomas!")

a = 20
b = 15
if a > b :
    print("Yes a lebih besar dari b")

#if statement harus menggunakan indentation untuk melakukan aksi
c = 5
d = 10
# if c < d :
# print("Yes")  #pernyataan ini akan error karena tidak ada indentation

if c < d :
    print("c lebih kecil dari d")

#Multiple Statements
umur = 15

if umur < 17 :
    print("Masih dibawah umur")
print("Belum cukup umur") #pernyataan ini tidak akan ikut pernyataan aksi di if karena tidak ada indentation

if umur < 17 :
    print("Belum cukup umur")
    print("Kamu belum punya KTP") #pernyataan ini akan ikut dalam aksi dalam if statement karena pakai indentation
