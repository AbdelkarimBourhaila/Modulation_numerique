from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import Generate as gb
#Fenetre principale
w_principal=Tk()
w_principal.geometry('960x540')
w_principal.title("Modulation")
w_principal.config(background="#ffffff")
#Paramètres d'affichage
Fs = 10000 #Nombre d'echantillons
T = 1 #temps de simulation(sec)
t = np.arange(0,T,1/Fs) #axe de temps
#t = np.linspace(0, 1, 500)
#Generation d'un signal numérique
Td = 0.1; # durée d'un bit
nbr_Ech = int(Td*Fs)#Nombre d'echantillons dans Tb
nbr_Sym = int(np.floor(np.size(t)/nbr_Ech))
#signal numérique
sig_num = gb.Seq_Binaire(nbr_Sym, nbr_Ech)

#***********************************La modulation OOK********************************
def OOK():
    #Porteuse
    Porteuse = Ap*np.cos(2*np.pi*Fp*t)
    #Generate OOK
    ook = Porteuse * sig_num
    #Afichage
    plt.subplot(3,1,1)
    plt.plot(t,sig_num), plt.title('Signal numérique (modulant)'), plt.xlabel("t"),plt.ylabel("m(t)"), plt.grid()
    plt.subplot(3,1,2), plt.plot(t,Porteuse,'r'),plt.title('La porteuse'), plt.xlabel("t"),plt.ylabel("p(t)"), plt.grid()
    plt.subplot(3,1,3), plt.plot(t,ook,'g'), plt.title('Signal modulé OOK'), plt.xlabel("t"),plt.ylabel("S_OOK(t)"), plt.grid()
    plt.tight_layout(), plt.show()

def OOk_GUI():
    w_OOK = Toplevel(w_principal)
    w_OOK.geometry('600x380'), w_OOK.title("OOK"), w_OOK.config(background="#ffffff")
    OOK_lbl=Label(w_OOK, text="La modulation OOK", font=('Roboto',30,'bold'), fg='#ed7d31', bg='white')
    OOK_lbl.place(x=100,y=10)
    OOK_btn=Button(w_OOK, text="Afficher le signal modulé OOK", font=("Comic Sans Ms",16), command=OOK, fg='#ffffff', bg='#ed7d31')
    OOK_btn.place(x=150,y=270)
    def enterAp():
        global Ap
        Ap=float(OOK_Ap_ent.get())
        print("Ap = ",Ap)

    def enterFp():
        global Fp
        Fp=float(OOK_Fp_ent.get())
        print("Fp = ",Fp)

    #les éléments de(OOK_GUI)
    OOK_Ap_lbl=Label(w_OOK,text="Ap = ",font=('Roboto',16,'bold'), bg='white')
    OOK_Ap_lbl.place(x=215,y=90)
    OOK_Ap_ent=Entry(w_OOK, relief=SOLID)
    OOK_Ap_ent.place(x=270,y=95)
    OOK_Fp_lbl=Label(w_OOK,text="Fp = ",font=('Roboto',16,'bold'), bg='white')
    OOK_Fp_lbl.place(x=215,y=140)
    OOK_Fp_ent=Entry(w_OOK, relief=SOLID)
    OOK_Fp_ent.place(x=270,y=145)
    OOK_btn=Button(w_OOK, text="Entrer Ap", font=("Comic Sans Ms",16), command=enterAp, fg='#ffffff', bg='#ed7d31')
    OOK_btn.place(x=180,y=200)
    OOK_btn=Button(w_OOK, text="Entrer Fp", font=("Comic Sans Ms",16), command=enterFp, fg='#ffffff', bg='#ed7d31')
    OOK_btn.place(x=310,y=200)

