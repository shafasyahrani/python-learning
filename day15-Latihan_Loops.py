#

tugas = []

while True:
    print("1.Tambah Tugas")
    print("2.Lihat Semua Tugas")
    print("3.Reset Tugas")
    print("4.Keluar")

    pilih = int(input("Pilih: "))

    if pilih == 1:
        tugas = input("Masukkan Tugas: ")
        print("1. ", tugas)
        print("="*10)
    elif pilih == 2:
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            print("/nDaftar Tugas")
            for i in tugas:
                print(1. )


