#Else
#else digunakan jika kondisi if tidak terpenuhi

nama = "Kayla"

if nama=="Shila" :
    print("Selamat datang Shila")
else :
    print("Data yang anda masukkan salah")

nilai = 50

if nilai >= 70 :
    print("Lulus!")
else :
    print("Tidak Lulus")


#Elif (else if)
#elif digunakan saat kamu punya lebih dari satu suatu kondisi

nama = "Cinta Laura"

if nama == "Agnez Monica":
    print("Selamat Agnez Monica")
elif nama == "Cinta Laura":
    print("Selamat Cinta Laura")
else :
    print("Maaf nama anda tidak ada di data")

print(20*'=')
nama = input("Princess siapakah kamu? ")
if nama == "Aurora":
    print("Hai putri tidur")
elif nama == "Snow White":
    print("Siapa teman-teman kurcacimu?")
elif nama == "Rapunzel":
    print("Bagaimana rasanya punya rambut yang panjang?")
elif nama == "Belle":
    print("Buku apa yang kamu baca hari ini?")
else :
    print("Maaf kamu bukan Princess")