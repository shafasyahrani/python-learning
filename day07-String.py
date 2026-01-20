#Pengenalan String
#String ditandai dengan ' atau "

nama = "jenny Blackpink" #double quote
asal = 'Korea Selatan' #single qoute

print(nama, 'dari', asal)

#Multiline String
data = """ Data adalah kumpulan fakta, angka, simbol, atau informasi
mentah yang diperoleh dari pengamatan atau penelitian, yang dapat diolah menjadi
informasi bermakna untuk pengambilan keputusan, analisis, dan pemahaman lebih lanjut,
dan dapat berupa data primer (langsung) atau sekunder (dari sumber lain), 
kuantitatif (angka) atau kualitatif (deskriptif), serta internal (dari dalam) atau 
eksternal (dari luar)."""

#Modify String

#Upper Case (membuat huruf menjadi besar)
a = "blackpink"
print(a.upper())

#Lower Case (membuat huruf menjadi kecil)
a = "Ariana Grande"
print(a.lower())

#Remove whitespace (menghilangkan spasi kosong di awal/akhir teks)
a = " Taylor Swift "
print(a.strip())

#Split Sting (memecahkan teks menjadi beberapa bagian)
a = "Musik membuat senang"
print(a.split())

#Backslash \\
print("File ada di c:\\Users\\data")

#Newline \n (membuat baris baru)
print("halo\napakabar?")

#Tab \t 
print("Nama:\t Shafa")
print("Umur:\t 21")

#tanda \' atau \" (tanda kutip di dalam string)
print('Dia berkata: \'aku akan lakukan itu\'')

#Raw String (membaca teks apa adanya bukan sebagai perintah)
print(r'C:\newfolder')
