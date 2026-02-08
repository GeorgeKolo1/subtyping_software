import numpy as np
import math
import pandas as pd

def DiscriminationIndex(sm):
    if isinstance(sm, pd.DataFrame) == True:
        return("This is a dataframe, series or np array required")
    elif isinstance(sm, pd.Series) == True:
        sm.to_numpy
    
    #discrimination index calculation (Hunter and Gaston)

    N = len(sm)
    s  = np.unique(sm, return_counts=True)
    summation_list =[]
    for i in s[1]:
        y = (i * (i-1))
        summation_list.append(y)
    D = 1 - (sum(summation_list)) / (N * (N-1))
    #95% CI calculation (Grundmann, Hori & Tanner, 2001)

    summation_pi_j3 = []
    summation_pi_j2 = []
    for i in s[1]:
        pi_j = i/N
        pi_j3 = pi_j ** 3
        pi_j2 = pi_j ** 2
        summation_pi_j3.append(pi_j3)
        summation_pi_j2.append(pi_j2)

    pi_j3 = sum(summation_pi_j3)
    pi_j2 = (sum(summation_pi_j2) ** 2)
    S2 = (4/N) * (pi_j3 - pi_j2)
    CI_low = (D - (2 * math.sqrt(S2)))
    CI_high = (D + (2 * math.sqrt(S2)))

    return(round(D, 3), round(CI_low, 3), round(CI_high, 3))


