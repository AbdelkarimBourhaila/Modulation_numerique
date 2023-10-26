import matplotlib.pyplot as plt
import numpy as np
import Generate as gb
Fs=1000 #Nombre d'echantillons
T=2 #temps de simulation(sec)
Fp = 20 #Frequence de la porteuse
t = np.arange(0,T,1/Fs); #axe de temps
#Generation d'un signal numérique
Tb = 0.1; # durée d'un bit
nbr_Ech = int(Tb*Fs) #Nombre d'echantillons dans Tb
nbr_Sym = int(np.floor(np.size(t)/nbr_Ech))
#signal numérique
sig_num = gb.Seq_Binaire(nbr_Sym, nbr_Ech)
# PSK
fi = 0 #phase pour symble 0
fi = fi + np.pi*sig_num #phase pour symble 1
psk = np.cos((2*np.pi*Fp*t) +fi)
Porteuse = np.cos(2*np.pi*Fp*t) #juste pour l'affichage
#L'affichage
plt.subplot(3,1,1)
plt.plot(t,sig_num); plt.title('Signal numérique (signal modulant)')
plt.xlabel("t"),plt.ylabel("m(t)"),plt.grid()
plt.subplot(3,1,2)
plt.plot(t,Porteuse,'g'); plt.title('La porteuse')
plt.xlabel("t"),plt.ylabel("p(t)"),plt.grid()
plt.subplot(3,1,3)
plt.plot(t,psk,'r'), plt.title('Signal modulé PSK')
plt.xlabel("t"),plt.ylabel("S_PSK(t)")
plt .tight_layout()
plt.show()
