#Pass Statement
#if statement tidak bisa kosong -> error
#untuk itu digunakan pass agar if statement tidak error

umur = 20

if umur == 20: 
    pass #ini tidak akan mengeksekusi apapun

#Why Use Pass?
#1. saat masih biki kerangka atau struktur program (belum tahu isinya apa namun program tetap bisa dijalankan)
#2. saat ingin mengabaikan kondisi tertentu
#3. saat buat function atau di dalam loop

#misal saat sedang membuat kerangka program
umur = 16

if umur > 18:
    pass
else:
    print("Kamu lolos")


#pass multiple conditions
nilai = 76

if nilai < 0:
    pass
elif nilai == 0:
    pass
else:
    print("Nilai Positif")