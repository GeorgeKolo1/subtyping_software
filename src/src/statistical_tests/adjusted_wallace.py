from discrimination_index import DiscriminationIndex

def AdjustedWallace(arr1, arr2, wallace_ab, wallace_ba):
    '''Calculates the adjusted wallace coefficient which is: 
        Adjusted Wallace = W(a->b) - Wi(a->b) / (1 - Wi(a->b) )
        
        For the case of W(b->a) the inverse is computed where Wi(b->a) is used instead
        
        Takes: Arr1 - pandas series or numpy array containing the subtypes of subtyping method X
            Arr2 - pandas or numpy array containing the subtypes of subtyping method Y
            wallace_ab - wallace coefficient in diretion a->b
            wallace_ba - wallace coefficient in diretion b->a '''
    
    
    Da, Da_low, Da_high = DiscriminationIndex(arr1)
    Db, Db_low, Db_high = DiscriminationIndex(arr2)

    Wi_ab = 1 - Db
    Wi_ba = 1 - Da

    AW_ab = (wallace_ab - Wi_ab) / (1 - Wi_ab)
    AW_ba = (wallace_ba - Wi_ba) / (1- Wi_ba)

    return AW_ab, AW_ba