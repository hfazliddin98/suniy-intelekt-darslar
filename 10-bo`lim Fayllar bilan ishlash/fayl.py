# fayl = 'fayllar/chipta.csv'
# with open(fayl) as file:
#     for line in file:
#         print(line)
fayl = 'fayllar/salom.doc'
ism = 'Ali'
familya = 'Aliyev'
with open(fayl, 'w') as file:
    file.write('asalomu alaykum\n' + ism)

with open(fayl) as file:
    for line in file:  
        print(line)      