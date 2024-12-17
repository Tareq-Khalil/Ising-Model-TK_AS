H = np.linspace(-2, 2, 100)  
T_fixed = [1.5, 2.0, 2.5]  
colors = ['blue', 'green', 'orange']

plt.figure()
for T in T_fixed:
    M_H = np.tanh(H / T)  
    plt.plot(H, M_H, label=f"T = {T}")
plt.title("Magnetization vs. Magnetic Field")
plt.xlabel("Magnetic Field (J)")
plt.ylabel("Magnetization (M)")
plt.legend()
plt.grid()
plt.show()

plt.figure()
for T in T_fixed:
    E_H = -H * np.tanh(H / T)  
    plt.plot(H, E_H, label=f"T = {T}")
plt.title("Energy vs. Magnetic Field")
plt.xlabel("Magnetic Field (J)")
plt.ylabel("Energy (E)")
plt.legend()
plt.grid()
plt.show()
