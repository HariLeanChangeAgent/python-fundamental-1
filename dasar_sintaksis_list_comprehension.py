print('\nperintah del')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
del daftar_buku[0:1] # start:end
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nperintah del dengan list comprehension start')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
del daftar_buku[0::2] # start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmembuat list baru')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    
print('\nmembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru')
daftar_buku = ['seven habits','how to influence people','first things first', 'sdx']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmembuat list baru dengan comprehension : ganjil')
daftar_buku = ['1 seven habits','2 how to influence people','3 first things first', '4 sdx']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension : genap')
daftar_buku = ['1 seven habits','2 how to influence people','3 first things first', '4 sdx']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension : buang diujung')
daftar_buku = ['1 seven habits','2 how to influence people','3 first things first', '4 sdx']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nmembuat list baru dengan comprehension : ganjil')
daftar_buku = ['1 seven habits','2 how to influence people','3 first things first', '4 sdx']
print(daftar_buku[0::2])
