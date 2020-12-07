from attack import *

sB = []
for i in range(k):
    sB.append(binomial_distribution())
#ans_sB = FireSaber_attack(sB)
#ans_sB = Saber_attack(sB)
ans_sB = LightSaber_attack(sB)


#mistake counter
counter = 0
for i in range(k):
    for j in range(n):
        if ans_sB[i][j] == sB[i].values[j]:
            counter += 1
        else:
            print("error")
            print(sB[i].values[j], ans_sB[i][j])
print(counter)