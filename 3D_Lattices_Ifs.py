import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lattice size and temperature
L = 10  # 10x10x10 lattice for visualization (adjust for clarity vs. performance)
np.random.seed(42)  # For reproducibility

def generate_3d_lattice(L, T, T_c):
    """Simulate a 3D lattice configuration for given T."""
    spins = np.random.choice([-1, 1], size=(L, L, L))  # Random initial configuration
    if T > T_c:
        spins = np.random.choice([-1, 1], size=(L, L, L))  # Disordered state
    elif T < T_c:
        spins = np.ones((L, L, L))  # Ordered state (all aligned spins)
    return spins

def plot_3d_lattice(spins, title):
    """Visualize a 3D lattice."""
    L = spins.shape[0]
    x, y, z = np.meshgrid(range(L), range(L), range(L), indexing='ij')
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the 3D lattice
    ax.scatter(x[spins == 1], y[spins == 1], z[spins == 1], color='red', label='Spin +1')
    ax.scatter(x[spins == -1], y[spins == -1], z[spins == -1], color='blue', label='Spin -1')

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

# Temperatures
T_high = 3.0  # T > T_c
T_critical = 2.27  # T ≈ T_c
T_low = 1.5  # T < T_c
T_c = 2.27  # Critical temperature

# Generate Lattices
lattice_high = generate_3d_lattice(L, T_high, T_c)
lattice_critical = generate_3d_lattice(L, T_critical, T_c)
lattice_low = generate_3d_lattice(L, T_low, T_c)

# Plotting Figures
plot_3d_lattice(lattice_high, "Figure 1: 3D Lattice at T > T_c (Disordered)")
plot_3d_lattice(lattice_critical, "Figure 2: 3D Lattice at T ≈ T_c (Critical)")
plot_3d_lattice(lattice_low, "Figure 3: 3D Lattice at T < T_c (Ordered)")
