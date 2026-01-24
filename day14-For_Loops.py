# For Loop (perulangan)

buah = ["pisang", "anggur","mangga"]

for x in buah:
    print(x)

for x in "pisang":
    print(x) #akan menghasilkan perulangan huruf yang ada pada "pisang"

#Break Statement
#break bisa mengentikan perulangan sebelum mengulang semua list 

nama = ["Reid","Hotchner","Jennifer","Derek"]

for x in nama:
    print(x)
    if x == "Jennifer":
        break

#Continue Statement
#continue melewati iterasi yang terjadi dan lanjut ke perulangan berikutnya

print("\n===Criminal Mind Guys===")

for x in nama:
    if x == "Jennifer":
        continue #disini "Jennifer" dilewati
    print(x)

#Range Function
#range() fungsi untuk menghasilkan urutan angka dengan dimulai dari 0

for x in range(6):
    print(x)

print("="*5)

#akan menghasilkan output 1 - 5 TIDAK termasuk 6
for x in range(1,6):
    print(x)

print("="*5)

#akan menghasilkan pertambahan 3 dengan range 1 sampai 21
for x in range(1, 21, 3):
    print(x)

#Else in For loop 
#Else akan dijalan ketika loop selesai NORMAL (tanpa "break")

print("="*5)
for x in range(6):
    print(x)
else:
    print("Selesai!!")

#Nested Loop 
#ini adalah Loop didalam loop

warna = ["merah", "hijau", "ungu"]
buah = ["jambu","mangga","anggur"]

#ini akan menghasilkan 9 output dengan masing2 iterasi
for x in warna:
    for y in buah:
        print(x,y)
