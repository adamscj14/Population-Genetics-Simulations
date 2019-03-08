
import random

## Class that holds population object

class Population:

    def __init__(self, size, allele_frequency, a_advantage=0.0, A_advantage=0.0, mut_rate_a_to_A=0.0, mut_rate_A_to_a=0.0):

        self.size = size

        self.parent_allele_freq = float(allele_frequency)
        self.child_allele_freq = 0

        self.parent_individuals = self.init_individuals()
        self.child_individuals = []

        self.a_advantage = float(a_advantage)
        self.A_advantage = float(A_advantage)

        self.mut_a_to_A = float(mut_rate_a_to_A)
        self.mut_A_to_a = float(mut_rate_A_to_a)


    def init_individuals(self):

        hwe = self.get_hwe()
        individuals = list(range(self.size))
        count = 0
        for index in [0, 1, 2]:
            allele_one = 1
            allele_two = 1

            num_indivs = hwe[index]
            print(num_indivs)
            if index == 1:
                allele_one = 1
                allele_two = 0

            elif index == 2:
                allele_one = 0
                allele_two = 0

            for i in range(num_indivs):

                individuals[count] = DiploidIndividual(allele_one, allele_two)
                count += 1

        return individuals


    def advance_generation(self):

        if len(self.child_individuals) != 0:
            self.parent_individuals = self.child_individuals[:]

        child_individuals = list(range(self.size))

        A_allele_count = 0

        for i in child_individuals:

            # pick first parent
            parent_one_index = random.randint(0, self.size - 1)
            parent_two_index = parent_one_index
            parent_one = self.parent_individuals[parent_one_index]

            allele_one = parent_one.choose_allele()

            # pick second parent
            while parent_one_index == parent_two_index:
                parent_two_index = random.randint(0, self.size - 1)

            parent_two = self.parent_individuals[parent_two_index]

            allele_two = parent_two.choose_allele()

            child_individuals[i] = DiploidIndividual(allele_one, allele_two)

            A_allele_count += allele_one
            A_allele_count += allele_two


        self.child_individuals = child_individuals

        self.child_allele_freq = float(A_allele_count / (self.size * 2))





    def get_hwe(self):

        counts = [0, 0, 0]

        a_freq = 1 - self.parent_allele_freq

        AA_freq = self.parent_allele_freq ** 2
        Aa_freq = 2 * self.parent_allele_freq * a_freq
        aa_freq = a_freq ** 2

        counts[0] = round(AA_freq * self.size)
        counts[1] = round(Aa_freq * self.size)
        counts[2] = round(self.size - (counts[0] + counts[1]))

        return counts


## Class that holds diploid individual

class DiploidIndividual:

    def __init__(self, allele_one, allele_two):

        self.allele_one = allele_one
        self.allele_two = allele_two

    def choose_allele(self):

        allele = 0

        allele_num = random.randint(0,1)

        if allele_num == 0:
            allele = self.allele_one
        else:
            allele = self.allele_two

        return allele