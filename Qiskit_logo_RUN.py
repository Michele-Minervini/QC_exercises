# Run the circuit of the Qiskit logo file on a simulator and a real device

# Get statevector from circuit
from qiskit.quantum_info import Statevector
statevector = Statevector.from_instruction(circuit)

# Run this cell to view the output of your quantum circuit as a histogram
from qiskit_aer.primitives import Sampler as AerSampler
from qiskit.tools.visualization import plot_distribution

# Run the circuit on the simulator and get probability distribution
sampler = AerSampler()
circuit.measure_all() # measure all qubits
job = sampler.run(circuit)
prob_distribution = job.result().quasi_dists[0].binary_probabilities()

# Print and plot results
print(statevector)
print("Simulator Probability Distribution:", prob_distribution)
plot_distribution(prob_distribution, color=['lightblue'])
