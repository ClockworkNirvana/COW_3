import matplotlib.pyplot as plt
import numpy as np

with open("Elevation.csv") as f:
    ncols = len(f.readline().split(','))

data = np.loadtxt('Elevation.csv', skiprows=1, usecols=range(1, ncols-1), delimiter=',')


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

dx = np.loadtxt('Elevation.csv', max_rows=1, delimiter=',', usecols=range(1, ncols-1))
dy = np.loadtxt('Elevation.csv', delimiter=',', usecols=0, skiprows=1)

X, Y = np.meshgrid(dx, dy)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, data, rstride=10, cstride=10)

# Plot start and end
ax.scatter(0, 0, 7.9, marker='^', c='red')
ax.text(0, 0, 7.9, 'start')
ax.scatter(90, 50, 4.1, marker='^', c='green')
ax.text(90, 50, 4.1, 'end')

# Rotate the axes and update
for angle in range(0, 360):
    # Normalize the angle to the range [-180, 180] for display
    azim = (angle + 180) % 360 - 180

    # Update the axis view and title
    ax.view_init(0, azim, 0)
    plt.title('Azimuth: %d°' % azim)

    plt.draw()
    plt.pause(.001)
