import matplotlib.pyplot as plt
import numpy as np

def random_walk1d(n_steps, sigma):
    x = 0

    trajectory = [0]

    for i in range(n_steps):

        step = np.random.normal(0, sigma)

        x += step

        trajectory.append(x)

    return trajectory


n_steps = 1000

n_runs = 1000

sigma = 0.1


walks = []


for i in range(n_runs):
    walks.append(random_walk1d(n_steps,sigma))


fig, axs = plt.subplots(1,3, figsize=(18,5), dpi=120)


for walk in walks:
    axs[0].plot(walk)


axs[0].set_title("Trajetórias dos Caminhantes")
axs[0].set_xlabel("Passos")
axs[0].set_ylabel("X")
axs[0].grid()


endp = []


for walk in walks:
    endp.append(walk[-1])


axs[1].hist(endp,bins=50,density=True)

axs[1].set_title("Distribuição Final")
axs[1].set_xlabel("Posição X Final")
axs[1].set_ylabel("Densidade")
axs[1].grid()


msd = []


for t in range(n_steps+1):

    x_s = []


    for walk in walks:

        x_s.append(walk[t]**2)


    msd.append(np.mean(x_s))


axs[2].plot(
    range(n_steps+1),
    msd,
    label="Caminhantes"
)


axs[2].plot(
    range(n_steps+1),
    sigma**2*np.arange(n_steps+1),
    label="DQM"
)


axs[2].set_title("Deslocamento Quadrático Médio")
axs[2].set_xlabel("Passos")
axs[2].set_ylabel("<x²>")
axs[2].grid()
axs[2].legend()


fig.suptitle(
    f"Caminhante Aleatório Gaussiano 1D\n"
    f"Δx ~ N(0, {sigma}) | {n_steps} passos - {n_runs} simulações",
    fontsize=14
)


plt.tight_layout()
plt.show()
