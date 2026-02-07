import numpy as np
import math
import pandas as pd

# Compute the contingency table for two arrays (subtyping methods)
def CT(arr1, arr2, dataframe=None):
    
    if dataframe == None:
        if not isinstance(arr1, pd.Series):
            arr1 = pd.Series(arr1) 
        if not isinstance(arr2, pd.Series):
            arr2 = pd.Series(arr2)
        


    ''' Compute the contingency table for the wallace coefficient in the a->b direction where a is the first array/series provided'''
    r1, c1 = arr1.shape
    r2 ,c2 = arr2.shape

    if r1 != r2:
        raise ValueError("Arrays must have the same number of rows/observations/isolates")
    
    ct_ab = pd.crosstab(arr1, arr2)
    ct_ab = ct_ab.to_numpy()
    ct_ba = pd.crosstab(arr2, arr1)
    ct_ba = ct_ba.to_numpy

    return ct_ab, ct_ba

def Wallace(ct_ab, ct_ba):
    sum_ct_ab = np.sum((ct_ab * (ct_ab - 1)))
    row_sum_ab = np.sum(ct_ab, axis=1)
    denominator_ab = np.sum(row_sum_ab * row_sum_ab - 1)

    sum_ct_ba = np.sum((ct_ba * (ct_ba - 1)))
    row_sum_ba = np.sum(ct_ba, axis=1)
    denominator_ba = np.sum(row_sum_ba * row_sum_ba - 1)

    wallace_ab = sum_ct_ab / denominator_ab
    wallace_ba = sum_ct_ba / denominator_ba


    return wallace_ab, wallace_ba
                