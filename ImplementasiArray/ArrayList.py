"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""

var_array = [i for i in range(101)]

total = 0
count = 0

for element in var_array:
    total += element
    count += 1

if count > 0:
    result = total / count
    print("Nilai Rata rata", result)
else:
    print("Nilai Array Kosong / tidak ada")


