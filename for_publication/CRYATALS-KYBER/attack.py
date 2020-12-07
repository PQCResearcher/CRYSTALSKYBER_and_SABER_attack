from kyber import *

def kyber_oracle(PA, sB):
    m = R_q(np.random.randint(0, 2, n))
    eBP = binomial_distribution()
    vB = R_q(np.zeros(n))
    for i in range(k):
        vB += PA[i]*sB[i]
    vB += (eBP+decompress(1, m))
    c2 = compress(dvB, vB)
    return c2

def kyber_768_1024_attack(sB):
    B = math.ceil(q/2**dvB)+4
    ans_sB = []
    for i in range(k):
        PA = []
        for j in range(k):
            PA.append(R_q(np.zeros(n)))
        PA[i].values[0] = B
        c2 = kyber_oracle(PA, sB)
        temp = []
        for l in range(n):
            if c2.values[l] >= 2**(dvB-1)-eta and c2.values[l] <= 2**(dvB-1)+eta:
                temp.append(c2.values[l]-2**(dvB-1))
            elif c2.values[l] <= eta:
                temp.append(c2.values[l])
            else:
                temp.append(c2.values[l]-2**dvB)
        ans_sB.append(temp)
    return ans_sB

def kyber_512_attack(sB):
    ans_sB = []
    for i in range(k):
        temp = np.full(n, 100)
        for B in [421, 631]:
            PA = []
            for j in range(k):
                PA.append(R_q(np.zeros(n)))
            PA[i].values[0] = B
            c2 = kyber_oracle(PA,sB)
            if B == 421:
                for l in range(n):
                    if c2.values[l] == 2 or c2.values[l] == 6:
                        continue
                    elif c2.values[l] >= 3 and c2.values[l] <= 5:
                        temp[l] = c2.values[l]-2**(dvB-1)
                    elif c2.values[l] == 0 or c2.values[l] == 1:
                        temp[l] = c2.values[l]
                    else:
                        temp[l] = c2.values[l]-2**dvB
            else:
                for l in range(n):
                    if c2.values[l] == 1 or c2.values[l] == 5:
                        temp[l] = -2
                    if c2.values[l] == 3 or c2.values[l] == 7:
                        temp[l] = 2
        ans_sB.append(temp)
    return ans_sB