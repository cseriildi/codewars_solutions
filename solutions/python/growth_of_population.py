# In a small town the population is p0 = 1000 at the beginning of a year. 
# The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
# How many years does the town need to see its population greater or equal to p = 1200 inhabitants?


def nb_year(p0, percent, aug, p):
    import math
    years = 0
    pop = p0
    while pop < p:
        pop = math.floor(pop * (1 + percent / 100)) + aug
        years += 1
        
    return years