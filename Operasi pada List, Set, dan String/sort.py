kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)

# Anda dapat membalikkan urutan dengan cara berikut

kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)

print(kendaraan)

# Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya.

# urutan = ['World', 1, 2, 'Indonesia', 3]
# urutan.sort()

# print(urutan)

# Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).

kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)
