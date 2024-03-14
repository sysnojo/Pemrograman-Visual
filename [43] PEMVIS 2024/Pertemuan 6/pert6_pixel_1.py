# case menentukan warna pixel berdasarkan posisi pixel dengan kondisi dan komparasi

# masukkan posisi pixel pada layar (nomor baris)
pixel_row = 100

rowmax = int(1079)
batas1 = int(0.5 * rowmax)

print("batas1: ", batas1)
print("Posisi pixel berada pada baris ke-", pixel_row)
if pixel_row < batas1:
    print("Warnai pixel merah.")
if pixel_row == batas1:
    print("Warnai pixel hitam.")
if pixel_row > batas1:
    print("Warnai pixel putih.")
if pixel_row <= batas1:
    print("Warnai pixel kuning.")
if pixel_row > batas1:
    print("Warnai pixel ungu.")
