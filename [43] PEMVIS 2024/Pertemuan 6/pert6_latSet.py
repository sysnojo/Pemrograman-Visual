import os

def menu():
    while True:
        os.system("cls")
        print("-- RESEP MEMBUAT MAKANAN --")
        print("===========================")
        print("1. Puding Strawberry")
        print("2. Puding Pisang")
        print("===========================")
        opt = int(input("Pilih Resep [1/2]: "))
        if opt == 1 or opt == 2: 
            proses_resep(opt)
            break

def proses_resep(pilihan):
    if pilihan == 1:
        # set bahan 
        set_bahan = {"Bubuk agar plain putih", "Strawberry", "Air", "Susu kental manis", "Gula Pasir"}
        # set quantity bahan dalam gram (kecuali air ml)
        set_q_bahan = {15, 100, 750, 80, 80} 
        
        # display
        while True:
            os.system("cls")
            print("----- BAHAN -----")
            print("=================")
            for idx, (b, q_b) in enumerate(zip(set_bahan, set_q_bahan), 1):
                print(f"{idx}. {b} - {q_b} {'ml' if 'Air' in b else 'gram'}")
            print(f"Jumlah bahan: {len(set_bahan)}")
            print("=================")
            ans = input("Siap untuk membuat puding strawberry? [Y/n]: ")
            if ans.lower() == 'y':
                break
        
        # membuat puding strawberry
        list_langkah = [
            "Ambil Strawberry dan Air dari bahan",
            "Masukkan Strawberry dan Air ke dalam blender",
            "Angkat Strawberry yang sudah di blender",
            "Bersihkan Blender",
            "Isi panci dengan Bubuk Agar, Gula Pasir, dan Susu Kental Manis"
        ]
        list_instruksi = [
            "instruksi: remove Strawberry Air from bahan",
            "instruksi: add Strawberry Air to blender",
            "instruksi: discard Strawberry from bahan",
            "instruksi: clear Blender",
        ]
        
        # set untuk blender
        set_blender = set()
        set_panci = set()
 
        for idx, (langkah, instruksi) in enumerate(zip(list_langkah, list_instruksi), 1):
            while True:
                os.system("cls")
                print("--- LANGKAH - LANGKAH ----")
                print("==========================")
                print(f"{idx}. {langkah}")
                print(instruksi)
                ans = input("Masukkan perintah: ")

                if "remove" in instruksi:
                    remove_items = [word for word in ans.split() if word.lower() not in ["remove", "from"]]
                    print("Set Bahan:", set_bahan)
                    for item in remove_items:
                        if item in set_bahan:
                            set_bahan.remove(item)
                    print("Set Bahan setelah dihapus:", set_bahan)

                elif "add" in instruksi:
                    add_items = [word for word in ans.split() if word.lower() not in ["add", "to", "set"]]
                    print("Set Blender:", set_blender)
                    for item in add_items:
                        set_blender.add(item)
                    print("Set Blender setelah ditambahkan:", set_blender)

                elif "discard" in instruksi:
                    discard_items = [word for word in ans.split() if word.lower() not in ["discard", "from", "bahan"]]
                    print("Set Blender:", set_blender)
                    for item in discard_items:
                        set_blender.discard(item)
                    print("Set Blender setelah discard:", set_blender)

                elif "clear" in instruksi:
                    set_blender.clear()
                    print("Set Blender setelah clear:", set_blender)

                else:
                    print("Perintah tidak valid. Silakan coba lagi.")

                lanjut = input("Lanjut ? [Y/n]: ")

                if lanjut.lower() == "y":
                    break

if __name__ == "__main__":
    menu()
