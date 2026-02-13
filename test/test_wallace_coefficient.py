import pandas as pd
import numpy as np
from src.statistical_tests import wallace_coefficient as wc

def test_wallace():
    """Function to test the wallace coefficient function
    
    This function takes test data and runs the wallace coefficient function on it, then checks if 
        out is as expected 
        
    Args:
        
    Returns:
        A pytest assert statement that checks if the output of the wallace coefficient function is as expected
"""
    data = pd.read_csv('test/test_data_folder/test_data.csv')
    data = data.to_numpy()
    wc_ab, wc_ba = wc.WallaceCoefficient(data[0], data[1])

    assert wc_ab != wc_ba
    assert wc_ab > 0 and wc_ab <= 1
    assert wc_ba > 0 and wc_ba <= 1


