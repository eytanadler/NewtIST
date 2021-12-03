#!/usr/bin/env python
"""
@File    :   powell.py
@Time    :   2021/12/3
@Desc    :   Run script for the Powell test problem
"""

# ==============================================================================
# Standard Python modules
# ==============================================================================

# ==============================================================================
# External Python modules
# ==============================================================================
import numpy as np

# ==============================================================================
# Extension modules
# ==============================================================================
from ipnewt.api import NewtonSolver, LULinearSystem, AdaptiveLineSearch, Powell

prob = NewtonSolver(options={"maxiter": 100, "tau": 100.0})
prob.model = Powell()
prob.linear_system = LULinearSystem()
prob.linesearch = AdaptiveLineSearch(options={"alpha max": 3.0})

prob.setup()
prob.solve()
