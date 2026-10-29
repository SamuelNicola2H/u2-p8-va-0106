import matplotlib.pyplot as plt
import numpy as np

diasX=["Lun","Mar","Mie","Jue","Vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("Califas en VA de Samuel Nicola NC 0106")
plt.xlabel("dias semana habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()
