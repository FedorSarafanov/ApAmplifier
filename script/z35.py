from scipy.interpolate import interp1d 
import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([2.99,3.21,3.40,3.55,3.68,3.8,3.91,4.,4.09,4.17,4.24,4.38,4.49,4.6,4.7,4.78,4.86,4.94,5.01,5.07,5.19,5.29,5.52,5.7,6.21,6.9,7.31,7.6,8.51,8.98,9.21,9.39,9.54,9.68,9.9,10.59,11.15,11.51,11.92,12.2]) 
y = np.array([0.89,0.89,0.89,0.89,0.89,0.89,0.89,0.89,0.92,0.89,0.89,0.9,0.89,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.89,0.89,0.89,0.89,0.89,0.89,0.9,0.95,0.97,0.93,0.89,0.89,0.98,0.89,0.98,0.97,0.95,1]) 
print(len(x),len(y)) 
z = np.polyfit(x, y, 1) 
p = np.poly1d(z) 
xp = np.linspace(0,1.1,0.1) 
p1 = np.poly1d(np.polyfit(x, y, 1)) 

plt.plot(x, y, '+',color='crimson') 
plt.grid(True) 
plt.ylabel('K(F), ед') 
plt.xlabel('ln частоты, Гц') 
plt.ylim(0,1.2) 
plt.title('Частотная характеристика каскада с общим коллектором') 
plt.savefig('z35.pdf',dpi=300) 
plt.show()