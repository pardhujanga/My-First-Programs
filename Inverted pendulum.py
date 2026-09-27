import numpy as np
import matplotlib.pyplot as plt

#Is there a way to find out a relation between the parameters to determine when
#becomes stable? when does it stay in on a straight line
theta0=0.1
g=10
l=1
A=0.1
w=44.818
Theta=theta0
dotTheta=0
theta=[]
dt=0.00001

for t in np.arange(0,10,dt):
    ddotTheta=((g/l)-((A*w**2)/l)*np.cos(w*t))*Theta
    Theta+=(dotTheta)*(dt)
    dotTheta+=(ddotTheta)*(dt)
    theta.append(Theta)   

plt.xlabel('time')
plt.ylabel('theta')
plt.title('Inverted Pendulum')
plt.plot(theta)
plt.show()

