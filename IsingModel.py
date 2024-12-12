import random
import math
from typing import Iterable, Sized
import matplotlib.pyplot as plt


class IsingModel:
    def __init__(self, x_size: int, y_size: int, z_size: int, temperature: float, interaction: float,
                 initializer: callable((int, int, int)) = lambda x, y, z: 1):
        self.initializer = initializer
        self.particles = [[[initializer(x, y, z) for z in range(z_size)] for y in range(y_size)] for x in range(x_size)]
        self.temperature = temperature
        self.x_size = x_size
        self.y_size = y_size
        self.z_size = z_size
        self.n = self.x_size * self.y_size * self.z_size
        self.j = interaction
        self.average_magnetism_points = []
        self.final_magnetism_points = []

    def initialize_particles(self):
        self.particles = [[[self.initializer(x, y, z) for z in range(self.z_size)]
                           for y in range(self.y_size)] for x in range(self.x_size)]

    @classmethod
    def from_file(cls, filename: str) -> 'IsingModel':
        with open(filename, 'r') as file:
            x, y, z, temperature, interaction = list(map(int, file.readline().split()))
            model = IsingModel(x, y, z, temperature, interaction)
            for i in range(x):
                for j in range(y):
                    spins = list(map(int, file.readline().split()))
                    for k in range(z):
                        model[i, j, k] = spins[k]
            return model

    def get_magnetism(self) -> float:
        res = 0
        for i in range(self.n):
            res += self[i]
        return res / self.n


    def calculate_h(self, x: int, y: int, z: int):
        current = self.particles[x][y][z]
        res = 0
        for coords in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            res += current * self.particles[(x + coords[0]) % self.x_size][(coords[1] + y) % self.y_size][(coords[2] + z) % self.z_size]
        return -self.j * res

    def make_simulation_step(self):
        for _ in range(self.n):
            x = random.randint(0, self.x_size - 1)
            y = random.randint(0, self.y_size - 1)
            z = random.randint(0, self.z_size - 1)
            h_old = self.calculate_h(x, y, z)
            h_new = -h_old
            delta_h = h_new - h_old
            if delta_h <= 0:
                self.particles[x][y][z] *= -1
            else:
                prob = math.exp(-delta_h / self.temperature)
                if random.random() < prob:
                    self.particles[x][y][z] *= -1

    def _n_index_to_xyz(self, key: int) -> (int, int, int):
        x = key // (self.y_size * self.z_size)
        key %= self.y_size * self.z_size
        y = key // self.z_size
        z = key % self.z_size
        return x, y, z

    def __getitem__(self, key: tuple[int, int, int] or int):
        if isinstance(key, int):
            x, y, z = self._n_index_to_xyz(key)
        else:
            x, y, z = key
        return self.particles[x][y][z]

    def __setitem__(self, key: tuple[int, int, int] or int, value: 1 or -1):
        if isinstance(key, int):
            x, y, z = self._n_index_to_xyz(key)
        else:
            x, y, z = key
        self.particles[x][y][z] = value

    @staticmethod
    def make_magnetism_progression_graph(magnetism: Sized and Iterable[float], output_filename: str):
        plt.close()
        plt.plot(range(1, len(magnetism) + 1), magnetism)
        plt.xlabel('Iteration')
        plt.ylabel('Magnetism')
        plt.savefig(output_filename + '.png')

    @staticmethod
    def make_magnetism_by_temperature_graph(data: dict[float, float], output_filename: str):
        plt.close()
        items = list(sorted(data.items()))
        plt.plot(list(map(lambda x: x[0], items)), list(map(lambda x: x[1], items)))
        plt.xlabel('Temperature')
        plt.ylabel('Magnetism')
        plt.savefig(output_filename + '.png')

    def add_average_magnetism(self, temperature: float, magnetism: float):
        self.average_magnetism_points.append((temperature, magnetism))

    def add_final_magnetism(self, temperature: float, magnetism: float):
        self.final_magnetism_points.append((temperature, magnetism))

    @staticmethod
    def scatter_points(points: Iterable[tuple[float, float]], output_filename):
        plt.close()
        fig, ax = plt.subplots()
        x = list(map(lambda _x: _x[0], points))
        y = list(map(lambda _x: _x[1], points))

        ax.scatter(x, y, c='deeppink')


        ax.set_facecolor('black')

        fig.set_figwidth(8)
        fig.set_figheight(8)  # высота "Figure"

        plt.savefig(output_filename)

    def make_points_graphs(self):
        self.scatter_points(self.average_magnetism_points, 'average_magnetism_each_simulation')
        self.scatter_points(self.final_magnetism_points, 'final_magnetism_each_simulation')

    def run_simulation(self, n_max: int, simulations_per_temperature: int = 10, generate_graphs: bool = True,
                       temperatures_list: Iterable[float] = ()):

        average_magnetism_by_temperature = {}
        final_magnetism_by_temperature = {}
        for temperature in temperatures_list:
            print(f'Temperature: {temperature}')
            self.temperature = temperature
            average_magnetism = []
            final_magnetism = []
            for simulation_n in range(simulations_per_temperature):
                print(f'Simulation: {simulation_n}')
                self.initialize_particles()
                current_step_magnetism = []
                for step in range(n_max):
                    self.make_simulation_step()
                    magnetism = self.get_magnetism()
                    current_step_magnetism.append(magnetism)
                final_magnetism.append(self.get_magnetism())
                average_magnetism.append(sum(current_step_magnetism) / len(current_step_magnetism))
                self.add_final_magnetism(temperature, final_magnetism[-1])
                self.add_average_magnetism(temperature, average_magnetism[-1])
                # make just one magnetism progression graph per one temperature
                if simulation_n == 0 and generate_graphs:
                    self.make_magnetism_progression_graph(current_step_magnetism,
                                                          f'temp_{temperature}_magnetism_progression')

            average_magnetism_by_temperature[temperature] = sum(map(abs, average_magnetism)) / len(average_magnetism)
            final_magnetism_by_temperature[temperature] = sum(map(abs, final_magnetism)) / len(final_magnetism)

            # Generate graphs after each temperature to observe changes dynamically
            # and not just after the end of all the simulation
            if generate_graphs:
                self.make_magnetism_by_temperature_graph(average_magnetism_by_temperature, 'average_magnetism_by_temperature')
                self.make_magnetism_by_temperature_graph(final_magnetism_by_temperature, 'final_magnetism_by_temperature')
                self.make_points_graphs()
