import numpy as np
import csv

def Randomwalkcounter(R2goal):
    cycling = True
    xspot = 0
    yspot = 0
    zspot = 0
    counter = 0
    while cycling:
        [a,b] = [np.random.random()*np.pi,2*np.random.random()*np.pi]
        xspot += np.sin(a)*np.cos(b)
        yspot += np.sin(a)*np.sin(b)
        zspot += np.cos(a)
        R2 = xspot**2+yspot**2+zspot**2
        counter += 1
        cycling = R2<R2goal
    return [R2, counter]

Rgoal = 1000
R2goal = Rgoal**2
simulations = 10
totalN = 0
totalR = 0
totalR2 = 0

with open('file.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',')
    for i in range(simulations):
        print("iteración: "+str(i+1))
        [R2,N] = Randomwalkcounter(R2goal)
        print("R alcanzado: "+str(np.sqrt(R2)))
        print("N: "+str(N))
        totalR += np.sqrt(R2)
        totalN += N
        totalR2 += R2
        filewriter.writerow([i+1,np.sqrt(R2),N])

avgN = totalN/simulations
avgR = totalR/simulations
avgR2 = totalR2/simulations

print("N promedio: "+str(avgN))
print("R promedio: "+str(avgR))
print("R(rms): "+str(np.sqrt(avgR2)))
