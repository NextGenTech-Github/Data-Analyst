# If you prefer to handle the image directly in memory (for example, to display it in a GUI or send over a network), 
# you can use the io module from Python's standard library 
# along with PIL (Pillow library) to convert the plot into an image object.

import matplotlib.pyplot as plt
from PIL import Image
import io

def get_plot_image():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]

    plt.figure()
    plt.plot(days, steps_walked, "o-g")
    plt.title("Step count for the week")
    plt.xlabel("Days of the week")
    plt.ylabel("Steps walked")

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()  # Close the figure to free up memory
    buf.seek(0)
    img = Image.open(buf)
    return img

# Example usage:
image = get_plot_image()
image.show()  # This will display the image if you are using a desktop environment
