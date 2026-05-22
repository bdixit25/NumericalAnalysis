# NumericalAnalysis

NumericalAnalysis is a Python project for solving nonlinear equations using classical root-finding methods. It supports:

- Bisection Method
- Newton-Raphson Method
- Regula Falsi Method

The project also supports plotting the function and generating critical-region plots from a config-driven workflow.

## Features

- Select a numerical method in `config.yaml`
- Define an equation in Python-compatible syntax
- Compute roots automatically by scanning sign changes
- Generate function plots and PDF reports for critical intervals

## Project Structure

- `run.py` — main entry point that reads `config.yaml` and dispatches the chosen solver
- `config.yaml` — configuration file for equation, solver, and plotting options
- `Solution_of_Equations/` — numerical solver implementations
  - `Bisection.py`
  - `NewtonRalphson.py`
  - `RegulaFalsiMethod.py`
- `common/` — shared utilities
  - `calculation_tools.py` — equation evaluation, root sign scanning, value generation
  - `plotting_tools.py` — plotting routines for function graphs
- `Plots/` — output directory for generated plot PDFs

## Requirements

This project depends on:

- Python 3.8+
- `PyYAML`
- `sympy`
- `numpy`
- `matplotlib`

Install dependencies with pip:

```bash
pip install pyyaml sympy numpy matplotlib
```

## Configuration

Use `config.yaml` to define:

- `Equation` — the expression to solve
- `DoPlot` — whether to generate the main function plot
- `DoCriticalRegionPlots` — whether to generate critical-region PDFs
- `SolvingEquations.method` — which solver to use

Example `config.yaml`:

```yaml
Equation:
  "x*x*x - 6*x*x + 11*x - 6"

DoPlot: True
DoCriticalRegionPlots: True

SolvingEquations:
  method: "NewtonRalphson"
```

## Usage

Run the solver from the repository root:

```bash
python run.py
```

This will:

1. load the equation and method from `config.yaml`
2. execute the selected solution finder
3. optionally produce a plot at `Plots/function_plot.pdf`
4. optionally produce critical-region plots at `Plots/critical_points.pdf`

## Numerical Methods

### Bisection Method

Implemented in `Solution_of_Equations/Bisection.py`.
- Searches for sign changes in interval values
- Refines the root by repeatedly bisecting the interval
- Uses `calculation_tools.critical_range_finder` to find candidate intervals

### Newton-Raphson Method

Implemented in `Solution_of_Equations/NewtonRalphson.py`.
- Uses symbolic differentiation via `sympy`
- Iterates using the Newton update rule: `x_{n+1} = x_n - f(x_n)/f'(x_n)` 
- Begins with a random initial guess from a critical interval

### Regula Falsi Method

Implemented in `Solution_of_Equations/RegulaFalsiMethod.py`.
- Uses secant-based interpolation between two interval endpoints
- Repeatedly computes the x-intercept of the line between the points

## Notes

- Equations should be provided in Python/sympy-compatible format
- The solver uses `critical_range_finder` to locate intervals where the function changes sign
- Plot output is saved as PDF files in the `Plots/` folder

## Extending the Project

To add a new method:

1. Create a new file under `Solution_of_Equations/`
2. Implement `solution_finder(equation)`
3. Set `SolvingEquations.method` in `config.yaml` to the new module name

## License

See `LICENSE` for licensing details.
