import numpy as np
import matplotlib.pyplot as plt

# parameters
MeanTemp = 15           # Average temperature in the country
DailyAmpl = 10          # Amplitude of the daily cycle
YearlyAmpl = 1          # Amplitude of the yearly cycle
NoiseStd = 0.1          # Standard deviation of normally distributed error term

# Total hours in year
TotalHours = 24*365

# Generate the frequency components of the data
x = np.arange(0, TotalHours)
DailyCycle = -DailyAmpl*np.cos( (2*np.pi)*x/24 )
YearlyCycle = -YearlyAmpl*np.cos( (2*np.pi)*x/TotalHours )
Noise = np.random.normal(0, NoiseStd, TotalHours)

# Final series
y = MeanTemp + DailyCycle + YearlyCycle + Noise

# Visualise result
fig, axs = plt.subplots(2, 1)
axs[0].plot(y)
axs[0].set_title('Complete series')
axs[1].plot(y[0:(10*24)])
axs[1].set_title('First ten days')
plt.show()