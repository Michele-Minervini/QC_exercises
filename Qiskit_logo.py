# Build a circuit with 4 qubits for the Qiskit logo

from qiskit import QuantumCircuit
from qiskit.visualization import plot_state_qsphere

circuit = QuantumCircuit(4)
circuit.h(1)
circuit.x([0,1,2,3])
circuit.cx(1,[0,2,3])

display(plot_state_qsphere(circuit))
display(circuit.draw('mpl'))
