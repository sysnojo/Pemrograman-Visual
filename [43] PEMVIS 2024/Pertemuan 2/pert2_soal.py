print("\033c")
import numpy as np
import matplotlib.pyplot as plt

ya=200; xa = 100
yb=1000; xb = 100
yc=600; xc = 600
yd=600; xd = 200

pd = int(8); pr = 255; pg = 0; pb = 255
lw = int(8); lr = 255; lg = 0; lb = 255

col = int(1200)
row = int(1200)
print('col, row =', col, ',', row)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    Gambar = np.zeros(shape=(row, col, 3), dtype = np.uint8)
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2-y1
    dx = x2-x1

    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) * 2 + (j - y1) * 2) < hw ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) * 2 + (j - y2) * 2) < hw ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)
            x = i
            y = j
            print("x, y =", x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) * 2 + (j - y) * 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j-y1) + x1)
            x = i
            y = j
            print("x, y =", x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if ((i - x) * 2 + (j - y) * 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    return Gambar

ya=200; xa = 100
yb=1000; xb = 100
yc=600; xc = 600
yd=600; xd = 200

hasil = buat_garis(ya, xa,yb,xb,pd,lw,pr,pg,pb,lr,lg,lb)

plt.figure()
plt.imshow(hasil)
plt.show()