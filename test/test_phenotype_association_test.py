import numpy as np
import pandas as pd
from src.statistical_tests.phenotype_association_test import AssociationTest

def test_association_test():
    '''
    
    
    
    
    
    
    '''
    data = pd.read_csv('test/test_data_folder/test_data.csv')
    data = data.to_numpy
    arr1 = data[:, 1]
    