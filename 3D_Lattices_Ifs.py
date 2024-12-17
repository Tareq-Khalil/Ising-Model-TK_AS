import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


L = 10  
np.random.seed(42)  

def generate_3d_lattice(L, T, T_c):
   
    spins = np.random.choice([-1, 1], size=(L, L, L))  
    if T > T_c:
        spins = np.random.choice([-1, 1], size=(L, L, L))  
    elif T < T_c:
        spins = np.ones((L, L, L)) 
    return spins

def plot_3d_lattice(spins, title):
  
    L = spins.shape[0]
    x, y, z = np.meshgrid(range(L), range(L),
range(L), indexing='ij')
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')


    ax.scatter(x[spins == 1], y[spins == 1], 
z[spins == 1], color='red', label='Spin +1')
    ax.scatter(x[spins == -1], y[spins == -1],
z[spins == -1], color='blue', label='Spin -1')

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

T_high = 3.0  
T_critical = 2.27  
T_low = 1.5  
T_c = 2.27

lattice_high = generate_3d_lattice(L, T_high, T_c)
lattice_critical = generate_3d_lattice(L, T_critical, T_c)
lattice_low = generate_3d_lattice(L, T_low, T_c)

plot_3d_lattice(lattice_high, "Figure 1: 3D Lattice at T > T_c (Disordered)")
plot_3d_lattice(lattice_critical, "Figure 2: 3D Lattice at T ≈ T_c (Critical)")
plot_3d_lattice(lattice_low, "Figure 3: 3D Lattice at T < T_c (Ordered)")
