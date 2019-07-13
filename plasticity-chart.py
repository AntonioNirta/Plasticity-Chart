import matplotlib.pyplot as plt
import numpy as np

IP=[6,11,5,8,6,6,6,6,11,12,8,10,8]
WL=[33,35,21,36,22,26,30,27,32,33,31,32,32]

#################################
a=0
a1=0
b=60
b1=60
plt.plot([a,b],[a1,b1], '-', color='black', linewidth=0.8)
#################################

#######################U-line######################
x=[16,16,16]
y=[0,2,4]
plt.plot(x, y, '--', color='gray', linewidth=0.8)

wl=[17.29,20.42,30.83,50,51.67,62.08,72.50]
ip=[7,10,20,38.40,40,50,60]
plt.plot(wl,ip, '--', color='gray', linewidth=0.8)
###################################################

#######################A-line######################
wl=[25.48,33.70,47.40,61.10,74.79,88.49,102.19]
ip=[4,10,20,30,40,50,60]
plt.plot(wl,ip, '-', color='black', linewidth=0.8)
###################################################

#######################CL-ML#######################
x=[4,10,20,25.48]
y=[4,4,4,4]
plt.plot(x,y, '-', color='black', linewidth=0.8)

x2=[7,10,20,29.59]
y2=[7,7,7,7]
plt.plot(x2,y2, '-', color='black', linewidth=0.8)
###################################################

#######################WL=50%####################################
plt.axvline(x=50, ymin=0,ymax=0.64, color='black', linewidth=0.8)

#IMPOSTO LE ETICHETTE DA METTERE NELLE PORZIONI DELLA CARTA#
ch= 'CH or OH'
mh= 'MH or OH'
cl= 'CL or OL'
ml='ML or OL'
cl_ml='CL-ML'

plt.text(70,50, ch) #PLOTTO ETICHETTA NELLA CARTA
plt.text(75,22, mh) #PLOTTO ETICHETTA NELLA CARTA
plt.text(42,25, cl) #PLOTTO ETICHETTA NELLA CARTA
plt.text(39,7, ml) #PLOTTO ETICHETTA NELLA CARTA
plt.text(15,5, cl_ml) #PLOTTO ETICHETTA NELLA CARTA

def addtext(props):
    plt.text(45, 35, 'U-line', props, rotation=45)
    plt.text(62, 32, 'A-line', props, rotation=35)

addtext({'ha': 'left', 'va': 'bottom'})

########Creazione grafico ed inserimento campioni###########
plt.axis([0, 100, 0, 60])

plt.xlabel('WL(%)')
plt.ylabel('IP(%)')

plt.plot(WL,IP, 'or')

plt.show()
