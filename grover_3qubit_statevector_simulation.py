#%%
# Importar as bibliotecas
from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_distribution

qc = QuantumCircuit(3,3)
# Superposição
qc.h(0)
qc.h(1)
qc.h(2)

# Oráculo
qc.barrier()
qc.x(0)
qc.ccz(0,1,2)
qc.x(0)

# Operador de difusão
qc.barrier()
qc.h(0)
qc.h(1)
qc.h(2)
qc.x(0)
qc.x(1)
qc.x(2)
qc.ccz(0,1,2)
qc.x(0)
qc.x(1)
qc.x(2)
qc.h(0)
qc.h(1)
qc.h(2)


# Oráculo
qc.barrier()
qc.x(0)
qc.ccz(0,1,2)
qc.x(0)

# Operador de difusão
qc.barrier()
qc.h(0)
qc.h(1)
qc.h(2)
qc.x(0)
qc.x(1)
qc.x(2)
qc.ccz(0,1,2)
qc.x(0)
qc.x(1)
qc.x(2)
qc.h(0)
qc.h(1)
qc.h(2)
qc.draw('mpl')

#%%
# Vetor de Estado
qc.save_statevector()
simulator = AerSimulator(method='statevector')
circ = transpile(qc, simulator)
result = simulator.run(circ).result()
statevector = result.get_statevector()
print(statevector)
#%%
# Probabilidade
probabilidade = Statevector(statevector).probabilities_dict()
print(probabilidade)
# Gráfico da probabilidade de distribuição 
plot_distribution(probabilidade,bar_labels=True)
#%%
# Plot histograma
qc_measure = qc.copy()
qc.measure([0,1,2], [0,1,2])
simulator = AerSimulator()
circ = transpile(qc, simulator)
result = simulator.run(circ, shots = 1024).result()
counts = result.get_counts(circ)
plot_histogram(counts)

# %%
