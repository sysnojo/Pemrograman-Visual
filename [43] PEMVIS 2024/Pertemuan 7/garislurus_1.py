import matplotlib.pyplot as plt
import numpy as np

# Ukuran radius lingkaran yang akan dibuat
radius = 10

# Ukuran canvas
canvas_width = 1000
canvas_height = 1000

# Membuat canvas berwarna hitam dengan ukuran yang ditentukan
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# Fungsi untuk menghitung persamaan garis lurus antara dua titik (x1, y1) dan (x2, y2)
def hitung_persamaan_garis(x1, y1, x2, y2):
    def persamaan(x):
        m = (y2 - y1) / (x2 - x1)  # Gradien garis
        y = m * (x - x1) + y1  # Persamaan garis y = mx + c
        return y
    return persamaan

# Fungsi untuk menggambar lingkaran pada koordinat (x, y) dengan radius tertentu
def gambar_lingkaran(x, y, radius, warna, gambar, height, width):
    for j in range(max(int(y - radius), 0), min(int(y + radius), height)):
        for i in range(max(int(x - radius), 0), min(int(x + radius), width)):
            if (i - x)**2 + (j - y)**2 < radius**2:
                gambar[j, i] = warna
    return gambar

# Titik awal dan akhir garis
titik_a = (100, 200)
titik_b = (800, 600)

# Menggambar lingkaran pada titik awal dan akhir
gambar_lingkaran(titik_a[0], titik_a[1], 20, [213, 85, 239], canvas, canvas_height, canvas_width)
gambar_lingkaran(titik_b[0], titik_b[1], 20, [155, 0, 186], canvas, canvas_height, canvas_width)

# Menghitung persamaan garis yang menghubungkan dua titik
persamaan_garis = hitung_persamaan_garis(titik_a[0], titik_a[1], titik_b[0], titik_b[1])

# Menggambar garis lurus dengan menggambar lingkaran kecil pada setiap titik sepanjang garis
for x in range(max(titik_a[0] - 50, 0), min(titik_b[0] + 50, canvas_width)):
    y = persamaan_garis(x)
    warna = [int(255 * x / canvas_width), 255, 255]  # Warna RGB yang berubah sesuai posisi x
    gambar_lingkaran(x, int(y), radius, warna, canvas, canvas_height, canvas_width)

# Menampilkan gambar
plt.figure(figsize=(20, 20))
plt.imshow(canvas)
plt.title('Garis Lurus antara Titik A dan Titik B')
plt.show()
