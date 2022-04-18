
import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
  
a=30
N=1000
x=np.linspace(-a,a,N)
y=np.array([1 if np.abs(n)<=1 else 0 for n in x])

Tstep=2*a/N
X=np.linspace(-1/(Tstep*2),1/(Tstep*2),N)
Y=scipy.fft.fftshift(scipy.fft(y))


plt.figure()
plt.plot(x,y)
plt.show()

plt.figure()
plt.plot(X,np.abs(Y))
plt.show()

