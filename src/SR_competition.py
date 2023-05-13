import numpy as np
from multiprocessing import cpu_count
from sympy import pi

print(cpu_count())

array = np.loadtxt("../datasets/dataset_1.csv", delimiter=",", skiprows=1, unpack=True)
#print(array)
X = array[0:9,:].T
y = array[-1,:] 
#print(X)
#print(y)

#exit()

print("Data loaded. Wait for....")

#inv((x0 * sin(0.9850267 + -0.35517097)) + (cos(0.9850267 ^ ((x0 + x0) + (0.12625904 ^ x0))) ^ x0))    

from pysr import PySRRegressor

model = PySRRegressor(
    model_selection="accuracy",  # Result is mix of simplicity+accuracy
    procs=8,
    populations=16,
    # ^ 2 populations per core, so one is always running.
    population_size=256,
    # ^ Slightly larger populations, for greater diversity.
    niterations=4440,
    ncyclesperiteration=1024,
    maxsize=64, #At least 7
    binary_operators=["+", "-","*","/","^"],
    unary_operators=[
        "sqrt",
        "log",
        "exp",
        "two_pi(x)   = 6.283185307179586476925286766559005768394338798750211641949889185f0",
        "two(x)   = 2.0f0",
        "three(x) = 3.0f0",
        "four(x)  = 4.0f0",
        "five(x)  = 5.0f0",
        "six(x)   = 6.0f0",
        "seven(x) = 7.0f0",
        "eight(x) = 8.0f0",
        "nine(x)  = 9.0f0",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"two_pi": lambda x: 2*pi, "two": lambda x: 2, "three": lambda x: 3, "four": lambda x: 4, "five": lambda x: 5, "six": lambda x: 6, "seven": lambda x: 7, "eight": lambda x: 8, "nine": lambda x: 9},
    # ^ Define operator for SymPy as well
    loss="loss(x, y) = (x - y)^2",
    # ^ Custom loss function (julia syntax),
    complexity_of_constants = 7,
    nested_constraints  = {
                           "two_pi" : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "two"    : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "three"  : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "four"   : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "five"   : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "six"    : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "seven"  : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "eight"  : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0},
                           "nine"   : {"two_pi" : 0, "two" : 0, "three" : 0, "four" : 0, "five" : 0, "six" : 0, "seven" : 0, "eight" : 0, "nine" : 0}
                          }
    # ^ True constant functions should never be nested, as only outermost is effective anyway

)

model.fit(X, y)

print(model)
