# Copyright 2018 The PECOS Developers
# Copyright 2018 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract
# DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License.You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
"""Performance Estimator of Codes On Surfaces (PECOS)
==================================================
A framework for developing, studying, and evaluating quantum error-correcting codes.
"""

# Allow for other namespace packages
__path__ = __import__("pkgutil").extend_path(__path__, __name__)

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pypecos")
except PackageNotFoundError:
    __version__ = "0.0.0"

# PECOS namespaces
from pypecos import (
    circuit_converters,
    circuits,
    decoders,
    engines,
    error_models,
    misc,
    qeccs,
    simulators,
    slr,
    tools,
)
from pypecos.circuits.quantum_circuit import QuantumCircuit
from pypecos.engines import circuit_runners
from pypecos.engines.cvm.binarray import BinArray
from pypecos.engines.hybrid_engine_old import HybridEngine

from . import pyo3pecos as rs  # noqa: TID252

__all__ = [
    "__version__",
    "rs",
    "circuits",
    "qeccs",
    "simulators",
    "error_models",
    "circuit_runners",
    "engines",
    "decoders",
    "circuit_converters",
    "misc",
    "tools",
    "QuantumCircuit",
    "BinArray",
    "HybridEngine",
    "slr",
]
