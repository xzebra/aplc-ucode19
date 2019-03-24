
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def isNear(a,b):
	return (abs(a-b)<=0.0001)

def notConsecutive(vector):
	toReturn = [vector[0]]
	for i in range(1,len(vector)):
		if vector[i]!=vector[i-1]+1:
			toReturn.append(vector[i])
	return toReturn


def golpeoBalon(r_xpos, r_ypos):
	fichero = "ball.csv"
	df = pd.read_csv(fichero)
	b_xpos = df.as_matrix(columns=['X'])
	b_ypos = df.as_matrix(columns=['Y'])
	if (len(r_xpos) < len(b_ypos)):
		size=len(r_xpos)
	else:
		size=len(b_ypos)
	hit = []
	for i in range(size):
		if isNear(r_xpos[i],b_xpos[i]) and isNear(r_ypos[i], b_ypos[i]):
			hit.append(i)
		
	return hit




# set file
file = 'track_points.csv'
# read file
df = pd.read_csv(file)

# get accel - left
r_xpos = df.as_matrix(columns=['X'])

r_ypos = df.as_matrix(columns=['Y'])




ax1 = plt.subplot(221)
plt.plot(r_xpos)
plt.ylabel('Pos')
plt.title('RIGHT-XPOS')

plt.subplot(222, sharex=ax1)
plt.plot(r_ypos)
plt.ylabel('Pos')
plt.title('RIGHT-YPOS')

plt.show()

golpeos = (golpeoBalon(r_xpos,r_ypos))
print(notConsecutive(golpeos))