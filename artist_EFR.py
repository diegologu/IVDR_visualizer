import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
    data = pd.read_csv('CookedData.txt', sep=",")
    data.columns = ["Time", "RPM", "EFR", "EFR_2"]
    time = data['Time']
    efr = data['EFR']
    efr_2 = data['EFR_2']

    plt.cla()

    plt.plot(time, efr, label='Fuel Flow EFR')
    plt.plot(time, efr_2, label='Fuel Flow MAF')
    plt.xlabel("Time (s)")
    plt.ylabel("Fuel Rate (L/s)")
    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()
plt.show()
