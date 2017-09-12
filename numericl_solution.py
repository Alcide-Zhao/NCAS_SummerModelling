import numpy as np
import matplotlib.pyplot as plt

##initial condition
def IniCon (x):
    return np.where (x%1. <0.5, np.power(np.sin(2*x*np.pi), 2), 0)

# setup space and courant number
nx =40        # number of points in space
# spatial points given from 0 to 1 
x = np.linspace(0.0,1.0,nx)
vel = IniCon (x)
velN = vel.copy();  velO = vel.copy()

def FiniteDiff (Uj,Uj_1):
    """
    THis is to derive  U[j,n+1] from u[j,n] and u[j-1,n] given 
    the initial condition and using the finite difference methods
    input : u[j] and u[j-1] at the former step
    output: u[j] at time stp n+1
    """
    c = 0.1       # the conurant number c =del(t)/ del(x)
    uj = uj*(1-c*(uj-uj_1))
    return uj

## for the first time step
# loop over space 
for j in xrange(1,nx):
    uj = velO[j];Uj_1 = velO[j-1]; vel[j] = FiniteDif(Uj,Uj_1);)
    #vel[j] = velO[j]* (1-c*( velO[j]- velO[j-1]));
vel[0] = FiniteDiff(velO[0],velO[nx-1])
# velO[0]* (1-c*( velO[0]- velO[nx-1])); vel[nx-1] = vel[0];

# loop over remainding time-steps (nt)
nt =40

for n in xrange(1,nt):
    # loop over space
    for j in xrange(1,nx):
	velN[j] = FIniteDiff()   #velO[j]* (1-c*( vel[j]- vel[j-1]))
        velN[j] = velO[j]* (1-c*( vel[j]- vel[j-1]))
    velN[0] = velO[0]* (1-c*( vel[0]- vel[nx-1])); velN[nx-1] = vel[0];
    velO = vel.copy(); vel = velN.copy()

# derived quantities 

plt.plot(x, vel,'r',label='Mine')
plt.legend(loc=1)
plt.xlabel('x')
plt.ylabel('Velocity')
plt.axhline(0,color='k')
plt.show()





    
