import matplotlib.pyplot as plt
import numpy as np
import os

# Specify OneDrive - UOB path
one_drive_path = r'C:\Users\harry\OneDrive - University of Bristol\Documents\QE CDT\Project B - Quantum Feedforward Loops\Results\Delay Results'

# Function to read CSV file generated from oscilloscope data
def read_csv(file_path):
    data = np.genfromtxt(file_path, delimiter=',', usecols=(3, 4))
    time = data[:, 0]
    voltage = data[:, 1]

    return time, voltage

# Specify file paths
file1 = os.path.join(one_drive_path, 'ALL0000', 'F0000CH1.CSV')
file2 = os.path.join(one_drive_path, 'ALL0000', 'F0000CH2.CSV')

# Read data from CSV files
time1, voltage1 = read_csv(file1)
time2, voltage2 = read_csv(file2)

# Plot data
plt.figure(figsize=(10,6))
plt.plot(time1, voltage1, label='Channel 1')
plt.plot(time2, voltage2, label='Channel 2')
plt.xlabel('Time (ns)')
plt.ylabel('Voltage ()')
plt.legend()
plt.grid(True)
plt.show()

