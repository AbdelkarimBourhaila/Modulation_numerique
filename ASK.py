import matplotlib.pyplot as plt
import numpy as np
import Generate as gb
Fs = 1000 #Nombre d'echantillons
T = 2 #temps de simulation(sec)
t = np.arange(0,T,1/Fs) #axe de temps
#Porteuse
Fp = 30 #Frequence de la porteuse
Ap=4
Porteuse =Ap*np.cos(2*np.pi*Fp*t)	
#Generation d'un signal numérique
Tb = 0.1; # durée d'un bit 
nbr_Ech = int(Tb*Fs) #Nombre d'echantillons dans Tb
nbr_Sym = int(np.floor(np.size(t)/nbr_Ech))
#signal numérique
sig_num = gb.Seq_Binaire(nbr_Sym, nbr_Ech)
#ASK
A=Ap+Ap*(sig_num/2)
ask = A*np.cos(2*np.pi*Fp*t)
#L'affichage
plt.subplot(3,1,1)
plt.plot(t,sig_num), plt.xlabel("t"),plt.ylabel("m(t)")
plt.title('Signal numérique (signal modulant)'),plt.grid()
plt.subplot(3,1,2)
plt.plot(t,Porteuse,'g'), plt.xlabel("t"),plt.ylabel("p(t)")
plt.title('La porteuse'),plt.grid()
plt.subplot(3,1,3)
plt.plot(t,ask,'r'), plt.xlabel("t"),plt.ylabel("S_ASK(t)")
plt.title('Signal modulé ASK'), plt.grid()
plt.tight_layout()
plt.show()
