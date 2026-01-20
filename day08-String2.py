#Concetente String (menggabungkan string)
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#len (menghitung panjang string)
panjang = len(c)
print("panjang string adalah ",panjang)

#Check String (mengecek kata yang ada dengan (in) -> True/False) 
kata = "Makan Bergizi Gratis"
print("Gratis" in kata)

txt = "Pendidikan Gratis"
if "Pendidikan" in txt :
    print("Mantap")

#check if NOT (mengecek apakah kata tidak ada di dalam string (not))
lagu = "My heart will go on"
print("Celine" not in lagu)

nama = "Celine Dion"
if "Beyonce" not in nama :
    print("Yes")

#indexing
print("index ke- 0: " + nama[0])
print("index ke- 1: " + nama[1])
print("index ke- (-1): " + nama[-1]) #indexing dari belakang
print("index ke- (3,5): " + nama[3:5])
print("index ke- (7,11): " + nama[7:11])
