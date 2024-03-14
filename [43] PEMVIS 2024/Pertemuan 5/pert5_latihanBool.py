import os
import time as tm

def main():
    ans = input("Siap untuk memainkan permainan? [y/N]: ")
    if ans.lower() == 'y':
        count = 0
        charDat = "a$u(9jkd/?"
        os.system('cls' if os.name == 'nt' else 'clear')  # Menghapus layar terminal
        print("INGAT KARAKTER-KARAKTER INI!")
        print(charDat)
        tm.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')  # Menghapus layar terminal
        print("INGAT KARAKTER-KARAKTER INI!")
        ansChar = input("Ketikkan karakter-karakter tersebut (10 Karakter): ")
        ansChar = ansChar[:10]  # Hanya mengambil 10 karakter pertama
        if len(ansChar) != len(charDat):
            print("Jumlah karakter yang Anda masukkan tidak sama dengan jumlah karakter yang harus diingat.")
            return
        for i in range(len(charDat)):
            if i < len(ansChar):  # Pastikan kita tidak melebihi panjang karakter yang dimasukkan oleh pengguna
                if ansChar[i] != charDat[i]:
                    charDat = charDat[:i] + 'x' + charDat[i+1:]
                else:
                    count += 1

        print(f"Koreksi: {charDat}")
        print(f"Anda berhasil mendapatkan {count}/{len(charDat)}")

if __name__ == "__main__":
    main()
