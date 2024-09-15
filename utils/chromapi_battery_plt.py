# -*- coding: utf-8 -*-

"""
    @file       chromapi_battery_plt.py
    @author     Mowibox (Ousmane THIONGANE)
    @brief      File to display Chromapi battery curves
    @version    1.0
    @date       2024-09-14

"""

import matplotlib.pyplot as plt

# Battery life values
V1 = [3.61, 3.57, 3.55, 3.52, 3.50, 3.48, 3.43, 3.35, 3.20, 2.9,
      2.8, 2.72, 2.67, 2.62, 2.46, 2.42, 2.39, 2.38, 2.37, 2.37, 2.37,]
T1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9.5, 10,
      10.5, 11, 12, 12.5, 13, 13.5, 14, 14.5, 15,]

# Battery recharge values
V2 = [3.21, 3.32, 3.36, 3.40, 3.43, 3.46, 3.48, 3.50, 3.52, 3.54, 3.56, 3.57,
      3.59, 3.6, 3.61, 3.62, 3.64, 3.66, 3.68, 3.69, 3.71, 3.72, 3.73, 3.74,]
T2 = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5,
      6, 6.5, 7, 7.5, 8, 9, 10, 11, 12, 13, 14, 15,]

# Displaying values
figure, axis = plt.subplots(2, 1)
axis[0].plot(T1, V1, 'ro-')
axis[0].set_title("Chromapi battery life time")

axis[1].plot(T2, V2, 'go-')
axis[1].set_title("Chromapi battery recharge time")

for i in range(2):
    axis[i].set_xlabel("Time (minutes)")
    axis[i].set_ylabel("Voltage (V)")
    axis[i].grid()

plt.tight_layout()
plt.plot()
plt.show()
