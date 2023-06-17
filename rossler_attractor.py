import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Model parameters
a = 0.2
b = 0.2
c = 5.7

# Position list
x_pos = []
y_pos = []
z_pos = []

def rossler(x,y,z):
    # Initial time
    dt = 0.01
    tglob = 0

    x_part = []
    y_part = []
    z_part = []

    # Simulation loop
    while tglob <=100:
        x_part.append(x)
        y_part.append(y)
        z_part.append(z)

        # Differential equations
        vx = -y -z
        vy = x + a * y
        vz = b + z * (x - c)

        x += vx * dt
        y += vy * dt
        z += vz * dt
        print(tglob)
        tglob +=dt
    
    x_pos.append(x_part)
    y_pos.append(y_part)
    z_pos.append(z_part)

x_initials = np.random.rand(5)
y_initials = np.random.rand(5)
z_initials = np.random.rand(5)

for n in x_initials:
    rossler(n,n,n)

fig = plt.figure()
ax = plt.axes(projection='3d')

for n in range(len(x_initials)):
    ax.plot(x_pos[n],y_pos[n],z_pos[n])

plt.axis('off')
plt.show()