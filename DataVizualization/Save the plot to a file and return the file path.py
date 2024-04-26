# This method involves saving the plot to a file (like a PNG or JPEG) and then returning the file path. 
# This is useful when you need to share the plot file or use it in web applications.


import matplotlib.pyplot as plt
import datetime

def save_plot():
    #data definition
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]

    #plot configuration
    plt.figure()
    plt.plot(days, steps_walked, "o-g")
    plt.title("Step count for the week")
    plt.xlabel("Days of the week")
    plt.ylabel("Steps walked")
    
    # Save the plot to a file
    # filepath = 'path/to/your/plot.png'
    currentdate = datetime.now();
    filepath = 'save_plot_.png' 
    plt.savefig(filepath)
    plt.close()  # Close the figure to free up memory
    return filepath

# Example usage:
plot_path = save_plot()
print("Plot saved to:", plot_path)
