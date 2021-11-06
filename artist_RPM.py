import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

def animate(i):
    data = pd.read_csv('CookedData.txt', sep=",")
    data.columns = ["Time", "RPM", "EFR", "EFR_2"]
    time = data['Time']
    rpm = data['RPM']

    plt.cla()
    plt.plot(time, rpm)
    plt.xlabel("Time (s)")
    plt.ylabel("RPM")
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.show()
