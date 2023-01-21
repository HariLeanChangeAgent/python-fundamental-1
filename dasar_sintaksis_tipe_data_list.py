daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
print('tampilkan variable daftar_buku')
print(daftar_buku)

print('\nproses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\ntampilkan isi daftar_buku pada index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print(('\ntampilkan dengan for in range'))
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'kenji volume 2', -313, 3.14]
print(('\ntampilkan dengan for in range, dimana tipe data tiap elemen berbeda2'))
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nkembalikan nilai awal daftar_buku')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
print('\ntambahkan 1 buku baru')
daftar_buku.append('dunia matematika kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nclear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nganti elemen pertama')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
daftar_buku[0] = 'eight habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nambil elemen ke-2')
daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nbuku yang diambil tadi')
print(buku)

print('\npop -2')
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

