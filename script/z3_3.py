from scipy.interpolate import interp1d 
import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([3800,2600,2300,1400,860,820,740,700,660,600,540,500,460,380,320,260,232,204,176,148,120,100,68,53,49,37,33.5,26.5,23.2,16.4,15.5]) 
y = np.array([3400,2600,2200,1200,800,740,680,660,620,540,500,440,400,360,280,232,208,184,160,132,112,88,60,44,38,29,22,18,12,7.2,4.8]) 
z = np.polyfit(x, y, 1) 
p = np.poly1d(z) 
xp = np.linspace(5,3800,2) 
p1 = np.poly1d(np.polyfit(x, y, 1)) 

plt.plot(x, y, '.',color='crimson') 
plt.plot(xp, p(xp), '-.', color='blue') 
plt.grid(True) 
plt.xlabel('$U_{ \t{Bx}}$, mB') 
plt.ylabel('$U_{ \t{Bыx}}$, mB') 
plt.title('Амплитудная характеристика каскада с общим коллектором') 
plt.savefig('z33.pdf',dpi=300) 
plt.show()