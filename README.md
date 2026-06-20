# Grover Algorithm with Qiskit

Implementação do Algoritmo de Grover utilizando Qiskit para estudo de Computação Quântica.

Este projeto apresenta uma implementação completa do algoritmo de busca de Grover em um sistema de 3 qubits, explorando três cenários distintos:

- Simulação ideal utilizando Statevector;
- Simulação com modelo de ruído baseado em hardware real da IBM;
- Execução em processador quântico real IBM Quantum.

## Sobre o Algoritmo de Grover

O Algoritmo de Grover é um dos principais algoritmos quânticos, oferecendo uma aceleração quadrática para problemas de busca não estruturada.

Enquanto uma busca clássica exige em média O(N) operações, o algoritmo de Grover encontra o elemento desejado em aproximadamente O(√N) operações.

Neste projeto, o estado marcado é:|011〉

O circuito é composto por:

1. Preparação da superposição;
2. Aplicação do Oráculo;
3. Operador de Difusão (Amplitude Amplification);
4. Repetição das iterações de Grover;
5. Medição dos qubits.

---

## Estrutura do Projeto

```text
grover-algorithm-qiskit/
│
├── grover_3qubit_statevector_simulation.py
├── grover_3qubit_noise_simulation_fakefez.py
├── grover_3qubit_real_hardware_ibm_fez.py
└── README.md
Arquivos
grover_3qubit_statevector_simulation.py

Simulação ideal do algoritmo utilizando o simulador Statevector do Qiskit.

Permite:

Visualizar o vetor de estado final;
Calcular probabilidades exatas;
Gerar gráficos de distribuição;
Comparar resultados teóricos com medições.
grover_3qubit_noise_simulation_fakefez.py

Simulação do circuito considerando ruídos reais de hardware.

Utiliza:FakeFez()
para reproduzir características de erro do processador IBM Fez.

Permite avaliar:

Impacto de ruídos quânticos;
Degradação da probabilidade do estado marcado;
Diferenças entre ambiente ideal e realista.
grover_3qubit_real_hardware_ibm_fez.py

Execução do algoritmo diretamente em um computador quântico IBM Quantum.

Utiliza:

Qiskit Runtime
SamplerV2
Backend ibm_fez

Os resultados obtidos refletem o comportamento do algoritmo em hardware quântico real.
Instalação

Clone o repositório:
git clone https://github.com/itbelar/grover-algorithm-qiskit.git

cd grover-algorithm-qiskit

Instale as dependências:
pip install qiskit qiskit-aer qiskit-ibm-runtime matplotlib

Para o Hardware Quântico Real

Configure suas credenciais IBM Quantum:
export IBM_QUANTUM_TOKEN="SEU_TOKEN"
export IBM_QUANTUM_INSTANCE="SEU_INSTANCE"
Conceitos Utilizados
Computação Quântica
Qubits
Superposição
Interferência Quântica
Porta Hadamard
Oracle
Amplitude Amplification
Grover Search
Simulação Quântica
IBM Quantum Platform
Tecnologias
Python
Qiskit
Qiskit Aer
IBM Quantum Runtime
Matplotlib
Resultados Esperados

O algoritmo amplifica a probabilidade do estado marcado:

|011〉

fazendo com que ele apareça com maior frequência nas medições quando comparado aos demais estados da superposição.

A comparação entre:

Simulação ideal;
Simulação ruidosa;
Hardware real;

permite observar os efeitos de erros físicos em dispositivos quânticos atuais (NISQ).

Referências
Grover, L. K. (1996). A Fast Quantum Mechanical Algorithm for Database Search.
Qiskit Documentation
IBM Quantum Learning
