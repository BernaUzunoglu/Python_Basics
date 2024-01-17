import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(-10,9,20)
y = x ** 3
z = x ** 2

''' # ----------- Tek figure üzerine iki tane ayrı grafik çizimi  - x-y çizgileri kendi değerleri var -----------------
#X-Y kordinat sistemini oluşturan yapı figure
figure = plt.figure()#bir tablo içine bir şeyler yazmak, çizmek için figure tanımlıyoruz
axes_cube = figure.add_axes([0.1,0.1,0.9,0.9])#figüre akses ekleyip koordinatlarını belirler.(0-1) arası değerler alır
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")


axes_square = figure.add_axes([0.18,0.7,0.25,0.25])
axes_square.plot(x,z,'r')
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Square")

'''
'''
# ----------- Aynı axez üzerine iki tane  grafik çizimi x-y çizgileri ortak -----------------
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
#çizgilerin bilgilerinin, etiketlerinin yazdığı kısım legend loc ile 1 verirsek sağ tarafda
axes.legend(loc = 1) # yazarak çizgilerin ne anlama geldiğini görsel üzerinde gösterebiliriz 
'''

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(5,5))#figsize() figürü boyutlandırma 

axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure2.pdf")

plt.show()