# %%
# Importar as bibliotecas
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit.visualization import plot_histogram
import os

service = QiskitRuntimeService(channel="ibm_quantum_platform"),
            token= os.environ.get("IBM_QUANTUM_TOKEN"),
            instance =os.environ.get("IBM_QUANTUM_INSTANCE")

# Conecta à IBM Quantum (token salvo previamente)
# service = QiskitRuntimeService()

# Seleciona QPU real
backend = service.backend("ibm_fez")
#%%
# squema de 3 qubits do algoritmo de Grover um estado marcado (|011〉)
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
#qc.draw("mpl")
#qc.measure([0, 1, 2], [0, 1, 2])

#%%
# Medição 
qc.measure([0,1,2], [0,1,2])

# Transpila para o hardware real
qc_tr = transpile(qc, backend)

# Executa na QPU
sampler = SamplerV2(mode=backend)
job = sampler.run([(qc_tr, None, 1024)])

# Resultados
result = job.result()
counts = result[0].data.c.get_counts()

# Converte para probabilidades
shots = sum(counts.values())
probabilities = {k: v/shots for k, v in counts.items()}
plot_histogram(probabilities)
#%%
# Plot do histograma
#plot_histogram(counts)

