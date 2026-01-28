#PROGEAM MELIHAT POLA 

while True:  #ini akan terus menerus berulang sampai user pilih 3
    print("1. Pola Bintang")
    print("2. Pola huruf")
    print("3. Keluar")

    pilih = int(input("Pilih (1/2/3): "))

    if pilih == 1:
        for i in range(1,20,3):
            print("*"*i)
    elif pilih == 2:
        for i in range(1,10):
            for j in range(1, i+1):
                print(j, end="")
            print()
    elif pilih == 3:
        print("Program Selesai")
        break
    else:
        print("Masukkan pilihan yang sesuai")
    
