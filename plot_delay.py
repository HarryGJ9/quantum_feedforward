import matplotlib.pyplot as plt
import numpy as np
import os


# Function to read CSV file generated from oscilloscope data
def read_csv(file_path):
    data = np.genfromtxt(file_path, delimiter=',', usecols=(3, 4))
    time = data[:, 0]
    voltage = data[:, 1]

    return time, voltage

# Function to find OneDrive path on either home or office PC
def find_onedrive_path():
    # Get user's home directory
    home_dir = os.path.expanduser("~")

    # Specify OneDrive folder name
    one_drive_name = 'OneDrive - University of Bristol'

    # Construct path to onedrive folder
    one_drive_path = os.path.join(home_dir, one_drive_name)

    # Check if it exists
    if os.path.exists(one_drive_path):
        return one_drive_path
    else:
        raise FileNotFoundError("University OneDrive not found.")

# Find University of Bristol's OneDrive path
try:
    one_drive_path = find_onedrive_path()
except FileNotFoundError as e:
    print(e)
    exit()

# Specify relative path from onedrive folder
relative_path = 'Documents/QE CDT/Project B - Quantum Feedforward Loops/Results/Delay Results'

# Specify file paths
file1 = os.path.join(one_drive_path, relative_path, 'ALL0000', 'F0000CH1.CSV')
file2 = os.path.join(one_drive_path, relative_path, 'ALL0000', 'F0000CH2.CSV')

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

