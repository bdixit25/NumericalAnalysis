import yaml
import importlib

with open("config.yaml") as config_file:
    try:
        config_settings = yaml.safe_load(config_file)
    except:
        print("Something went wrong. Couldn't find the config.yaml")

method_file = config_settings["SolvingEquations"]["method"][0]
module_path = f"Solution_of_Equations.{method_file}"

module = importlib.import_module(module_path)
solution_finder = module.solution_finder 
equation = config_settings["Equation"]


solution_finder(equation)
