#function to calculate necessary weight of a solid solution based on database of molecular weights and input of concentrations
def calculate_solution_weights(molecular_weights,solutions_needed):

    #parsing solution name from list to compare against molecular_weights keys
    soln_name = tuple([item.split('-')[0] for item in solutions_needed])

    #extracting concentrations of solutions for calculating needed weights
    conc = [str(sub.split('-')[1]) for sub in solutions_needed]
    conc_num = [float(item.split('M')[0]) for item in conc]

    #creating empty list for final output
    results = []

    #for loop and try-except to test if solutions_needed variable matches molecular_weights keys
    for item in range(len(soln_name)):
        try:
            mol_weight = molecular_weights[soln_name[item]]
            weight = mol_weight * conc_num[item]
            results.append(soln_name[item] + "-" + conc[item] + "-" + str(weight) + "g")

        #appends "unknown" error message if the list variable does not match dict key
        except KeyError:
            results.append("unknown")
    return results