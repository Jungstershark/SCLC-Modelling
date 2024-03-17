from numpy import roots, isreal, linspace, array
from math import exp
import matplotlib.pyplot as plt

D_bar = 10**6
step = 5000
def model_VI(D_bar, step):
    E_bar = linspace(0,62, step)
    E_bar_list = E_bar.tolist()
    E_bar_list = [i for i in E_bar_list if i!=0]
    print("E_bar_list: ", E_bar_list)

    ksi_list = []
    for E in E_bar_list:
        coeff = [1,3,0,(-1*6*D_bar*E*exp((-2)/E))]
        cubic_roots = roots(coeff)

        real_root = []
        for root in cubic_roots:
            print()
            if isreal(root): real_root.append(float(root))
        
        if len(real_root) > 1 or len(real_root)<1:
            ksi_list.append(max(real_root))
            # print("FAIL", real_root)
            # break
        else: ksi_list.extend(real_root)
    print("ksi_list: ", ksi_list)

    V_bar_list = []
    JDsq_bar_list = []
    for E_bar, ksi in zip(E_bar_list, ksi_list):
        V_bar = 0.5*(((((ksi+1)**2)-1)/(2*exp((-1)/E_bar)))**2)
        J_bar = (E_bar**2)*exp((-1)/E_bar)
        JDsq_bar = J_bar*(D_bar**2)
        
        V_bar_list.append(V_bar)
        JDsq_bar_list.append(JDsq_bar)

    print("Vbar_list: ", V_bar_list)
    print("JDsq_bar_list: ", JDsq_bar_list)

    V_bar_list, JDsq_bar_list = (list(t) for t in zip(*sorted(zip(V_bar_list,JDsq_bar_list))))
    V_bar_list.pop(0)
    JDsq_bar_list.pop(0)

    data = [V_bar_list, JDsq_bar_list]
    return data

def plot_rls(D_bar_list, D_bar_index):
    fig, ax = plt.subplots(1, 1, figsize=(6,4))
    for list, index in zip(D_bar_list, D_bar_index):
        model_vi = model_VI(list, 5000)
        V_bar_list = array(model_vi[0])
        JDsq_bar_list = array(model_vi[1])
        # ax.scatter(V_bar_list, JDsq_bar_list, linewidth=1, label=f"{index}")
        ax.plot(V_bar_list, JDsq_bar_list, linewidth=1, label=f"{index}")
    ax.set_xlabel('Vbar')
    ax.set_ylabel('JDsq')
    ax.set_title("Graph of JD^2 against V\n<-------- F-N         CL -------->")
    ax.legend()
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.show()
    return

D_bar_list = [10**5, 10**6, 10**7, 10**8, 10**9, 10**10]
D_bar_index = ["10^5","10^6","10^7","10^8","10^9","10^10"]
plot_rls(D_bar_list,D_bar_index)