#**********************************La modulation ASK*********************************** 
def ASK():
    #Porteuse
    Porteuse = Ap*np.cos(2*np.pi*Fp*t)
    #Generate ASK
    A=Ap+Ap*(sig_num/2)
    ask = A*np.cos(2*np.pi*Fp*t)
    #Afichage
    plt.subplot(3,1,1)
    plt.plot(t,sig_num), plt.title('Signal numérique (modulant)'), plt.xlabel("t"),plt.ylabel("m(t)"), plt.grid()
    plt.subplot(3,1,2), plt.plot(t,Porteuse,'r'),plt.title('La porteuse'), plt.xlabel("t"),plt.ylabel("p(t)"), plt.grid()
    plt.subplot(3,1,3), plt.plot(t,ask,'g'), plt.title('Signal modulé ASK'), plt.xlabel("t"),plt.ylabel("S_ASK(t)"), plt.grid()
    plt.tight_layout()
    plt.show()

def ASK_GUI():
    w_ASK = Toplevel(w_principal)
    w_ASK.geometry('600x380'), w_ASK.title("ASK"), w_ASK.config(background="#ffffff")
    ASK_lbl=Label(w_ASK, text="La modulation ASK", font=('Roboto',30,'bold'), fg='#ed7d31', bg='white')
    ASK_lbl.place(x=100,y=10)
    ASK_btn=Button(w_ASK, text="Afficher le signal modulé ASK", font=("Comic Sans Ms",16), command=ASK, fg='#ffffff', bg='#ed7d31')
    ASK_btn.place(x=150,y=300)
    def enterAp():
        global Ap
        Ap=float(ASK_Ap_ent.get())
        print("Ap = ",Ap)

    def enterFp():
        global Fp
        Fp=float(ASK_Fp_ent.get())
        print("Fp = ",Fp)

    #les éléments de(ASK_GUI)
    ASK_Ap_lbl=Label(w_ASK,text="Ap = ",font=('Roboto',16,'bold'), bg='white')
    ASK_Ap_lbl.place(x=215,y=130)
    ASK_Ap_ent=Entry(w_ASK, relief=SOLID)
    ASK_Ap_ent.place(x=270,y=135)
    Info_ASK_lbl=Label(w_ASK,text="Amplitude de niveau haut : Ap\nAmplitude de niveau bas : Ap/2 ",font=('Roboto',14), bg='white')
    Info_ASK_lbl.place(x=150,y=72)
    ASK_Fp_lbl=Label(w_ASK,text="Fp = ",font=('Roboto',16,'bold'), bg='white')
    ASK_Fp_lbl.place(x=215,y=180)
    ASK_Fp_ent=Entry(w_ASK, relief=SOLID)
    ASK_Fp_ent.place(x=270,y=185)
    ASK_btn=Button(w_ASK, text="Entrer Ap", font=("Comic Sans Ms",16), command=enterAp, fg='#ffffff', bg='#ed7d31')
    ASK_btn.place(x=180,y=240)
    ASK_btn=Button(w_ASK, text="Entrer Fp", font=("Comic Sans Ms",16), command=enterFp, fg='#ffffff', bg='#ed7d31')
    ASK_btn.place(x=310,y=240)


#**********************************La modulation FSK*********************************** 
def FSK():
    #Porteuse
    Porteuse1 = Ap*np.cos(2*np.pi*Fp*t)
    Porteuse2 = Ap*np.cos(np.pi*Fp*t)
    #Generate FSK
    F = Fp + Fp*(sig_num/2)
    fsk = Ap*np.cos(2*np.pi*F*t)
    #Afichage
    plt.subplot(4,1,1)
    plt.plot(t,sig_num), plt.title('Signal numérique (modulant)'), plt.xlabel("t"),plt.ylabel("m(t)"), plt.grid()
    plt.subplot(4,1,2), plt.plot(t,Porteuse1,'r'),plt.title('La porteuse 1'), plt.xlabel("t"),plt.ylabel("p1(t)"), plt.grid()
    plt.subplot(4,1,3), plt.plot(t,Porteuse2,'r'),plt.title('La porteuse 2'), plt.xlabel("t"),plt.ylabel("p2(t)"), plt.grid()
    plt.subplot(4,1,4), plt.plot(t,fsk,'g'), plt.title('Signal modulé FSK'), plt.xlabel("t"),plt.ylabel("S_FSK(t)"), plt.grid()
    plt.tight_layout()
    plt.show()

