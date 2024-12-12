from IsingModel3d import IsingModel3d
from IsingModel import IsingModel
import random


def main():
    #model = IsingModel3d(1, 100, 100, 0.1, 1, lambda x, y, z: random.choice([-1, 1]))
    model = IsingModel3d(30, 30, 30, 10, 1, lambda x, y, z: random.choice([-1, 1]))
    model.run_simulation(n_max=400, simulations_per_temperature=10, generate_graphs=True, temperatures_list=[1, 2, 4, 6, 8], visualize=False)


if __name__ == "__main__":
    main()
