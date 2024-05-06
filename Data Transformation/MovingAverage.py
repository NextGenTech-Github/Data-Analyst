# How to write a python function using class and function to find moving average using Simple, Cumulative and Exponential Moving Average

# Simple Moving Average (SMA), 
# Cumulative Moving Average (CMA), 
# and Exponential Moving Average (EMA)—provides a structured approach to handle various financial data analysis tasks

# Used in fiancial analysis

import pandas as pd

class MovingAverages:
    def __init__(self, data):
        """
        Initialize with a list of numbers or a Pandas Series.
        """
        self.data = pd.Series(data)

    def simple_moving_average(self, window):
        """
        Calculate Simple Moving Average (SMA).
        :param window: Number of periods to consider for the moving average.
        :return: Pandas Series of the SMA values.
        """
        return self.data.rolling(window=window).mean()

    def cumulative_moving_average(self):
        """
        Calculate Cumulative Moving Average (CMA).
        :return: Pandas Series of the CMA values.
        """
        return self.data.expanding().mean()

    def exponential_moving_average(self, span):
        """
        Calculate Exponential Moving Average (EMA).
        :param span: Specifies the decay in terms of the span of the window.
        :return: Pandas Series of the EMA values.
        """
        return self.data.ewm(span=span, adjust=False).mean()

# Example usage
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ma = MovingAverages(data)
    print("Simple Moving Average (window=5):\n", ma.simple_moving_average(window=5))
    print("Cumulative Moving Average:\n", ma.cumulative_moving_average())
    print("Exponential Moving Average (span=3):\n", ma.exponential_moving_average(span=5))
