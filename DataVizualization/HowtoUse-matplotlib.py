import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6890]
steps_last_week = [9788, 8710, 5308, 17630, 21309, 4002, 5223]
steps_last_month = [6752, 8610, 5708, 18630, 20000, 3800, 6999]
steps_last_quater = [7657, 8710, 5308, 17630, 21309, 4002, 5223]

plt.plot(days, steps_walked)
plt.plot(days, steps_walked, "o-g")  # using green lines with circle markers ("o-g").
plt.plot(days, steps_last_week, "v--m") # using magenta dashed lines with triangle_down markers ("v--m")
plt.plot(days, steps_last_month, "x:r") # days using red dotted lines with x markers ("x:r")


plt.title("Step count for the week")
plt.xlabel("Days of the week")
plt.ylabel("Steps walked")
plt.grid(False) # this shows grid lines.
plt.show()


