import time
import random
import matplotlib.pyplot as plt
from pysat.solvers import Glucose3

# configuración del tamaño de los datos
sizes = [10, 20, 25, 30]

# lista para almacenar los tiempos de ejecucion
times = []

# generacion de problemas SAT aleatorios y medicion del tiempo de ejecucion
for n in sizes:
    # generacion de una formula SAT aleatoria con n variables y m clausulas
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
    f = Glucose3()
    for clause in clauses:
        f.add_clause(clause)

    # resolucion del problema SAT y medicion del tiempo de ejecucion
    start_time = time.time()
    greedy_solution = {}
    for i in range(1, n + 1):
        greedy_solution[i] = random.choice([True, False])
    while True:
        unsatisfied_clauses = []
        for clause in clauses:
            satisfied = False
            for literal in clause:
                variable = abs(literal)
                value = greedy_solution[variable]
                if literal > 0 and value or literal < 0 and not value:
                    satisfied = True
                    break
            if not satisfied:
                unsatisfied_clauses.append(clause)
        if not unsatisfied_clauses:
            break
        variable = abs(random.choice(unsatisfied_clauses)[random.randint(0, 2)])
        greedy_solution[variable] = not greedy_solution[variable]
    end_time = time.time()
    times.append(end_time - start_time)

# grafico de los tiempos de ejecucion vs el tamaño de los datos
plt.plot(sizes, times)
plt.xlabel('Tamaño del problema')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución vs tamaño del problema')
plt.show()