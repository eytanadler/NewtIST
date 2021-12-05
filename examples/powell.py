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
import matplotlib.pyplot as plt
import niceplots

# ==============================================================================
# Extension modules
# ==============================================================================
from ipnewt.api import NewtonSolver, LULinearSystem, AdaptiveLineSearch, Powell, viz2D, vizNewt

# ==============================================================================
# External Python modules
# ==============================================================================

# Set up niceplots
dark_mode = True
niceColors = niceplots.get_niceColors()
niceplots.setRCParams(dark_mode=dark_mode, set_dark_background=dark_mode)
plt.rcParams["text.usetex"] = True
plt.rcParams["font.size"] = 14
plt.rcParams["text.latex.preamble"] = r"\usepackage{amsmath} \usepackage{cmbright}"

# Set up problem
prob = NewtonSolver(options={"maxiter": 100, "tau": 0.01})
prob.model = Powell()
prob.linear_system = LULinearSystem()
prob.linesearch = AdaptiveLineSearch(options={"alpha max": 1000000.0})

# Set the initial state values
prob.model.states = np.array([14.9, 14.9])

# Run the problem
prob.setup()
prob.solve()

print(f"Solution at {prob.model.states} with residuals of {prob.model.residuals}")

# Plot the results
plt.figure(figsize=[12, 10])
xlim = [-11, 16]
ylim = [-11, 16]
c = viz2D.contour(plt.gca(), prob.model, xlim, ylim, levels=100, cmap="viridis")
plt.colorbar(c)
viz2D.bounds(plt.gca(), prob.model, xlim, ylim, colors="white", alpha=0.5, zorder=2, linestyles="solid")
viz2D.newton_path(plt.gca(), prob.data, c="white")
plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")
plt.show()

# Plot the convergence
plt.figure(figsize=[12, 10])
vizNewt.convergence(plt.gca(), prob.data, "atol", color=niceColors["Blue"], marker="o")
plt.show()

plt.figure(figsize=[12, 10])
vizNewt.convergence(plt.gca(), prob.data, "atol", color=niceColors["Red"], marker="o")
plt.show()

# Plot the pseudo-time step
plt.figure(figsize=[12, 10])
vizNewt.pseudo_time_step(plt.gca(), prob.data, marker="o", color=niceColors["Green"])
plt.show()

# Plot the penalty
plt.figure(figsize=[12, 11])
vizNewt.penalty_parameter(plt.gca(), prob.data, "mu upper", 1, color=niceColors["Yellow"], marker="o")
plt.show()
