#COPY LIST

#copy()
a = ["Shafa","Sheila","Jenny"]
b = a.copy()
print(a)
print(b)

print("===mengubah list yang di copy===")


a [0] = "Dilla"     #mengubah index-0 dari list a
print(a)
print(b)    #list b tidak akan ikut berubah karena menggunakan copy()

print("===mengubah list yang di copy===")

b [1] = "Sazkia"
print(a) 
print(b)

print("="*5)

#list() menduplikat list dengan list()
c = list(b)
print(c)

b [1] = "Rahma"
print(c)
print(b)