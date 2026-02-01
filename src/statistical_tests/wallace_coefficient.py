import numpy as np
import math
import pandas as pd

# Compute the contingency table for two arrays (subtyping methods)
def CT(dataframe, arr1, arr2):
    
    if not isinstance(arr1, pd.Series):
        arr1 = pd.Series(arr1) 
    if not isinstance(arr1, pd.Series):
        arr2 = pd.Series(arr2)
        
    

    ''' Compute the contingency table for the wallace coefficient'''
    r1, c1 = arr1.shape
    r2 ,c2 = arr2.shape

    if r1 != r2:
        raise ValueError("Arrays must have the same number of rows/observations/isolates")
    
    ct = pd.crosstab(arr1, arr2)
    ct = ct.to_numpy()

    sum_ct = np.sum((ct * (ct - 1)))
    row_sum = np.sum(ct, axis=1)
    denominator = np.sum(row_sum * row_sum - 1)

    wallace = sum_ct / denominator

    return ct, wallace
                