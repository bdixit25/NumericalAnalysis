import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Function to plot the 'function'
def plotter(values = []):
    x_values = []
    y_values = []

    for val_pairs in values:
        x_values.append(val_pairs[0])
        y_values.append(val_pairs[1])
   
    fig = plt.figure()
    plt.plot(x_values, y_values)
    plt.grid()
    return fig

# Plot function around critical range
def critical_range_plotter():
    critical_ranges = critical_range_finder()

    plot_dic = {}

    pdf_file = PdfPages("critical_points.pdf")

    for range_pairs in critical_ranges:
        print(range_pairs)
        values = value_finder(range_pairs[0][0]-0.5, range_pairs[1][0]+0.5, step = 0.001)
        fig = plotter(values)
        pdf_file.savefig(fig)
        plt.close(fig)
    
    pdf_file.close()
