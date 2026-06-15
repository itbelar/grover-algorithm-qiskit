#%%
# Importar as bibliotecas
from qiskit import QuantumCircuit,transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from qiskit.visualization import plot_distribution
from qiskit_ibm_runtime.fake_provider import FakeFez
#%%
# Construção do circuito
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
qc.measure([0, 1, 2], [0, 1, 2])
qc.draw("mpl")
#%%
# FakeBackend e Aer
fake_backend = FakeFez()
simulator = AerSimulator.from_backend(fake_backend)

circ = transpile(qc, simulator)
result = simulator.run(circ, shots=1024).result()

counts = result.get_counts()
shots = sum(counts.values())

probabilidade = {state: count / shots for state, count in counts.items()}
plot_distribution( probabilidade,bar_labels=True )
#%%
# Plot histograma
#qc.measure([0, 1, 2], [0, 1, 2])
#plot_histogram(counts)

# %%
