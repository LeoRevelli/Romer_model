# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:57:25 2022

@author: leore
"""

import math as m
import numpy as np
import pylab
s=0
alpha=0.25
beta=0.25
S=[ ]
C=[ ]
while s<1:
    K=1
    A=1
    L=1
    R=1
    Y=K**(0.5)*(A*L)**(0.5)
    t=0
    while t<15:
        x=np.random.random()
        g=-0.05*x+(0.08)*x
        A=A+g*A
        n=0.02
        L=L+n*L
        d=0.05
        K=K+s*Y-d*K
        Y=K**(alpha)*(A*L)**(beta)*R**(1-alpha-beta)
        L_=L**(beta)*R**((1-alpha-beta)/2)
        A_=A**(beta)*R**((1-alpha-beta)/2)
        L_=L_+L_*((n*beta)/(1-alpha))
        A_=A_+A_*((g*beta)/(1-alpha))
        Y=K**alpha*(A_*L_)**1-alpha
        Y=Y+Y*((n*beta)/(1-alpha)+(g*beta)/(1-alpha))
        P=Y/(A*L)
        t=t+1
    S=S+[s]
    c=P-s*P
    C=C+[c]
    s=s+0.01
pylab.plot(S,C)
 
"""L_=L**(beta)*R**((1-alpha-beta)/2)
A_=A**(beta)*R**((1-alpha-beta)/2)
L_=L_+L_*((n*beta)/(1-alpha))
A_=A_+A_*((g*beta)/(1-alpha))
Y=K**alpha*(A_*L_)**1-alpha
Y=Y+Y*((n*beta)/(1-alpha)+(g*beta)/(1-alpha))"""