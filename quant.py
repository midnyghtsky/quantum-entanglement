from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler import generate_preset_pass_manager
 
# Create a new circuit with two qubits
qc = QuantumCircuit(4)
 
# Add a Hadamard gate to qubit 0
qc.h(0)
qc.h(2) 
qc.cx(1,3)
qc.cx(0, 2)
 
def q():
    return (qc.draw())