# Will drive actual simulations

import population_class

generations = 1000

pop = population_class.Population(100, 0.5)

for i in range(generations):
    print(pop.child_allele_freq)
    pop.advance_generation()

