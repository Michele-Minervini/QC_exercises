# Run the circuit of the Qiskit logo file on a simulator and a real device


# Build a circuit with 4 qubits for the Qiskit logo
from qiskit import QuantumCircuit
from qiskit.visualization import plot_state_qsphere
circuit = QuantumCircuit(4)
circuit.h(1)
circuit.x([0,1,2,3])
circuit.cx(1,[0,2,3])


# SIMULATION

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



# REAL DEVICE

from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

service = QiskitRuntimeService(channel="ibm_quantum")

# Get the least busy backend, this step may take a while
real_backend = service.least_busy(min_num_qubits=4, simulator=False)

with Session(service, backend=real_backend) as session:
    sampler = Sampler(session=session)
    job_real = sampler.run(circuit)

# Depending on the queue of the quantum system, the job can take sometime to complete. You can monitor the status on the [Jobs page](https://quantum-computing.ibm.com/jobs) or run the following cell.
job_real.status()

#If your job has successfully completed, run the following cell to compare the measurement probability distribution of the simulator and the real device.
prob_distribution_real = job_real.result().quasi_dists[0].binary_probabilities()

plot_distribution(
    data=[prob_distribution, prob_distribution_real], 
    legend=['Simulator', 'Real Device'], 
    color=['lightblue', 'black'], 
    bar_labels = False
)


