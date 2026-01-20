#OPERASI LOGIKA

print("===LOGICAL OPERATORS===")

# AND OR NOT

#AND (akan bernilai TRUE apabila kedua statement bernilai TRUE)
print("===AND===")
a = False
b = True
c = a and b
print(a,'AND', b, '=', c)
a = True
b = True
c = a and b
print(a,'AND', b, '=', c)
a  = 5
print(a < 6 and a == 2 )

#OR (bernilai TRUE jika salah satu statement bernilai TRUE)
print("===OR===")
a = True
b = False
c = a or b
print(a,'OR', b, '=', c)
a = False
b = False
c = a or b
print(a,'OR', b, '=', c)
a = 10
print(a > 11 or a == 10)

#NOT (kebalikan dari nilai yang ada)
print("===NOT===")
a = True
b = not a
print('NOT', a, '=', b)
a = 20
print(not(5 > 8))
