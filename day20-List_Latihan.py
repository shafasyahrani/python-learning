#PROGRAM TO DO LIST
#program sederhana untuk menambahkan, menghapus, dan melihat to do list 

mylist = []       #list untuk menyimpan tugas

while True :
    #Menampilkan menu utama
    print("\n=====PROGRAM TO DO LIST=====")
    print("1. To Do List saat ini.")
    print("2. Menambahkan To Do List.")
    print("3. Reset To Do List.")
    print("4. Keluar.")

    #meminta input pilihan user
    input_user = int(input("Apa yang akan anda lakukan (1/2/3/4): "))

    if input_user == 1:
        #cek apakah list kosong
        if not mylist:
            print("\nKamu belum ada tugas nih\n")
        else:
            #menampilkan daftar to do list yg ada
            print("\n=====Daftar To Do List=====")
            i = 1
            for x in mylist:
                print(f"{i}. {x}")
                i += 1

    elif input_user == 2:
        #menambahkan tugas baru ke dalam list
        add_user = input("Tambahkan To DO List hari ini: ")
        mylist.append(add_user)

        #menampilkan to do list 
        print("\n=====Daftar To Do List=====")
        i = 1
        for x in mylist:
            print(f"{i}. {x}")
            i += 1

    elif input_user == 3:
        #menhapus seluruh isi to do list
        mylist.clear()
        print("\nDaftar To DO List terhapus")

    elif input_user == 4:
        #keluar dari program
        break