# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 12:42:39 2015

@author: matevzk
"""

from podatkovneStrukture import skladPush, skladPop
import numpy as np

def pretvoriBinarno( n, x ):
    # n = število ki ga pretvarjamo
    # x = število bitov

    sklad = np.ones(x)*99;
    
    while n > 0:
        bit = n%2;
        [sklad,stat] = skladPush(sklad,bit);
        n = np.floor(n/2);
        bit = 0;
    
    return sklad   
    
def pretvoriDecimalno(biti):
    cifra = 0;
    b = [i for i,x in enumerate(biti) if x != 99];
    b = len(b);
    potenca = 2**(b-1);
    [biti,s,d] = skladPop(biti);
    while s == 1:
        cifra = cifra + potenca * d;
        potenca = potenca / 2;
        [biti,s,d] = skladPop(biti);
        
    return cifra
    

#primer
x = pretvoriBinarno(10,5)
print "10 v binarnem zapisu" , x

print "0101 decimalno", pretvoriDecimalno(x)