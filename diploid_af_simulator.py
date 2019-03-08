# Will drive actual simulations

import matplotlib.pyplot as plt
import population_class

generations = 1000
start_freq = 0.5
pop = population_class.Population(100, start_freq)
freqs = [start_freq]
for i in range(generations):
    pop.advance_generation()
    freqs.append(pop.child_allele_freq)

plt.plot(list(range(generations+1)), freqs)
plt.show()
