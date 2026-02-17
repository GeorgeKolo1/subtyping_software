from src.statistical_tests.discrimination_index import DiscriminationIndex
from src.statistical_tests.wallace_coefficient import Wallace

def AdjustedWallace(arr1, arr2):
    '''Calculates the adjusted wallace coefficient 
    
    This function computes the adjusted Wallace coefficient which is = W(a->b) - Wi(a->b) / (1 - Wi(a->b))
    Where W(a->b) is the wallace coefficient in direction a->b and Wi(a->b) is the wallace coefficient under independence,
    in other words that wallace coefficient if the two subtyping methods were completely independent.
        
    Args:
        arr1 - pandas series or numpy array containing the subtypes of subtyping method a
        arr2 - pandas or numpy array containing the subtypes of subtyping method b
        wallace_ab - wallace coefficient in diretion a->b
        wallace_ba - wallace coefficient in diretion b->a 
        
    Returns:
        AW_ab (float) - adjusted wallace coefficient in direction a->b
        AW_ba (float) - adjusted wallace coefficient in direction b->a

    Raises:
        ValueError: 1.If the input arrays do not have the same number of samples
                    2. Are not one-dimensional
        
    '''
    if arr1.shape[0] != arr2.shape[0]:
        raise ValueError("Input arrays must have the same number of samples")
    if len(arr1.shape) != 1 or len(arr2.shape) != 1:
        raise ValueError("Input arrays must be one-dimensional")
    if arr1.dtype != arr2.dtype:
        arr1 = arr1.astype(str)
        arr2 = arr2.astype(str)
    
    Da, Da_low, Da_high = DiscriminationIndex(arr1)
    Db, Db_low, Db_high = DiscriminationIndex(arr2)

    wallace_ab, wallace_ba = Wallace(arr1, arr2)

    Wi_ab = 1 - Db
    Wi_ba = 1 - Da

    AW_ab = (wallace_ab - Wi_ab) / (1 - Wi_ab)
    AW_ba = (wallace_ba - Wi_ba) / (1- Wi_ba)

    return AW_ab, AW_ba