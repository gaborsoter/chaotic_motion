import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

array_x = []
array_y = []
array_i = []

plt.rcParams.update({'font.size': 7})

x = 0.2
y = 0.2 + 0.0000000001

for i in range(60):
	x = 4*x*(1-x)
	y = 4*y*(1-y)
	array_x.append(x)
	array_y.append(y)
	array_i.append(i)

array_x = np.array(array_x)
array_y = np.array(array_y)
array_i = np.array(array_i)

fig, ax = plt.subplots(figsize = (4.8, 3.5))
ax.set_color_cycle(["#323A45", "#5FAEB6"])
line,  = ax.plot(array_i, array_x, marker='o', markersize = 3)
line2, = ax.plot(array_i, array_y, marker='o', markersize = 3)

def update(num, array_i, array_x, array_y, line, line2):
    line.set_data(array_i[:num], array_x[:num])
    line.axes.axis([0, 50, -0.5, 1.5])
    line2.set_data(array_i[:num], array_y[:num])
    line2.axes.axis([0, 50, -0.5, 1.5])
    return line, line2,

ax.set_xlabel('Number of iterations')
ax.set_ylabel('x')
ax.set_ylim(-0.5, 1.5)
plt.legend([r'$x_{0} = 0.2 $', r'$x_{0} = 0.2 + 1E-10 $'])

ani = animation.FuncAnimation(fig, update, len(array_i), fargs=[array_i, array_x, array_y, line, line2],
                              interval=45, blit=True)
ani.save("test.mp4", dpi=300)
plt.show()
plt.close()