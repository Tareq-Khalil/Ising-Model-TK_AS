# Parameters for Magnetic Field
H = np.linspace(-2, 2, 100)  # Magnetic field range
T_fixed = [1.5, 2.0, 2.5]  # Example fixed temperatures
colors = ['blue', 'green', 'orange']

# Graph 5: Magnetization vs. Magnetic Field
plt.figure()
for T in T_fixed:
    M_H = np.tanh(H / T)  # Example function for Magnetization
    plt.plot(H, M_H, label=f"T = {T}")
plt.title("Magnetization vs. Magnetic Field")
plt.xlabel("Magnetic Field (H)")
plt.ylabel("Magnetization (M)")
plt.legend()
plt.grid()
plt.show()

# Graph 6: Energy vs. Magnetic Field
plt.figure()
for T in T_fixed:
    E_H = -H * np.tanh(H / T)  # Example function for Energy
    plt.plot(H, E_H, label=f"T = {T}")
plt.title("Energy vs. Magnetic Field")
plt.xlabel("Magnetic Field (H)")
plt.ylabel("Energy (E)")
plt.legend()
plt.grid()
plt.show()
