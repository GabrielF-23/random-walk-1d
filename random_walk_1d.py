import matplotlib.pyplot as plt 
import random as random


def rw_1d(n):
    '''Caminhante Aleatório em 1D, onde 'n' = número de passos - 
       Random Walk 1D, where 'n' = number of steps'''

    #Origem em x = 0
    #Origin at x = 0
    x = 0
    a = [0]

    #Condição do caminhante aleatório em 1D 50% para direita ou 50% para esquerda.
    #Random Walk 1D condition 50% to right or 50% to left
    for i in range(n):
        step = random.choice([1,2])

        if step == 1:
            x += 1
        else:
            x -= 1

        a.append(x)
    return a


#Rodadas
#Runs.
r = 2

#Passos.
#Steps.
s = 3

#Lista de caminhadas.
#Walk list.
walk = []

#For que gera varios caminhantes da origem.
#Loop that create multiple walkers from the origin.
for i in range(r):
    walk.append(rw_1d(s))

#Gera o subplot.
#Generate the subplot.
fig, axs = plt.subplots(1, 2, figsize=(12,5), dpi=120)


#Lista de pontos finais das trajetórias.
#Endpoints of the trajectories list.
endp = []

#Percorre a lista 'walk' e cria lista de todos os pontos finais das trajetórias.
#Iterates through the 'walk' list and creates a list of all the endpoints of the trajectories.
for a in walk:
    axs[0].plot(a)
    endp.append(a[-1])



#Título principal.
#Main tittle.
fig.suptitle(
    "Caminhante Aleatório 1D",
    fontsize=14
)

if r == 1:
    sim = f'{r} Simulação'
else:
    sim = f'{r} Simulações'

#Trajetórias dos caminhantes.
#Random walk trajectories.
axs[0].set_title(f"Trajetória Caminhante Aleatório.\n {s} Passos - {sim}")
axs[0].set_xlabel("Passos")
axs[0].set_ylabel("Posição")
axs[0].grid()

#Histograma das posições finais.
#Histogram of final positions.
axs[1].hist(endp, bins=30)
axs[1].set_title(f"Histograma de Posições Finais\n {s} Passos - {sim}")
axs[1].set_xlabel("Posição X")
axs[1].set_ylabel("Probabilidade de cair em X")
axs[1].grid()

plt.tight_layout()
plt.show()

