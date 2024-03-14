"""
Latihan Boolean

- ada 2 input (masukkan nilai) a dan b
- output (berupa print)
- cek dengan boolean apakah a lebih besar dari b?
- cek dengan boolean apakah b lebih besar dari a?
- cek dengan boolean apakah a sama dengan b?
- hitung ppn a sebesar 12% jika lebih dari 10000
- hitung ppn b sebesar 12% jika lebih dari 50000
- tambahkan kedua ppn a dan b, cek dengan boolean
- hapus a dan b, cek dengan boolean
"""
# input
a, b = map(int, input("Masukkan nilai a dan b [ex: 100000, 20000]: ").split(','))

# print input (output)
print(f"\nNilai a = {a}")
print(f"Nilai b = {b}")

# cek a > b
print(f"a > b = {a > b}")
        
# cek b > a
print(f"b > a = {b > a}")

# cek a == b
print(f"a == b -> {a == b}")

ppn_a = 0
ppn_b = 0

# hitung ppn a 12% jika lebih dari 10000
if (a > 10000):
    ppn_a = 12/100 * a
    a = a - ppn_a
    print(f"PPN a 12% = {ppn_a}")
    print(f"Total = {a}")

# hitung ppn b 12% jika lebih dari 50000
if (b > 50000):
    ppn_b = 12/100 * b
    b = b - ppn_b
    print(f"PPN b 12% = {ppn_b}")
    print(f"Total = {b}")

# tambahkan kedua ppn a dan b
hasil = ppn_a + ppn_b
# cek ppn dengan boolean
print(f"PPN A + PPN B = {hasil} -> {hasil != 0}")
# cek a dan b dengan boolean dihapus
del(a)
del(b)

cek = 'a' in locals() and 'b' in locals()
print(f"a dan b = {cek}")
    




