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
# def forwardMT1D(res,thick,frequency):
#     pi = np.pi
#     mu = 4 * pi * 1E-7
#     w = 2 * pi * frequency
#     # Z = np.zeros(len(res))
#     Z = np.sqrt(1j * w * mu * res[-1])
#
#     for i in range(len(res)-2,-1,-1):
#         print(i)
#         print(res[i])
#         Yj = np.sqrt(1j * w * mu * (1.0/res[i]))
#         Wj = Yj * res[i]
#         Ej = np.exp(-2 * Yj * thick[i])
#
#
#         RC = (Wj-Z)/(Wj+Z)
#         RE = RC * Ej
#         Z = Wj * ((1-RE)/(1+RE))
#
#     AppRes = (abs(Z)**2)/(mu * w)
#     Phase = np.arctan2(Z.imag,Z.real)
#
#     return AppRes,Phase


def forwardMT1D(res,thick,freq):
    mu = 4 * np.pi * 1E-7
    w = 2 * np.pi * freq
    Z = np.sqrt(1j * w * mu * res[-1])
    print(res[-1])
    for ii in range(len(res)-2,-1,-1):
        dj = np.sqrt(w * mu * (1.0/res[ii]) * 1j)
        wj = dj * res[ii]
        ej = np.exp (-2 * thick[ii]*dj)
        print(res[ii])
        rj = (wj - Z)/(wj + Z)
        re = rj*ej
        Z = wj * ((1 - re)/(1 + re))

    AppRes = (abs(Z)**2)/(mu * w)
    Phase = np.arctan2(Z.imag,Z.real)
    print("=== "*10)
    return AppRes,Phase


# def calculateJacobMT1D(res,thick,freq):
#     # dm/dx = f(m) - f(m+dm)/dm
#     for ii in range(0,len(res)):
def clear_all():
    """Clears all the variables from the workspace of the spyder application."""
    gl = globals().copy()
    for var in gl:
        if var[0] == '_': continue
        if 'func' in str(globals()[var]): continue
        if 'module' in str(globals()[var]): continue

        del globals()[var]
# if __name__ == "__main__":
#     clear_all()


# ============================================================================================
# Run Code! Run!

clear_all()

resistivity = np.array([100,100,500,500,500,100,1000])
thickness = np.ones([len(resistivity)]) * 400
freq = np.linspace(-4,4,160)
freq = 10**freq


App = np.zeros(len(freq))
Phase = np.zeros(len(freq))
for ii in range(np.size(freq)):
    App[ii],Phase[ii] = forwardMT1D(resistivity,thickness,freq[ii])

plt.subplot(121)
plt.loglog(freq,App)

plt.subplot(122)
plt.plot(np.log(freq),np.rad2deg(Phase))
plt.show()

# fig = plt.figure()
# # fig.add_subplot(121)
# fig.add_subplot(121).loglog(freq,App)
#
# fig.show()
# # fig.add_subplot(122)
# # fig.add_subplot(122).loglog(freq,Phase)
# # fig.show()

