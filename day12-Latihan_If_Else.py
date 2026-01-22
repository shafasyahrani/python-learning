#Program Diskon Restaurant


user_input = float(input("Total Belanja: "))

if user_input >= 50000 and user_input < 100000:
    bayar = user_input - (user_input * (0.1))
    print("Anda Mendapatkan diskon 10%, anda hanya perlu membayar: ", bayar)
elif user_input >= 100000 and user_input < 200000:
    bayar = user_input - (user_input * (0.2))
    print("Anda Mendapatkan diskon 20%, anda hanya perlu membayar: ", bayar)
elif user_input >= 200000 and user_input < 500000:
    bayar = user_input - (user_input * (0.3))
    print("Anda Mendapatkan diskon 30%, anda hanya perlu membayar: ", bayar)
elif user_input >=500000:
    bayar = user_input - (user_input * (0.5))
    print("Anda Mendapatkan diskon 50%, anda hanya perlu membayar: ", bayar) 
else:
    print("Maaf anda belum mendapatkan diskon")