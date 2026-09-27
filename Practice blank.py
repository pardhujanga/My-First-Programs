# %% Defining and solving the Hamiltonian for a 2D lattice with open boundary conditions
import numpy as np
import scipy.sparse as sp
from scipy import linalg
from matplotlib import pyplot as plt

L=30

def kron(x,y):
    if x == y:
        return 1
    else:
        return 0


index = range(L**2)
length = range(L)

H = np.zeros((L**2,L**2),dtype=np.complex128) #intializing the hamiltonian 

for i in index:
    for x in length:
        for y in length:
            if x!=0 and x!=L-1:
                H[i][L*y + x] = - kron(i,L*y+(x-1)) - kron(i,L*y+(x+1)) - kron(i,L*((y-1))+x) - kron(i,L*((y+1))+x)
            elif x==0:
                H[i][L*y + x] = - kron(i,L*y+(x+1)) - kron(i,L*((y-1))+x) - kron(i,L*((y+1))+x)
            elif x==L-1:
                H[i][L*y + x] = - kron(i,L*y+(x-1)) - kron(i,L*((y-1))+x) - kron(i,L*((y+1))+x)
#NOTE Needed to split the hamiltoninan generation as the way the lattice to avoid interactions between
# endpoints of consecutive "lines of atoms"

#solving for spectrum and eigenfunctions
val, vec = linalg.eig(H)


# %% Plotting the energy spectrum
x = np.pi*np.array(range(L))/(L-1)
cos = np.cos(x)
theory = []
for i in cos:
    for j in cos:
        theory.append(2*i+2*j)

sorted = np.sort(theory)

ordered_val = np.sort(val)
plt.plot(ordered_val,'k')
plt.plot(sorted)
plt.show()

# %%
print(np.argmax(val))

# %%
n=9
# %%  Defining a function to find the expansion of eigenfunctions in the lattice basis
eigf = np.abs(vec[:,n])

# defining the lattice
X, Y = np.meshgrid(np.linspace(0,L-1,L,dtype=int), np.linspace(0,L-1,L,dtype=int))
Z = eigf[L*Y + X]

# plot
fig, ax = plt.subplots()

im = ax.imshow(Z, cmap='plasma')
ax.set_title("absolute value of eigenfunction on the lattice")
fig.colorbar(im)
plt.show()


# %% plotting the phase of the eigenfunctions
phase = np.angle(vec[:,n])

#defining the lattice
X, Y = np.meshgrid(np.linspace(0,L-1,L,dtype=int), np.linspace(0,L-1,L,dtype=int))
Zp = phase[L*Y + X]

# plot
fig, ax = plt.subplots()

im = ax.imshow(Zp, cmap='plasma')
ax.set_title("phase of eigenfunction on the lattice")
fig.colorbar(im)
plt.show()
# %% to get an idea of which eigenfunction will be seen for what n as they can't be sorted
plt.plot(val)
plt.show()
# %%
