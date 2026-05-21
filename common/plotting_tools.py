import matplotlib.pyplot as plt

# Function to plot the 'function'
def plotter(values=None, filename="output.pdf"):
    # Avoid mutable default arguments (like values=[]) in Python
    if values is None:
        values = []
        
    x_values = []
    y_values = []

    for val_pairs in values:
        x_values.append(val_pairs[0])
        y_values.append(val_pairs[1])
   
    fig = plt.figure()
    plt.plot(x_values, y_values)
    plt.grid()
    
    # Save directly to PDF and optimize layout spacing
    plt.savefig(filename, format='pdf', bbox_inches='tight')
    
    return fig 

