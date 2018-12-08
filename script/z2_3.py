from scipy.interpolate import interp1d
import matplotlib.pyplot as plt 
import numpy as np
#0.1 mm
x = np.array([190,180,170,150,140,130, 110, 96, 82, 80, 72, 68,64,60,54,50,46,41,38,34,29,23,17,16])
y = np.array([1720, 1600, 1520, 1440, 1320, 1160, 1080, 960, 829, 760, 700, 660, 600, 560, 500, 460, 400, 340, 290, 224, 172, 128, 74, 48])
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xp = np.linspace(4,190,2)
p1 = np.poly1d(np.polyfit(x, y, 1))

x2 = np.array([53,50,46,44,41,35,33,29,28.4,26.8,23.5,23,21.2,18.8,16.5,15.8])
y2= np.array([1520, 1360, 1240, 1120, 1010, 900, 750, 650,590, 520, 460, 380, 310, 250, 180, 96])
z2 = np.polyfit(x2, y2, 1)
p2 = np.poly1d(z2)
xp2 = np.linspace(12,60,2)
p12 = np.poly1d(np.polyfit(x2, y2, 1))
# plt.errorbar(x, y, xerr=0., yerr=0, c='navy', marker='.', mfc='white', ms=5, fmt='o')
plt.plot(x, y, '.',color='crimson')
plt.plot(x2, y2, '.',color='green')
plt.plot(xp, p(xp), '-.', color='blue')
plt.plot(xp2, p2(xp2), '-.', color='peru')
# plt.ylim(1800)
# plt.xlim(200)
plt.grid(True)
plt.xlabel('$U_{ \t{Bx}}$, mB')
plt.ylabel('$U_{ \t{Bыx}}$, mB')
plt.title('Амплитудная характеристика каскада с общим эмиттером')
plt.legend(("Без конденсатора", "С конденсатором"))
plt.savefig('z2.3.pdf',dpi=300)
plt.show()


