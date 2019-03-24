from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file = 'ball_track.csv'
# read file
df = pd.read_csv(file)


info = df.as_matrix(columns=['X', 'Y', 'Height', 'Width'])

vx = []
vy = []
vh = []
#vw = []

for i in range(len(info)):
	vx.append(info[i][0])

for i in range(len(info)):
	vy.append(info[i][1])

for i in range(len(info)):
	vh.append(info[i][2])
	
#for i in range(len(r_pos)):
#	vw.append(info[i][3])
	
# Creamos la figura
fig = plt.figure()

# Agrrgamos un plano 3D
ax1 = fig.add_subplot(111,projection='3d')

relativeSize = [0]

for i in range(1,len(vh)):
	relativeSize.append(vh[i]-vh[i-1])


ax1 = plt.subplot(221)
plt.plot(vx)
plt.ylabel('Pos')
plt.title('Ancho')

plt.subplot(222, sharex=ax1)
plt.plot(vy)
plt.ylabel('Pos')
plt.title('Altitud')

plt.subplot(223, sharex=ax1)
plt.plot(relativeSize)
plt.ylabel('Lejania balón')
plt.title('Profundidad')


# Mostramos el gráfico
plt.show()

fig = plt.figure()

# Agrrgamos un plano 3D
ax1 = fig.add_subplot(111,projection='3d')

# Datos en array bi-dimensional
x = np.array([vx])
y = np.array([vh])
z = np.array([vy])

# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
ax1.plot_wireframe(x, y, z)

# Mostramos el gráfico
plt.show()