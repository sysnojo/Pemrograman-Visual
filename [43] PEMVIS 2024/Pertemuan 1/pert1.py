import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image
mpl.use('QtAgg')

col = int(1920)
row = int(1080 + 300)

# red
Rrow1 = int(0.25 * row)
Rrow2 = int(0.5 * row)
Rcol1 = int(0.25 * col)
Rcol2 = int(0.75 * col)

# Mrow1 = int(0.25 * row) + 1
# Mrow2 = int(0.5 * row) + 1
# Mcol1 = int(0.25 * col)
# Mcol2 = int(0.75 * col)
# white
Wrow1 = int(0.5 * row) + 1
Wrow2 = int(0.75 * row) + 1
Wcol1 = int(0.25 * col)
Wcol2 = int(0.75 * col)

Crow1 = int(0.75 * row) + 2
Crow2 = int(0.95 * row) + 2
Ccol1 = int(0.25 * col)
Ccol2 = int(0.75 * col)

Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
for i in range(Rrow1, Rrow2 + 1):
    for j in range(Rcol1, Rcol2):
        Gambar[i, j, 0] = 0
for i in range(Wrow1, Wrow2 + 1):
    for j in range(Wcol1, Wcol2):
        Gambar[i, j, 0] = 255
for i in range(Crow1, Crow2 + 3):
    for j in range(Ccol1, Ccol2):
        Gambar[i - 230, j, 1] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()

# N = 3 # Meshsize
# fps = 90 # frame per sec
# frn = 9# frame number of the animation

# x = np.linspace(-4,4,N+1)
# x, y = np.meshgrid(x, x)
# zarray = np.zeros((N+1, N+1, frn))

# f = lambda x,y,sig : 1/np.sqrt(sig)*np.exp(-(x**2+y**2)/sig**2)

# for i in range(frn):
#     zarray[:,:,i] = f(x,y,1.5+np.sin(i*2*np.pi/frn))

# def update_plot(frame_number, zarray, plot):
#     plot[0].remove()
#     plot[0] = ax.plot_surface(x, y, zarray[:,:,frame_number], cmap="magma")

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# plot = [ax.plot_surface(x, y, zarray[:,:,0], color='0.75', rstride=1, cstride=1)]
# ax.set_zlim(0,1.1)
# ani = animation.FuncAnimation(fig, update_plot, frn, fargs=(zarray, plot), interval=1000/fps)

# fig, ax = plt.subplots()
# # frame = 90
# t = np.linspace(0, 9, 100)
# g = -9.81
# v0 = 12
# z = g * t**2 / 2 + v0 * t

# v02 = 5
# z2 = g * t**2 / 2 + v02 * t

# scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
# line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
# ax.set(xlim=[0, ], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
# ax.legend()


# def update(frame):
#     # for each frame, update the data stored on each artist.
#     x = t[:frame]
#     y = z[:frame]
#     # update the scatter plot:
#     data = np.stack([x, y]).T
#     scat.set_offsets(data)
#     # update the line plot:
#     line2.set_xdata(t[:frame])
#     line2.set_ydata(z2[:frame])
#     return (scat, line2)


# ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=30)
plt.show()



# img = np.asarray(Image.open('C:/Users/ngrok/Documents/[43] PEMVIS 2024/imgTest2.jpg'))
# print(repr(img))

# cmapArr = np.array(['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 
# 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 
# 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 
# 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r'
# ])

# for i in cmapArr:
#     lum_img = img[:, :, 0]
#     imgplot = plt.imshow(lum_img, cmap=i)
#     plt.title(i)
#     plt.colorbar()
#     plt.show()
    

# X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
# Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

# fig, axs = plt.subplots(2, 2, layout='constrained')
# pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
# fig.colorbar(pc, ax=axs[0, 0])
# axs[0, 0].set_title('pcolormesh()')

# co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
# fig.colorbar(co, ax=axs[0, 1])
# axs[0, 1].set_title('contourf()')

# pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma',
#                           norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
# fig.colorbar(pc, ax=axs[1, 0], extend='both')
# axs[1, 0].set_title('imshow() with LogNorm()')

# pc = axs[1, 1].scatter(40, 30, c=90, cmap='RdBu_r')
# fig.colorbar(pc, ax=axs[1, 1], extend='both')
# axs[1, 1].set_title('scatter()')
