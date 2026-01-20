#Format String
#di format String bisa menggabungkan strings dan number dengan menggunakan f" "

#contoh umum
nama = "Sheila"
sapa = f"hello {nama}, Apa kabar?"
print(sapa)

#angka
angka = 22
kata = f"Jenny berumur {angka} tahun ini"
print(kata)

#modifier dengan angka

#melakukan operasi aritmatika dalam place holder
kata2 = f"harga buku ini adalah {angka * 1000}" 
print(kata2)

kata3 = f"harga pulpen itu {angka:.2f}"
print(kata3)

kata4 = f"Total semuanya adalah {20*1000} rupiah"
print(kata4)

#memformat persen
persen = 0.5
format_persen = f"persen = {persen:.2%}"
print(format_persen)

#menambahkan koma pada angka ribuan/jutaan
ribuan = 22000
format_ribuan = f"{ribuan:,} orang datang hari ini"
print(format_ribuan)

#boolean
boolean = True
format_str = f"Hasil boolean adalah :{boolean}"
print(format_str)
