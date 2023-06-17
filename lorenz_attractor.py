
import matplotlib.pyplot as plt
from matplotlib import cmf

# Model parameters
sigma = 10
beta = 8/3
p = 28

# Initial time
dt = 0.01
tglob = 0

# Position Parameters
x = 10
y = 5
z = 2

x_pos = []
y_pos = []
z_pos = []

# Simulation loop
while tglob <=100:
    x_pos.append(x)
    y_pos.append(y)
    z_pos.append(z)

    # Differential equations
    vx = sigma * (y - x)
    vy = x* (p - z) - y
    vz = x * y - beta * z

    x += vx * dt
    y += vy * dt
    z += vz * dt
    print(tglob)
    tglob +=dt

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(x_pos,y_pos,z_pos)
plt.show()