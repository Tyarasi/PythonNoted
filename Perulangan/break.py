for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

print('-- Antoher World --')
for huruf in 'Nico Bang':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))