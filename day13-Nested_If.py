#Nested If
#adalah ketika mempunyai if statements di dalam if statements.

#example
umur = 17
sim = True

if umur >= 17 :
    print("Kamu sudah cukup umur")
    if sim:  
        print("Kamu bisa berkendara")
    else:
        print("Kamu tidak bisa berkendara karena tidak ada sim")
#if dalam dijalankan ketika luar if berkondisi (umur >= 17)

#Multiple levels of nesting
tinggi = 170
toefl = 600
health = True

if tinggi >= 160:
    if toefl >= 600:
        if health:
            print("Selamat anda lolos rekrutmen")
        else:
            ("Silahkan coba lagi tahun depan")
    else:
        ("Maaf anda belum lolos")
else:
    ("Maaf anda belum memenuhi kriteria yang kami cari")

#Nested if Vs logical operators
#terkadang nested if bisa di simpulkan dengan menggunakan logical operators seperti AND
username = True
password = True

if username:
    if password:
        print("Kamu berhasil login")

if username and password:
    print("Kamu berhasil login")