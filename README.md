# Ising-Model-TK_AS

# Usage
To use the code you need **Python 3.9+** \
To run visualization just run the IsingModel3d ```run_simulation``` method. This way no graphs are created, you can just see the visualization. \
The model is updated in runtime and you can rotate and move the camera \


# Structure
There are 2 classes in the code: IsingModel and IsingModel3d. The latter inherits IsingModel and implements additional visualization

# Implementation
The model is implemented without any libraries that can improve the performance (like NumPy) \
Visualization is done with **pyqtgraph** Python library
