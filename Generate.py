import numpy as np

#Fonction génére une séquence de nombres binaires aléatoirement
def Seq_Binaire (symbol, sym_len):
    #symbol: le nbr de bits
    #sym_Len: durée de chaque bit
    #generation des nombres alétoires (entre 1 and 0)
    rand_n = np.random.rand(symbol)
    rand_n[np.where(rand_n >= 0.5)] = 1
    rand_n[np.where(rand_n < 0.5)] = 0
    
    signal = np.zeros(int(symbol*sym_len))
    #generation des  symboles
    id_n = np.where(rand_n== 1)
    for i in id_n[0]:
        temp = int(i*sym_len)
        signal[temp:temp+sym_len]= 1
    return signal
