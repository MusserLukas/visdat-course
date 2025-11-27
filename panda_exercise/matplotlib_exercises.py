
import pandas as pd
import h5py
import matplotlib.pyplot as plt
"""
plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'ro', linewidth=5.0,)
plt.axis((0, 6, 0, 20))
plt.ylabel('some numbers')
plt.show()
"""
import numpy as np

# Formatting the style of your plot
"""
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
"""
# Plotting with keyword strings
"""
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
"""
# Plotting with categorical variables
"""
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
"""
# Controlling line properties
"""
x1=[1,2,3,4], y1=[1,2,3,4]
x2=[1,2,3,4], y2=[1,2,4,8]
lines = plt.plot(x1, y1, x2, y2)
# use keyword arguments
# plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
# plt.setp(lines, 'color', 'r', 'linewidth', 2.0)
"""
# Working with multiple figures and Axes
"""
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot() by default

plt.figure(1)                # first figure current;
                             # subplot(212) still current
plt.subplot(211)             # make subplot(211) in the first figure
                             # current
plt.title('Easy as 1, 2, 3') # subplot 211 title
"""
# Working with text
"""
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
"""
# Using mathematical expressions in text
"""
# plt.title(r'$\sigma_i=15$')
"""
# Annotation text
"""
ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.ylim(-2, 2)
plt.show()
"""
# Logarithmic and other nonlinear axes
"""
# Fixing random state for reproducibility
np.random.seed(19680801)
# make up some data in the open interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
# plot with various axes scales
plt.figure()
# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)
# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)
# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog')
plt.grid(True)
# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
plt.show()
"""


# Create sample sensor data
np.random.seed(42)
n_samples = 10000  # 10 seconds at 1000 Hz
timestamps = np.linspace(0, 10, n_samples)

# Generate generic sensor measurements
sensor_data = pd.DataFrame({
    'timestamp': timestamps,
    'sensor_1': np.random.normal(0, 1, n_samples),
    'sensor_2': np.random.normal(10, 2, n_samples),
    'sensor_3': np.random.normal(100, 5, n_samples),
    'steering_angle': 50 * np.sin(0.07 * timestamps) + np.random.normal(0, 8, n_samples),
    'throttle_position': np.clip(55 + 35 * np.sin(0.09 * timestamps) + np.random.normal(0, 12, n_samples), 0, 100),
    'brake_pressure': np.maximum(0, 25 * np.sin(0.13 * timestamps + np.pi) + np.random.normal(0, 6, n_samples)),
    'suspension_travel_fl': 50 + 30 * np.sin(0.12 * timestamps) + np.random.normal(0, 8, n_samples),  # Front left
    'suspension_travel_fr': 50 + 30 * np.sin(0.12 * timestamps + 0.1) + np.random.normal(0, 8, n_samples)  # Front right
})

sensor_data['speed'] = np.clip(sensor_data['sensor_1'], 0, 75)  # Example: limit speed to realistic range
sensor_data['suspension_travel_fl'] = np.clip(sensor_data['suspension_travel_fl'], 0, 100)  # 0-100mm travel
sensor_data['suspension_travel_fr'] = np.clip(sensor_data['suspension_travel_fr'], 0, 100)

# Save to HDF5 with compression
# Key arguments for pandas' to_hdf:
#   - 'path_or_buf': filename to save to
#   - 'key': name of the dataset/group in the HDF5 file
#   - 'mode': file mode ('w' for write, 'a' for append, etc.)
#   - 'format': 'fixed' (default, fast, no queries) or 'table' (slower, supports queries)
#   - 'complib': compression library (e.g., 'zlib', 'lzf')
#   - 'complevel': compression level (0-9, higher is more compressed)
#   - 'data_columns': columns to make queryable (only for table format)
sensor_data.to_hdf('data/sensor_data.h5', 
                  key='telemetry', 
                  mode='w',
                  complib='zlib',    # Compression algorithm
                  complevel=9)       # Maximum compression

print(f"Saved {len(sensor_data)} samples to HDF5")