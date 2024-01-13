print( 'keterangan:')
bensin = int(input('masukkan harga bensin :'))
solar = int(input('masukkan harga solar:'))
pertamax = int(input('masukkan harga pertamax:'))

liter =int(input('masukkan liter:'))

print('hasil')
print('harga bensin     :Rp',bensin)
print('harga solar      :Rp',solar)
print('harga pertamax   :Rp',pertamax)

jumlah = 0

menu = int(input('masukkan pilihan :'))
match menu:
        case minyak if menu == 1:harga = bensin
        case minyak if menu == 2:harga = solar
        case minyak if menu == 3:harga = pertamax
        case _:print('tidak ada harga')

if harga != 0:
        jumlah = liter
        for i in range (jumlah) :
                jumlah += harga
                print('total prmbayaran :Rp.', jumlah)