#Case 1
print("Case 1")
#Data Bertipe Boolean yang Kita Deklarasikan (Cara Standar)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("==========================")

#Case 2
print("Case 2")
#Data Bertipe Boolean Dalam Berbagai Konteks
#Terdekat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
print(3>2)
print(3+2==5)
print("==========================")

#Case 3
print("Case 3")
#Data Bertipe Boolean Dalam Berbagai Konteks
#Terdekat Dengan Sendirinya oleh Komputer tanpa Deklarasi.
Penghasilan = 2800000
PenghasilanTanpaPajak = 4000000

if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar =0 
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar =0.1 * Penghasilan

print("Pajak yang harus Anda bayar: Rp ", PajakYangHarusDibayar)

# PART 2
print("Case 4")
a = 3
b = "Ini data string"
c = ("laptop", "buku", "ballpen")
d = ["laptop", "buku", "ballpen"]
e = {"laptop":"asus", "buku":"buku_teks", "ballpen":"arrow"}
f = {1, 2, 3, 4, 5}
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("===============================================")

# PART 3
print("Case 5")
a = 0
b = ""
c = ()
d = []
e = {}

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print("===============================================")

# Case 6
print("Case 6")
class myclass():
    def __len__(self):
        return 0;
print(bool(myclass()))
print("===============================================")