def FSK_GUI():
    w_FSK = Toplevel(w_principal) 
    w_FSK.geometry('600x380'), w_FSK.title("FSK"), w_FSK.config(background="#ffffff")
    FSK_lbl=Label(w_FSK, text="La modulation FSK", font=('Roboto',30,'bold'), fg='#ed7d31', bg='white')
    FSK_lbl.place(x=100,y=10)
    FSK_btn=Button(w_FSK, text="Afficher le signal modulé FSK", font=("Comic Sans Ms",16), command=FSK, fg='#ffffff', bg='#ed7d31')
    FSK_btn.place(x=150,y=300)
    def enterAp():
        global Ap
        Ap=float(FSK_Ap_ent.get())
        print("Ap = ",Ap)

    def enterFp():
        global Fp
        Fp=float(FSK_Fp_ent.get())
        print("Fp = ",Fp)

    #les éléments de(FSK_GUI)
    FSK_Ap_lbl=Label(w_FSK,text="Ap = ",font=('Roboto',16,'bold'), bg='white')
    FSK_Ap_lbl.place(x=215,y=130)
    FSK_Ap_ent=Entry(w_FSK, relief=SOLID)
    FSK_Ap_ent.place(x=270,y=135)
    Info_FSK_lbl=Label(w_FSK,text="Fréquence de niveau haut : Fp\nFréquence de niveau bas : Fp/2 ",font=('Roboto',14), bg='white')
    Info_FSK_lbl.place(x=150,y=72)
    FSK_Fp_lbl=Label(w_FSK,text="Fp = ",font=('Roboto',16,'bold'), bg='white')
    FSK_Fp_lbl.place(x=215,y=180)
    FSK_Fp_ent=Entry(w_FSK, relief=SOLID)
    FSK_Fp_ent.place(x=270,y=185)
    FSK_btn=Button(w_FSK, text="Entrer Ap", font=("Comic Sans Ms",16), command=enterAp, fg='#ffffff', bg='#ed7d31')
    FSK_btn.place(x=180,y=240)
    FSK_btn=Button(w_FSK, text="Entrer Fp", font=("Comic Sans Ms",16), command=enterFp, fg='#ffffff', bg='#ed7d31')
    FSK_btn.place(x=310,y=240)


#**********************************La modulation PSK*********************************** 
def PSK():
    #Porteuse
    Porteuse = Ap*np.cos(2*np.pi*Fp*t)
    #Generate PSK
    phi = Phi + np.pi*sig_num
    psk = np.cos((2*np.pi*Fp*t) +phi)
    #Afichage
    plt.subplot(3,1,1)
    plt.plot(t,sig_num), plt.title('Signal numérique (modulant)'), plt.xlabel("t"),plt.ylabel("m(t)"), plt.grid()
    plt.subplot(3,1,2), plt.plot(t,Porteuse,'r'),plt.title('La porteuse'), plt.xlabel("t"),plt.ylabel("p(t)"), plt.grid()
    plt.subplot(3,1,3), plt.plot(t,psk,'g'), plt.title('Signal modulé PSK'), plt.xlabel("t"),plt.ylabel("S_PSK(t)"), plt.grid()
    plt.tight_layout()
    plt.show()

