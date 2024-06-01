import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menghitung persamaan garis lurus antara dua titik (x1, y1) dan (x2, y2)
def hitung_persamaan_garis(x1, y1, x2, y2):
    def persamaan(x):
        m = (y2 - y1) / (x2 - x1)  # Gradien garis
        y = m * (x - x1) + y1  # Persamaan garis y = mx + c
        return y
    return persamaan

# Fungsi untuk menghitung persamaan garis vertikal antara dua titik (x1, y1) dan (x2, y2)
def garis_vertikal(x1, y1, x2, y2):
    def persamaan(y):
        m = (x2 - x1) / (y2 - y1)  # Gradien garis vertikal
        x = m * (y - y1) + x1  # Persamaan garis x = my + c
        return x
    return persamaan

# Fungsi untuk menggambar lingkaran pada koordinat (x, y) dengan radius tertentu
def gambar_lingkaran(x, y, radius, warna, gambar, height, width):
    for j in range(max(int(y - radius), 0), min(int(y + radius), height)):
        for i in range(max(int(x - radius), 0), min(int(x + radius), width)):
            if (i - x)**2 + (j - y)**2 < radius**2:
                gambar[j, i] = warna
    return gambar

# Ukuran radius lingkaran yang akan dibuat
radius = 10

# Ukuran canvas
canvas_width = 1920
canvas_height = 1200

# Membuat canvas berwarna hitam dengan ukuran yang ditentukan
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# Titik-titik untuk berbagai garis
titik_a = (100, 200)
titik_b = (1800, 1000)
titik_c = (100, 1000)
titik_d = (1800, 1000)
titik_e = (100, 200)
titik_f = (100, 1000)
titik_g = (100, 800)
titik_h = (300, 800)
titik_i = (300, 800)
titik_j = (300, 1000)

# Titik-titik untuk 1/4 lingkaran
pusat_x = 1300
pusat_y = 800
radius_lingkaran = 200

# Menggambar lingkaran pada titik-titik tujuan
semua_titik = [titik_a, titik_b, titik_c, titik_d, titik_e, titik_f, titik_g, titik_h, titik_i, titik_j]
warna_lingkaran = [213, 85, 239]

for titik in semua_titik:
    gambar_lingkaran(titik[0], titik[1], 20, warna_lingkaran, canvas, canvas_height, canvas_width)

# Menggambar garis 1
persamaan_garis = hitung_persamaan_garis(titik_a[0], titik_a[1], titik_b[0], titik_b[1])
for x in range(min(titik_a[0] + 50, canvas_width), max(titik_b[0] - 50, 0), -1):
    y = persamaan_garis(x)
    warna = [255, int(255 * (1 - x / canvas_width)), 255]  # Warna RGB yang berubah sesuai posisi x
    gambar_lingkaran(x, int(y), radius, warna, canvas, canvas_height, canvas_width)

# Menggambar garis 2
persamaan_garis = hitung_persamaan_garis(titik_c[0], titik_c[1], titik_d[0], titik_d[1])
for x in range(min(titik_c[0] + 50, canvas_width), max(titik_d[0] - 50, 0), -1):
    y = persamaan_garis(x)
    warna = [int(255 * x / canvas_width), 255, 255]  # Warna RGB yang berubah sesuai posisi x
    gambar_lingkaran(x, int(y), radius, warna, canvas, canvas_height, canvas_width)

# Menggambar garis 3
persamaan_garis_vertikal = garis_vertikal(titik_e[0], titik_e[1], titik_f[0], titik_f[1])
for y in range(max(titik_e[1] - 50, 0), min(titik_f[1] + 50, canvas_height)):
    x = persamaan_garis_vertikal(y)
    warna = [255, 255, int(255 * (1 - y / canvas_height))]  # Warna RGB yang berubah sesuai posisi y
    gambar_lingkaran(int(x), y, radius, warna, canvas, canvas_height, canvas_width)

# Menggambar garis 4
persamaan_garis = hitung_persamaan_garis(titik_g[0], titik_g[1], titik_h[0], titik_h[1])
for x in range(min(titik_g[0] + 50, canvas_width), max(titik_h[0] - 50, 0), -1):
    y = persamaan_garis(x)
    warna = [int(255 * x / canvas_width), 255, 255]  # Warna RGB yang berubah sesuai posisi x
    gambar_lingkaran(x, int(y), radius, warna, canvas, canvas_height, canvas_width)

# Menggambar garis 5
persamaan_garis_vertikal = garis_vertikal(titik_i[0], titik_i[1], titik_j[0], titik_j[1])
for y in range(max(titik_i[1], 0), min(titik_j[1], canvas_height)):
    x = persamaan_garis_vertikal(y)
    warna = [255, int(255 * (1 - y / canvas_height)), 255]  # Warna RGB yang berubah sesuai posisi y
    gambar_lingkaran(int(x), y, radius, warna, canvas, canvas_height, canvas_width)

# Menggambar 1/4 lingkaran
for y in range(pusat_y, pusat_y + radius_lingkaran + 1):
    for x in range(pusat_x - radius_lingkaran, pusat_x + 1):
        if (x - pusat_x)**2 + (y - pusat_y)**2 <= radius_lingkaran**2:
            canvas[y, x] = [255, 255, 255]  # Warna putih

# Menampilkan gambar
plt.figure(figsize=(20, 20))
plt.imshow(canvas)
plt.title('Gambar Garis dan 1/4 Lingkaran')
plt.show()
