"""
  Created on :
    18:40 GMT+7 - 07 Mar 2019 
  Author     :
    github.com/71unxv
    github.com/
______________________________________________________________________________________________
  Note       :
    Python For Geophysical data processing and Inverse Problem    
______________________________________________________________________________________________
    
   Cheers!
"""
# ============================================================================================
# Import Library
import numpy as np
import matplotlib.pyplot as plt


# ============================================================================================
# Function
def forwardMT1D(res,thick,frequency):
    pi = np.pi
    mu = 4 * pi * 1e-7
    w = 2 * pi * frequency
    # Z = np.zeros(len(res))
    Z = np.sqrt(1j * w * mu * res[-1])

    for i in np.arange(len(res)-2,0,-1):
        Yj = np.sqrt(1j * w * (1/res[i]))
        Ej = np.exp(-2 * Yj * thick[i])
        Wj = Yj * res[i]

        RC = (Wj-Z+1)/(Wj+Z+1)
        Z = Wj * ((1-(RC*Ej))/(1+(RC*Ej)))

    AppRes = (abs(Z)**2)/w
    Phase = np.arctan(np.imag(Z)/np.real(Z))
    return AppRes,Phase

def calculateJacobMT1D(res,thick,freq):
    # dm/dx = f(m) - f(m+dm)/dm
    for ii in range
# ============================================================================================
# Run Code! Run!



resistivity = np.array([100,1000,100])
thickness = np.ones([len(resistivity)]) * 500
freq = np.linspace(-4,4,30)
freq = 10**freq

App = np.zeros(len(freq))
Phase = App[:]

for ii in range(np.size(freq)):
    App[ii],Phase[ii] = forwardMT1D(resistivity,thickness,freq[ii])

plt.loglog(freq,App)
plt.show()

# fig = plt.figure()
# # fig.add_subplot(121)
# fig.add_subplot(121).loglog(freq,App)
#
# fig.show()
# # fig.add_subplot(122)
# # fig.add_subplot(122).loglog(freq,Phase)
# # fig.show()

