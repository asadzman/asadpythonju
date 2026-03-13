import pytest_lazyfixture

def calculate_power(base,exponent):
    return base**exponent

@pytest.mark.parametrize("base,exponent,expected",[
    (2,2,4),(2,3,8),(1,9,1),(0,9,0)
])
def test_power_values(base,exponent,expected):
    assert calculate_power(base,exponent)==expected

def test_power_error():
    with pytest.raises(ZeroDivisionError):
        calculate_power(0,-1)