from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit_algorithms.state_fidelities import ComputeUncompute
from qiskit.primitives import Sampler


# IRIS Data Set
from sklearn import datasets
iris = datasets.load_iris()
print(iris.data)
print(iris.target)
print(iris.target_names)
dimension = len(iris.data[0])

adhoc_dimension = len(iris.data[0])
adhoc_feature_map = ZZFeatureMap(feature_dimension=adhoc_dimension, reps=2, entanglement="linear")
sampler = Sampler()
fidelity = ComputeUncompute(sampler=sampler)
adhoc_kernel = FidelityQuantumKernel(fidelity=fidelity, feature_map=adhoc_feature_map)

qsvc = QSVC(quantum_kernel=adhoc_kernel)

qsvc.fit(iris.data,iris.target)

print(qsvc.predict([[5.0, 3.3, 1.5, 0.3], 
                    [6.0, 2.9, 5.2, 1.7]]))
