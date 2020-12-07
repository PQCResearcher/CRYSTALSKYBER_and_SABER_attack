from saber import *

def saber_oracle(PA, sB):
    m = R_q(np.random.randint(0, 2, n))
    for i in range(n):
        m.values[i] *= (p//2) 
    vB = R_q(np.zeros(n,dtype = int))
    for i in range(k):
        vB += PA[i]*sB[i]
    for i in range(n):
        vB.values[i] %= p
    c = R_q(np.zeros(n,dtype = int))
    c = vB+constant_h(1)-m
    for i in range(n):
        c.values[i] %= p
    c = bit_shift(ep-et, c)
    return c

def FireSaber_attack(sB):
    B = 16
    ans_sB = []
    for i in range(k):
        PA = []
        for j in range(k):
            PA.append(R_q(np.zeros(n)))
        PA[i].values[0] = B
        c = saber_oracle(PA, sB)
        temp = []
        for l in range(n):
            if c.values[l]>=2**(et-1)-mu and c.values[l]<=2**(et-1)+mu:
                temp.append(c.values[l]-2**(et-1))
            elif c.values[l]<=mu:
                temp.append(c.values[l])
            else:
                temp.append(c.values[l]-2**et)
        ans_sB.append(temp)
    return ans_sB

def Saber_attack(sB):
    ans_sB = []
    for i in range(k):
        temp = np.full(n, 100)
        for B in [64, 96]:
            PA = []
            for j in range(k):
                PA.append(R_q(np.zeros(n)))
            PA[i].values[0] = B
            c = saber_oracle(PA,sB)
            if B == 64:
                for l in range(n):
                    if c.values[l] == 4 or c.values[l] == 12:
                        continue
                    elif c.values[l] >=5 and c.values[l] <= 11:
                        temp[l] = c.values[l]-2**(et-1)
                    elif c.values[l] >= 0 and c.values[l] <= 3:
                        temp[l] = c.values[l]
                    else:
                        temp[l] = c.values[l]-(2**et)
            else:
                for l in range(n):
                    if temp[l] == 100:
                        if c.values[l] == 2 or c.values[l] == 10 :
                            temp[l] = -4
                        elif c.values[l] == 6 or c.values[l] == 14:
                            temp[l] = 4
                        else:
                            continue
        ans_sB.append(temp)
    return ans_sB

def LightSaber_attack(sB):
    ans_sB = []
    for i in range(k):
        negative_list = []
        temp = np.full(n, 100)
        for B in [16, 128, 192]:
            PA = []
            for j in range(k):
                PA.append(R_q(np.zeros(n)))
            PA[i].values[0] = B
            c = saber_oracle(PA,sB)
            if B == 16:
                for l in range(n):
                    if c.values[l] == 7 or c.values[l] == 3:
                        negative_list.append(True)
                    else:
                        negative_list.append(False)
            elif B == 128:
                for l in range(n):
                    if negative_list[l]:
                        if c.values[l] >= 4 and c.values[l] <= 6:
                            temp[l] = c.values[l]-8
                        elif c.values[l] >= 0 and c.values[l] <= 2:
                            temp[l] = c.values[l]-4
                        else:
                            continue
                    else:
                        if c.values[l] == 2 or c.values[l] == 3:
                            temp[l] = c.values[l]
                        elif c.values[l] == 6 or c.values[l] == 7:
                            temp[l] = c.values[l] - 4
                        else:
                            continue
            else:
                for l in range(n):
                    if temp[l] == 100:
                        if negative_list[l]:
                            if c.values[l] == 0 or c.values[l] == 4:
                                temp[l] = -5
                            elif c.values[l] == 2 or c.values[l] == 6:
                                temp[l] = -1
                            else:
                                continue
                        else:
                            if c.values[l] == 0 or c.values[l] == 4:
                                temp[l] = 0
                            elif c.values[l] == 1 or c.values[l] == 5:
                                temp[l] = 1
                            elif c.values[l] == 2 or c.values[l] == 6:
                                temp[l] = 4
                            elif c.values[l] == 3 or c.values[l] == 7:
                                temp[l] = 5
                            else:
                                continue
        ans_sB.append(temp)
    return ans_sB