from math import exp, pi
from numpy import linspace, array
import matplotlib.pyplot as plt



e = 1.60217663*(10**(-19)) #--> electron charge(eV)
#Change to SI Units
Φ = 2*e #--> work function (eV) mobility
T=300 #--> electrode temperature (K) - Room Temperature
J = (120*(T**2)*exp((-11606*Φ)/T))/10000 #--> current density (amp/m^2)
D = 10**7

Es = 100 #--> Surface electric field
Ep = 8.85418782*(10**(-12)) #--> Permitivity of free space (m^-3 kg^-1 s^4 A^2)
µ = 0.14 #--> silicon
m = 9.1093837*(10**(-31)) #--> mass of e (kg)
t = linspace(0,100, 1000)


vt = µ*((µ/e)*(((J/Ep)*µ)-((e*Es)/m))*(exp(-1*(e/(m*µ)))-1)+((J/Ep)*t))
xt = µ*((µ/e)*(((J/Ep)*µ)-((e*Es)/m))*(((-1*(m*µ)/e)*exp(-1*(e/(m*µ))))-t+((m*µ)/e))+(J/(2*Ep))*(t**2))
vt_list = array([vt for t in t])
print(vt_list)
xt_list = array([xt for t in t])
print(xt_list)


def plot_xt(xt, t):
    fig, ax = plt.subplots(1, 1, figsize=(10,5))
    ax.plot(xt, t, linewidth=1, label="xt")
    ax.set_xlabel('time')
    ax.set_ylabel('')
    ax.set_title("x against t")
    ax.legend()
    plt.show()
    return

        
def plot_vt(vt, t):
    fig, ax = plt.subplots(1, 1, figsize=(10,5))
    ax.plot(vt, t, linewidth=1, label="vt")
    ax.set_xlabel('time')
    ax.set_ylabel('')
    ax.set_title("v against t")
    ax.legend()
    plt.show()
    return

plot_xt(xt,t)
plot_vt(vt,t)