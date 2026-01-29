#indexing (list bisa di akses menggunakan index yang di mulai dari index 0 sebagai item pertama)

list_country = ["Indonesia","Malaysia","India","Thailand"]
print(list_country[1]) #akan mengeluarkan Malaysia sbg index pertama

# -1 dalam indexing akan mengeluarkan list paling akhir dan -2 list kedua paling akhir
list_fruits = ["grape","mango","apple"]
print(list_fruits[-1])

#range index
list_foods = ["Noodle","Pasta","Spaggeti","Fries","Taco","Burger"]
print(list_foods[2:5]) # mengeluarkan index ke 2 sampai ke 5 namun item ke 5 TIDAK ikut\

list_names = ["Bree","Susan","Gabriel","Lynette","Katherine"]
print(list_names[:4]) #menghasilkan index awal sampai index ke 3

list_drinks = ["coffe", "tea","Water","Smoothies","soda"]
print(list_drinks[2:]) #menghasilkan index ke 2 sampai akhir

list_capital = ["New York","Jakarta","Berlin","Tokyo","Denver"]
print(list_capital[-4:-2]) #menghasilkan item Jakarta dan Berlin

#Cek apakah item ada dalam list
list_animal = ["rabbit","monkey","fish","bird"]
if "bird" in list_animal :
    print("Ya bird berada dalam list")
