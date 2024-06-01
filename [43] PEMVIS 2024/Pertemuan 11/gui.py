import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

# Fungsi untuk menambahkan data baru
def tambah_data():
    nama = simpledialog.askstring("Input", "Masukkan Nama:")
    if nama is None:  # Jika pengguna membatalkan input
        return
    usia = simpledialog.askinteger("Input", "Masukkan Usia:")
    if usia is None:
        return
    kota = simpledialog.askstring("Input", "Masukkan Kota Asal:")
    if kota is None:
        return
    
    data.append([nama, usia, kota])
    update_treeview()

# Fungsi untuk mengupdate tampilan treeview
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    for i, (nama, usia, kota) in enumerate(data):
        tree.insert('', 'end', iid=i, values=(nama, usia, kota))

root = tk.Tk()
root.title("Data Mahasiswa")

data = [
    ['Andi', 20, 'Surabaya'],
    ['Budi', 19, 'Bandung'],
    ['Citra', 21, 'Medan']
]

# Membuat frame utama
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# Membuat Treeview
tree = ttk.Treeview(frame, columns=("Nama", "Usia", "Kota"), show='headings')
tree.heading("Nama", text="Nama")
tree.heading("Usia", text="Usia")
tree.heading("Kota", text="Kota")
tree.pack(side='left', fill='x', expand=True)

# Membuat scrollbar untuk treeview
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscrollcommand=scrollbar.set)

# Tombol untuk menambahkan data
tambah_button = ttk.Button(root, text="Tambah Data", command=tambah_data)
tambah_button.pack(pady=5)

# Mengisi treeview dengan data awal
update_treeview()

# Menjalankan aplikasi
root.mainloop()
