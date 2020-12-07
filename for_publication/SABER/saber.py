import numpy as np
import math
import random
from params import *


class R_q:
    def __init__(self, array):
        self.values = array


    def __add__(self, other):
        for i in range(n):
            self.values[i] = self.values[i] + other.values[i]
            self.values[i] = self.values[i] % q
        return self

    def __sub__(self, other):
        for i in range(n):
            self.values[i] = self.values[i] - other.values[i]
            self.values[i] = self.values[i] % q
        return self
    
    def __mul__(self, other):
        p1 = self.values
        p2 = other.values
        ret = np.zeros(n)
        for i in range(n):
            for j in range(n):
                temp = i+j
                flag = 1
                if temp >= 256:
                    temp -= 256
                    flag = -1
                ret[temp] += flag*(p1[i]*p2[j])
                ret[temp]%=q
        return R_q(ret)
    

def binomial_distribution():
    array = np.zeros(n)
    sum = 0
    for i in range(n):
        for j in range(mu//2):
            sum += random.randint(0, 1)-random.randint(0, 1)
        array[i] = sum
        sum = 0
    return R_q(array)

def uniform_distribution():
    return R_q(np.random.randint(0, q, n))

#h1: num = 1, h2: num = 2
def constant_h(num):
    cst=0
    if num == 1:
        cst = pow(2, eq-ep-1)
    elif num==2:
        cst = pow(2, ep-2)-pow(2, ep-et-1)+pow(2, eq-ep-1)
    coeffs = np.zeros(n,dtype = int)
    for i in range(n):
        coeffs[i] = cst
    return R_q(coeffs)


#bit shift
def bit_shift(num, poly):
    for i in range(n):
        poly.values[i] = poly.values[i]>>num
    return poly
    
