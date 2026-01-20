#Width and Multiline

#Data
data_nama = "Ardinata Kusuma"
data_umur = 26
data_tinggi = 183
data_bb = 70

#String Standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, berat = {data_bb}"
print(5*"=" + "Data String" + 5*"=")
print(data_string)

#String Multiline dengan (\n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nberat = {data_bb}"
print(5*"=" + "Data String" + 5*"=")
print(data_string)

#String Multiline kutip (""")
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
berat = {data_bb}"""
print(5*"=" + "Data String" + 5*"=")
print(data_string)

#atur lebar
data_string = f"""
nama    = {data_nama:>5}
umur    = {data_umur:>2}
tinggi  = {data_tinggi:>3}
berat   = {data_bb:>2}
"""
print(5*"=" + "Data String" + 5*"=")
print(data_string)


