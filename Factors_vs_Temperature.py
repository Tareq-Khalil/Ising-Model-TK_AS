import numpy as np
import matplotlib.pyplot as plt


T = np.linspace(1, 5, 100)  
T_c = 2.27  
M = np.tanh((T_c - T) * 5)  
M[T > T_c] = 0
E = -np.abs(M) * T  
C_v = np.exp(-np.abs(T - T_c)) * 10 
Chi = C_v / T  

plt.figure()
plt.plot(T, M, label="Magnetization")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")

plt.xlabel("Temperature (T)")
plt.ylabel("Magnetization (M)")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(T, E, label="Energy")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")

plt.xlabel("Temperature (T)")
plt.ylabel("Energy (E)")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(T, C_v, label="Specific Heat Capacity")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")

plt.xlabel("Temperature (T)")
plt.ylabel("$C_v$")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(T, Chi, label="Susceptibility")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")

plt.xlabel("Temperature (T)")
plt.ylabel("$\chi$")
plt.legend()
plt.grid()
plt.show()
