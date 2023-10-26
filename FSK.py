import matplotlib.pyplot as plt
import numpy as np
import Generate as gb
Fs=1000 #Nombre d'echantillons
T=2 #temps de simulation(sec)
Fp=30 #Frequence de la porteuse
t = np.arange(0,T,1/Fs); #axe de temps
#Generation d'un signal numérique
Tb = 0.1; # durée d'un bit
nbr_Ech = int(Tb*Fs) #Nombre d'echantillons dans Tb
nbr_Sym = int(np.floor(np.size(t)/nbr_Ech))
#signal numérique
sig_num = gb.Seq_Binaire(nbr_Sym, nbr_Ech)
#FSK
F =Fp + Fp*(sig_num/2)
fsk = np.cos(2*np.pi*F*t)
#les porteuses (juste pour l'affichage)
Porteuse1 = np.cos(2*np.pi*Fp*t)
Porteuse2 = np.cos(np.pi*3*Fp*t)
#Affichage
plt .subplot(4,1,1)
plt.plot(t,sig_num), plt.title('Signal numérique (signal modulant)')
plt.xlabel("t"),plt.ylabel("m(t)"), plt.grid()
plt.subplot(4,1,2)
plt.plot(t,Porteuse1,'y'), plt.title('Porteuse 1')
plt.xlabel("t"),plt.ylabel("p1(t)"), plt.grid()
plt.subplot(4,1,3)
plt.plot(t,Porteuse2,'g'), plt.title('Porteuse 2')
plt.xlabel("t"),plt.ylabel("p2(t)"), plt.grid()
plt.subplot(4,1,4)
plt.plot(t,fsk,'r'), plt.title('Signal modulé FSK')
plt.xlabel("t"),plt.ylabel("S_FSK(t)")
plt .tight_layout()
plt.show()
