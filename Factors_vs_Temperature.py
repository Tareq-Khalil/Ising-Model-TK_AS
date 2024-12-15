import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = np.linspace(1, 5, 100)  # Temperature range
T_c = 2.27  # Critical temperature (example value)
M = np.tanh((T_c - T) * 5)  # Magnetization (example function)
M[T > T_c] = 0
E = -np.abs(M) * T  # Energy (example function)
C_v = np.exp(-np.abs(T - T_c)) * 10  # Specific Heat Capacity
Chi = C_v / T  # Magnetic Susceptibility

# Graph 1: Magnetization vs. Temperature
plt.figure()
plt.plot(T, M, label="Magnetization")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")
plt.title("Magnetization vs. Temperature")
plt.xlabel("Temperature (T)")
plt.ylabel("Magnetization (M)")
plt.legend()
plt.grid()
plt.show()

# Graph 2: Energy vs. Temperature
plt.figure()
plt.plot(T, E, label="Energy")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")
plt.title("Energy vs. Temperature")
plt.xlabel("Temperature (T)")
plt.ylabel("Energy (E)")
plt.legend()
plt.grid()
plt.show()

# Graph 3: Specific Heat Capacity vs. Temperature
plt.figure()
plt.plot(T, C_v, label="Specific Heat Capacity")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")
plt.title("Specific Heat Capacity vs. Temperature")
plt.xlabel("Temperature (T)")
plt.ylabel("$C_v$")
plt.legend()
plt.grid()
plt.show()

# Graph 4: Susceptibility vs. Temperature
plt.figure()
plt.plot(T, Chi, label="Susceptibility")
plt.axvline(x=T_c, color='r', linestyle='--', label="Critical Temperature $T_c$")
plt.title("Magnetic Susceptibility vs. Temperature")
plt.xlabel("Temperature (T)")
plt.ylabel("$\chi$")
plt.legend()
plt.grid()
plt.show()
