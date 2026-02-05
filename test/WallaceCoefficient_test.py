from statistical_tests.wallace_coefficient import CT

def test_CT():
    ct, wallace = CT(dataframe=None, arr1=[1, 2, 1, 2], arr2=[1, 1, 2, 2])
    assert 0 <= wallace <= 1.0