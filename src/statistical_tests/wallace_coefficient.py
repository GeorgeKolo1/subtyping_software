import numpy as np
import math
import pandas as pd

# Compute the contingency table for two arrays (subtyping methods)
def CT(arr1, arr2):
    
    ct_ab = pd.crosstab(arr1, arr2)
    ct_ab = ct_ab.to_numpy()
    ct_ba = pd.crosstab(arr2, arr1)
    ct_ba = ct_ba.to_numpy()

    return ct_ab, ct_ba

def Wallace(arr1, arr2):
    ''' Compute the wallace coefficient for two arrays (subtyping methods) in both directions'''

    ct_ab, ct_ba = CT(arr1, arr2)

    sum_ct_ab = np.sum((ct_ab * (ct_ab - 1)))
    row_sum_ab = np.sum(ct_ab, axis=1)
    denominator_ab = np.sum(row_sum_ab * (row_sum_ab - 1))

    sum_ct_ba = np.sum((ct_ba * (ct_ba - 1)))
    row_sum_ba = np.sum(ct_ba, axis=1)
    denominator_ba = np.sum(row_sum_ba * (row_sum_ba - 1))

    wallace_ab = sum_ct_ab / denominator_ab
    wallace_ba = sum_ct_ba / denominator_ba


    return wallace_ab, wallace_ba
                