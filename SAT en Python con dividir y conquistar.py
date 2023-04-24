import time
import matplotlib.pyplot as plt
import random
from typing import List
from pysat.solvers import Glucose3

class Formula:
    def __init__(self, clauses: List[List[int]]):
        self.clauses = clauses
        self.solver = Glucose3()
        for clause in clauses:
            self.solver.add_clause(clause)
            
    def solve(self) -> bool:
        return self.solver.solve()
        
    def split(self) -> List['Formula']:
        mid = len(self.clauses) // 2
        f1 = Formula(self.clauses[:mid])
        f2 = Formula(self.clauses[mid:])
        return [f1, f2]
# Función que resuelve una fórmula SAT utilizando una estrategia de dividir y conquistar
def sat_dc(formula):
    if len(formula.clauses) == 0:
        return True
    if len(formula.clauses[0]) == 0:
        return False
    # Dividir la fórmula en dos mitades
    f1, f2 = formula.split()
    # Resolver las dos mitades recursivamente
    if sat_dc(f1):
        return True
    if sat_dc(f2):
        return True
    return False

# Configuración del tamaño de los datos
sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 300, 500, 1000]

# Lista para almacenar los tiempos de ejecución
times = []

# Generación de problemas SAT aleatorios y medición del tiempo de ejecución
for n in sizes:
    # Generación de una fórmula SAT aleatoria con n variables y m cláusulas
    m = int(n * 4.2)
    clauses = []
    for i in range(m):
        a, b, c = sorted([random.randint(1, n) for j in range(3)])
        if random.choice([True, False]):
            a = -a
        if random.choice([True, False]):
            b = -b
        if random.choice([True, False]):
            c = -c
        clauses.append([a, b, c])
    f = Formula(clauses)

    # Resolución del problema SAT utilizando una estrategia de dividir y conquistar y medición del tiempo de ejecución
    start_time = time.time()
    sat_dc(f)
    end_time = time.time()
    times.append(end_time - start_time)

# Gráfico de los tiempos de ejecución vs el tamaño de los datos
plt.plot(sizes, times)
plt.xlabel('Tamaño del problema')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución vs tamaño del problema')
plt.show()