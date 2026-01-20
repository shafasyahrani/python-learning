#Login dan Menentukkan nilai Lulus

print("===ELEARNING===\n")

#sistem login
print("LOGIN")
username = "admin"
password = "12345"

username_login = input("Masukkan username:")
password_login = input("Masukkan password:")

y = username == username_login
x = password == password_login
z = y and x

print("Login Berhasil :", z)
