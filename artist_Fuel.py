import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
    data = pd.read_csv('CookedData.txt', sep=",")
    data.columns = ["Time", "RPM", "EFR", "EFR_2"]
    time = data['Time']
    efr = data['EFR']
    efr_2 = data['EFR_2']
    Tdiff = np.diff(time)
    efr.pop(0)
    efr_2.pop(0)
    time.pop(0)
    plt.cla()
    plt.plot(time, np.cumsum(efr*Tdiff), label='Fuel Consumption EFR')
    plt.plot(time, np.cumsum(efr_2*Tdiff), label='Fuel Consumption MAF')
    plt.xlabel("Time (s)")
    plt.ylabel("Fuel (L)")
    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()
plt.show()
