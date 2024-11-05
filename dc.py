import matplotlib.pyplot as plt
import numpy as np

def xn(n):
    return (((2*n)%3)/3)*((20*n+1)/(n**2+2))

n = np.arange(1, 101)
x = xn(n)

n_even = np.arange(1, 100, 3)
x_even = xn(n_even)

fig, axes = plt.subplots(2, 1, figsize=(8, 8))

axes[0].plot(n, x, 'magenta', label='xn')
axes[0].plot(n_even, x_even, '#98FB98', label='x_mod_3', marker='o')

axes[0].axhline(y=14/3, color=(0.00, 0.83, 1.00), linestyle='-', label='sup xn')
axes[0].axhline(y=0, color=(1.00, 0.07, 0.00), linestyle='-', label='inf xn')
axes[0].axhline(y=14/3, color='magenta', linestyle=':', label='limsup xn')
axes[0].axhline(y=0, color=(1.00, 0.90, 0.00), linestyle=':', label='liminf xn')
axes[0].set_xlabel('n')
axes[0].set_ylabel('xn')
axes[0].set_title('График xn')

epsilons = [0.01, 0.001, 0.0001]
for i, epsilon in enumerate(epsilons):
    m = 0
    for j in range(len(x)):
        if x[j] > 14/3 - epsilon:
            m = j
            break
    axes[0].scatter(m + 1, x[m], color='yellow', marker='o')
    if i == 0:
        axes[0].scatter(m + 1, x[m], color='yellow', marker='o', label=f'm для ε = {epsilon}',s=100)

axes[0].legend()

epsilons = [0.01, 0.001, 0.0001]
colors = ['cyan', 'lime', 'red']
linestyles = ['-', '--', ':']

for i, epsilon in enumerate(epsilons):
    n0 = 0
    for j in range(len(x_even)):
        if abs(x_even[j] - 14/3) < epsilon:
            n0 = j
            break

    n_plot = n_even[n0:n0+100]
    x_plot = x_even[n0:n0+100]
    axes[1].plot(n_plot, x_plot, color=colors[i], linestyle=linestyles[i], label=f'ε = {epsilon}')

axes[1].axhline(y=14/3, color='magenta', linestyle='-', label='lim')
axes[1].set_xlabel('n')
axes[1].set_ylabel('xn')
axes[1].set_title('Графики x_mod_3 для ε')
axes[1].legend()

plt.tight_layout()
plt.show()