def PSK_GUI():
    w_PSK = Toplevel(w_principal) 
    w_PSK.geometry('600x380'), w_PSK.title("PSK"), w_PSK.config(background="#ffffff")
    PSK_lbl=Label(w_PSK, text="La modulation PSK", font=('Roboto',30,'bold'), fg='#ed7d31', bg='white')
    PSK_lbl.place(x=100,y=10)
    PSK_btn=Button(w_PSK, text="Afficher le signal modulé PSK", font=("Comic Sans Ms",16), command=PSK, fg='#ffffff', bg='#ed7d31')
    PSK_btn.place(x=150,y=310)
    def enterAp():
        global Ap
        Ap=float(PSK_Ap_ent.get())
        print("Ap = ",Ap)

    def enterFp():
        global Fp
        Fp=float(PSK_Fp_ent.get())
        print("Fp = ",Fp)

    def enterPhi():
        global Phi
        Phi=float(PSK_Phi_ent.get())
        print("Phi = ",Phi)
        return Phi

    #les éléments de(PSK_GUI)
    Info_PSK_lbl=Label(w_PSK,text="Phase de niveau bas : Phi (en rad)\nPhase de niveau haut : Phi+pi (en rad)",font=('Roboto',14), bg='white')
    Info_PSK_lbl.place(x=150,y=72)
    PSK_Ap_lbl=Label(w_PSK,text="Ap = ",font=('Roboto',16,'bold'), bg='white')
    PSK_Ap_lbl.place(x=155,y=135)
    PSK_Ap_ent=Entry(w_PSK, relief=SOLID)
    PSK_Ap_ent.place(x=215,y=140)
    PSK_Fp_lbl=Label(w_PSK,text="Fp = ",font=('Roboto',16,'bold'), bg='white')
    PSK_Fp_lbl.place(x=155,y=190)
    PSK_Fp_ent=Entry(w_PSK, relief=SOLID)
    PSK_Fp_ent.place(x=215,y=195)
    PSK_Phi_lbl=Label(w_PSK,text="Phi = ",font=('Roboto',16,'bold'), bg='white')
    PSK_Phi_lbl.place(x=155,y=250)
    PSK_Phi_ent=Entry(w_PSK, relief=SOLID)
    PSK_Phi_ent.place(x=215,y=255)
    PSK_btn=Button(w_PSK, text="Entrer Ap", font=("Comic Sans Ms",14), command=enterAp, fg='#ffffff', bg='#ed7d31')
    PSK_btn.place(x=350,y=129)
    PSK_btn=Button(w_PSK, text="Entrer Fp", font=("Comic Sans Ms",14), command=enterFp, fg='#ffffff', bg='#ed7d31')
    PSK_btn.place(x=350,y=183)
    PSK_btn=Button(w_PSK, text="Entrer Phi", font=("Comic Sans Ms",14), command=enterPhi, fg='#ffffff', bg='#ed7d31')
    PSK_btn.place(x=350,y=242)


Principal_lbl=Label(w_principal, text="La modulation numérique", font=('Roboto',40,'bold'), fg='#ed7d31', bg='white')
Principal_lbl.place(x=150,y=15)
Principal_OOK_btn=Button(w_principal, text="OOK (On-OFF-Keing)", font=("Comic Sans Ms",25), command=OOk_GUI, fg='#ffffff', bg='#ed7d31')
Principal_OOK_btn.place(x=270,y=120)
Principal_ASK_btn=Button(w_principal, text="ASK (Amplitude shift Keing)", font=("Comic Sans Ms",25), command=ASK_GUI, fg='#ffffff', bg='#ed7d31')
Principal_ASK_btn.place(x=200,y=220)
Principal_FSK_btn=Button(w_principal, text="FSK (Frequency shift Keing)", font=("Comic Sans Ms",25), command=FSK_GUI, fg='#ffffff', bg='#ed7d31')
Principal_FSK_btn.place(x=200,y=320)
Principal_PSK_btn=Button(w_principal, text="PSK (Phase shift Keing)", font=("Comic Sans Ms",25), command=PSK_GUI, fg='#ffffff', bg='#ed7d31')
Principal_PSK_btn.place(x=240,y=420)
w_principal.mainloop()
