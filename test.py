people = {
  'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
  'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
  'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
}

name = 'Harry'
PROBS = {
    # Unconditional probabilities for having gene
    "gene": {2: 0.01, 1: 0.03, 0: 0.96},
    "trait": {
        # Probability of trait given two copies of gene
        2: {True: 0.65, False: 0.35},
        # Probability of trait given one copy of gene
        1: {True: 0.56, False: 0.44},
        # Probability of trait given no gene
        0: {True: 0.01, False: 0.99},
    },
    # Mutation probability
    "mutation": 0.01,
}



def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    probailitis_to_join = []

    def check_for_parents(person):
        if person['mother'] == None or person['father'] == None:
            return False
        return True

    for name in people:
        check_parents = check_for_parents(people[name])
        trait_factor = 0
        gene_factor = 0
        genes_number = 0
        trait_status = False

        if name in one_gene:
            genes_number = 1
        if name in two_genes:
            genes_number = 2
        if name in have_trait:
            trait_status = True

        trait_factor = PROBS['trait'][genes_number][trait_status]

        if check_parents:
            mother_genes = 0
            father_genes = 0
            from_mother = 0
            not_from_mother = 0
            from_father = 0
            not_from_father = 0

            def gene_passover_chance(gene_number):
                passed = 0
                no_passed = 0

                if(gene_number == 0):
                    passed = 0.01
                    no_passed = 0.99
                elif(gene_number == 1):
                    passed = 0.51
                    no_passed = 0.51
                elif(gene_number == 2):
                    passed = 0.99
                    no_passed = 0.01
                return [passed, no_passed]

            if(people[name]['mother'] in one_gene):
                mother_genes = 1
            if(people[name]['mother'] in two_genes):
                mother_genes = 2
            if(people[name]['father'] in one_gene):
                father_genes = 1
            if(people[name]['father'] in two_genes):
                father_genes = 2            
            
            [from_mother, not_from_mother] = gene_passover_chance(mother_genes)
            [from_father, not_from_father] = gene_passover_chance(father_genes)

            if(genes_number == 0):
                gene_factor = not_from_father + not_from_mother
            if(genes_number == 1):
                gene_factor = from_father * not_from_mother + from_mother * not_from_father
            if(genes_number == 2):
                gene_factor = from_father + from_mother

        else:
            gene_factor = PROBS['gene'][genes_number]

        probailitis_to_join.append(trait_factor*gene_factor)

    propability = 1
    for number in probailitis_to_join:
        propability = propability * number

    return propability
print(joint_probability(people, {"Harry"}, {"James"}, {"James"}))