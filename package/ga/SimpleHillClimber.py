from typing import List, Tuple
from .AbstractFitness import AbstractFitness


class SimpleHillClimber(object):
    def __init__(self, fitness: AbstractFitness, gene_mutators = [], individual_mutators = []):
        self.fitness = fitness
        self.gene_mutators = gene_mutators
        self.individual_mutators = individual_mutators

    def run(self, individual: List[any], iterations: int = 1000, display_logging: bool = False) -> Tuple[List[any], float, int]:
        for iteration in range(iterations):
            current_individual_fitness = self.fitness.evaluate(individual)
            if (current_individual_fitness >= 1):
                ## finished early,
                break

            if display_logging:
                print('iteration:', iteration, '=', current_individual_fitness)

            new_individual = []
            for gene in individual:
                for gene_mutator in self.gene_mutators:
                    gene = gene_mutator(gene, display_logging)

                new_individual.append(gene)

            for individual_mutator in self.individual_mutators:
                new_individual = individual_mutator(new_individual, display_logging)

            new_individual_fitness = self.fitness.evaluate(new_individual, display_logging)
            if new_individual_fitness > current_individual_fitness:
                individual = new_individual

        return (
            individual,
            self.fitness.evaluate(individual),
            iteration
        )
