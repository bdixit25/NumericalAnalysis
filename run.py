import yaml
import importlib

# Open the config file and load the settings
with open("config.yaml") as config_file:
    try:
        config_settings = yaml.safe_load(config_file)
    except:
        print("Something went wrong. Couldn't find the config.yaml")

method_file = config_settings["SolvingEquations"]["method"]
equation = config_settings["Equation"]
doPlot = config_settings["DoPlot"]
doCriticalRegionPlots = config_settings["DoCriticalRegionPlots"]


# Import the method for finding the solution and 
# Solving the equation for solutions
module_path = f"Solution_of_Equations.{method_file}"
module = importlib.import_module(module_path)
solution_finder = module.solution_finder
solution_finder(equation)


# Do the plots if needed
if doPlot or doCriticalRegionPlots:
    plotter_module = importlib.import_module("common.plotting_tools")
    calculation_module = importlib.import_module("common.calculation_tools")
    value_finder_tool = calculation_module.value_finder
    xy_pairs = value_finder_tool(equation)


    # Do the plots if asked
    if doPlot:
        plotter_tool = plotter_module.plotter
        plotter_tool(xy_pairs)
    # Plot the critical regions if asked
    if doCriticalRegionPlots:
        print("Hi! I haven't implemented this yet")
