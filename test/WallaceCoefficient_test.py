from discrimination_index import DiscriminationIndex

def test_CT():
    ct, wallace = CT(dataframe=None, arr1=[1, 2, 1, 2], arr2=[1, 1, 2, 2])
    assert 0 <= wallace <= 1.0