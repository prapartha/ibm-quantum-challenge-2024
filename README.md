# IBM Quantum Challenge 2024 — Solutions

Personal solutions for the [IBM Quantum Challenge 2024](https://github.com/qiskit-community/ibm-quantum-challenge-2024), completed on IBM Quantum Platform using Qiskit 1.0+.

> **Official challenge repository:** [qiskit-community/ibm-quantum-challenge-2024](https://github.com/qiskit-community/ibm-quantum-challenge-2024)

---

## Structure

```
ibm-quantum-challenge-2024/
├── labs/
│   ├── lab-1/                        # Introduction to Qiskit 1.0
│   ├── lab-2/                        # The Transpiler
│   ├── lab-3/                        # What's Next — four sneak previews
│   │   ├── lab-3-serverless.ipynb
│   │   ├── lab-3-ai-transpiler.ipynb
│   │   ├── lab-3-code-assistant.ipynb
│   │   └── lab-3-circuit-knitting.ipynb
│   ├── lab-4/                        # Variational Quantum Classifier on real hardware
│   └── lab-bonus/                    # Bonus: Scaling to 50 Qubits
├── scripts/                          # Reusable Python modules used by the labs
└── extras/                           # Additional notebooks (VQC tutorial/experiments)
```

---

## Labs

### Lab 1 — Introduction to Qiskit 1.0
[`labs/lab-1/lab-1.ipynb`](labs/lab-1/lab-1.ipynb)

Covers the updated Qiskit 1.0 API: building circuits, using primitives (`Estimator`, `Sampler`), and executing on IBM backends via `QiskitRuntimeService`.

---

### Lab 2 — The Transpiler
[`labs/lab-2/lab-2.ipynb`](labs/lab-2/lab-2.ipynb)

Deep dive into Qiskit's transpiler pipeline — pass managers, optimization levels, ISA (Instruction Set Architecture) circuits, and target-aware compilation.

---

### Lab 3 — What's Next (Four Sneak Previews)

Four independent sub-labs, each previewing an emerging IBM Quantum capability:

| Notebook | Topic |
|----------|-------|
| [`lab-3-serverless.ipynb`](labs/lab-3/lab-3-serverless.ipynb) | **Qiskit Serverless** — offload quantum workloads to the cloud |
| [`lab-3-ai-transpiler.ipynb`](labs/lab-3/lab-3-ai-transpiler.ipynb) | **AI-Powered Transpilation** via Qiskit Transpiler Service |
| [`lab-3-code-assistant.ipynb`](labs/lab-3/lab-3-code-assistant.ipynb) | **Qiskit Code Assistant** — LLM-aided quantum programming |
| [`lab-3-circuit-knitting.ipynb`](labs/lab-3/lab-3-circuit-knitting.ipynb) | **Circuit Knitting Toolbox** — cutting large circuits into smaller pieces |

---

### Lab 4 — Variational Quantum Classifier on Real Hardware
[`labs/lab-4/lab-4.ipynb`](labs/lab-4/lab-4.ipynb)

Trains and evaluates a Variational Quantum Classifier (VQC) on a bird species dataset using a real IBM quantum backend. Pre-optimized parameters are included for reproducibility.

**Accompanying data files:**
- `birds_dataset.csv` — classification dataset
- `opt_params_shallow_VQC.npy` — optimized VQC parameters
- `params_0_list.npy` — initial parameter sweep results

---

### Bonus Lab — Scaling to 50 Qubits
[`labs/lab-bonus/lab-bonus.ipynb`](labs/lab-bonus/lab-bonus.ipynb)

Explores techniques for executing circuits at scale (50 qubits) on real IBM hardware, including error mitigation and efficient sampling strategies.

---

## Scripts

Reusable Python modules referenced across the labs:

| File | Description |
|------|-------------|
| [`vqe.py`](scripts/vqe.py) | VQE implementation using `EstimatorV2` and Qiskit Serverless |
| [`transpile_parallel.py`](scripts/transpile_parallel.py) | Parallel circuit transpilation across multiple backends |
| [`utils.py`](scripts/utils.py) | Shared utilities for visualization and circuit inspection |
| [`knn1.py`](scripts/knn1.py) | Quantum k-nearest neighbours using amplitude encoding (Qiskit/Aer) |
| [`qsvm.py`](scripts/qsvm.py) | Quantum SVM with `ZZFeatureMap` and `FidelityQuantumKernel` on IRIS dataset |

---

## Extras

[`extras/vqc.ipynb`](extras/vqc.ipynb) — Standalone notebook introducing variational quantum algorithms and VQC theory with worked examples; used as reference material while completing Lab 4.

---

## Setup

```bash
pip install qiskit qiskit-ibm-runtime qiskit-aer qiskit-serverless \
            qiskit-machine-learning scikit-learn matplotlib numpy scipy
```

An IBM Quantum account is required for running circuits on real backends:

```python
from qiskit_ibm_runtime import QiskitRuntimeService
QiskitRuntimeService.save_account(channel="ibm_quantum", token="<YOUR_TOKEN>")
```

---

## Reference

- [IBM Quantum Challenge 2024 — Official Repo](https://github.com/qiskit-community/ibm-quantum-challenge-2024)
- [Qiskit Documentation](https://docs.quantum.ibm.com/)
- [IBM Quantum Platform](https://quantum.ibm.com/)
- [Qiskit Machine Learning](https://qiskit-community.github.io/qiskit-machine-learning/)
- [Circuit Knitting Toolbox](https://qiskit-community.github.io/qiskit-addon-cutting/)
