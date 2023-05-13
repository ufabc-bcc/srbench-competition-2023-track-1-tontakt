import numpy as np
from multiprocessing import cpu_count

print(cpu_count())

array = np.loadtxt("../SR_competition/srbench-competition-2023-track-1-tontakt/datasets/dataset_2.csv", delimiter=",", skiprows=1, unpack=True)
#print(array)
X = array[0:6,:].T
y = array[-1,:] 
#print(X)
#print(y)

#exit()

print("Data loaded. Wait for....")

#inv((x0 * sin(0.9850267 + -0.35517097)) + (cos(0.9850267 ^ ((x0 + x0) + (0.12625904 ^ x0))) ^ x0))    

from pysr import PySRRegressor

model = PySRRegressor(
    model_selection="accuracy",  # Result is mix of simplicity+accuracy
    procs=56,
    populations=100,
    # ^ 2 populations per core, so one is always running.
    population_size=64,
    # ^ Slightly larger populations, for greater diversity.
    niterations=44440,
    ncyclesperiteration=1024,
    maxsize=17, #At least 7
    binary_operators=["+", "*","^"],
    unary_operators=[
        "log",
        "exp",
        "two(x) = 2.0f0"
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"two": lambda x: 2},
    # ^ Define operator for SymPy as well
    loss="loss(x, y) = (x - y)^2",
    # ^ Custom loss function (julia syntax)
)

model.fit(X, y)

print(model)
